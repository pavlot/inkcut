# -*- coding: utf-8 -*-
"""
Copyright (c) 2017-2024, Pavlo Taranov.

Distributed under the terms of the GPL v3 License.

The full license is in the file LICENSE, distributed with this software.

Created on Sep 20, 2024

@author: pavlot
"""
import traceback
from atom.atom import set_default
from atom.api import List, Instance, Str, Bool
from inkcut.core.api import Plugin, Model, log
from inkcut.device.plugin import DeviceTransport
from serial.tools.list_ports import comports

import usb.core
import usb.util


class UsbDeviceDescriptor:
    def __init__(self, vendor_id, product_id, serial):
        self.__vendor_id = vendor_id
        self.__product_id = product_id
        self.__serial = serial

    def __str__(self):
        return "{} ({}:{})".format(self.__serial, self.__vendor_id, self.__product_id)

    def matcher(self, dev):
        return (
            self.__vendor_id == dev.idVendor
            and self.__product_id == dev.idProduct
            and self.__serial == dev.serial_number
        )


class UsbDeviceEnumerator:
    PRINTER_DEVICE_CLASS = 7

    class class_filter(object):
        def __init__(self, class_):
            self._class = class_

        def __call__(self, device):
            if device.bDeviceClass == self._class:
                return True
            for cfg in device:
                intf = usb.util.find_descriptor(cfg, bInterfaceClass=self._class)
                if intf is not None:
                    return True
            return False

    def list():
        log.info("Updating USB device list")
        result = []
        for dev in usb.core.find(
            find_all=True,
            custom_match=UsbDeviceEnumerator.class_filter(UsbDeviceEnumerator.PRINTER_DEVICE_CLASS),
        ):
            result.append(UsbDeviceDescriptor(dev.idVendor, dev.idProduct, dev.serial_number))
        return result


class UsbDeviceConfig(Model):
    device_descriptors = List()

    selected_device = Instance(UsbDeviceDescriptor)

    def _default_device_descriptors(self):
        return UsbDeviceEnumerator.list()

    def _default_selected_device(self):
        if self.device_descriptors:
            return self.device_descriptors[0]
        return None

    def refresh(self):
        self.device_descriptors = UsbDeviceEnumerator.list()


class UsbDeviceTransport(DeviceTransport):

    #: Default config
    config = Instance(UsbDeviceConfig, ()).tag(config=True)

    device = Instance(usb.core.Device)
    ep_in = Instance(usb.core.Endpoint)
    ep_out = Instance(usb.core.Endpoint)

    reattach_kernel_driver = Bool(False)

    def connect(self):
        config = self.config
        log.info("Connecting to USB device {}".format(config.selected_device))
        devices = list(usb.core.find(find_all=True, custom_match=config.selected_device.matcher))
        if len(devices) > 0:
            dev = devices[0]
            if dev.is_kernel_driver_active(0):
                dev.detach_kernel_driver(0)
                self.reattach_kernel_driver = True
            dev.set_configuration()

            # get an endpoint instance
            cfg = dev.get_active_configuration()

            intf = cfg[(0, 0)]

            self.ep_out = usb.util.find_descriptor(
                intf,
                custom_match=lambda e: usb.util.endpoint_direction(e.bEndpointAddress)
                == usb.util.ENDPOINT_OUT,
            )
            self.ep_in = usb.util.find_descriptor(
                intf,
                # match the first OUT endpoint
                custom_match=lambda e: usb.util.endpoint_direction(e.bEndpointAddress)
                == usb.util.ENDPOINT_IN,
            )

            self.device = dev
            self.connected = True

    def write(self, data):
        log.info("Writing: {}".format(data))
        self.ep_out.write(data)

    def read(self, size=None):
        """Read using whatever implementation necessary and
        invoke `protocol.data_received` with the output.

        """
        raise NotImplementedError

    def disconnect(self):
        try:
            log.info("Disconnecting USB device")
            if self.device:
                usb.util.dispose_resources(self.device)
                self.device.reset()
                if self.reattach_kernel_driver:
                    self.device.attach_kernel_driver(0)
                self.device = None
                self.ep_out = None
                self.ep_in = None
                self.connected = False
        except Exception as e:
            log.warning("{}.{}".format(e.__class__.__qualname__, e))


class UsbDevicePlugin(Plugin):
    """Plugin for handling usb device communication"""

    # -------------------------------------------------------------------------
    # UsbDevicePlugin API
    # -------------------------------------------------------------------------
