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
from atom.api import List, Instance, Str
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

    def connect(self):
        """Connect using whatever implementation necessary"""
        raise NotImplementedError

    def write(self, data):
        """Write using whatever implementation necessary"""
        raise NotImplementedError

    def read(self, size=None):
        """Read using whatever implementation necessary and
        invoke `protocol.data_received` with the output.

        """
        raise NotImplementedError

    def disconnect(self):
        """Disconnect using whatever implementation necessary"""
        raise NotImplementedError


class UsbDevicePlugin(Plugin):
    """Plugin for handling usb device communication"""

    # -------------------------------------------------------------------------
    # UsbDevicePlugin API
    # -------------------------------------------------------------------------
