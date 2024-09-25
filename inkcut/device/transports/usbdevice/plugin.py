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

from inkcut.device.transports.raw.plugin import RawFdProtocol


import usb.core
import usb.util


class UsbDeviceEnumerator:
    PRINTER_DEVICE_CLASS = 7

    class class_filter(object):
        def __init__(self, class_):
            self._class = class_

        def __call__(self, device):
            # first, let's check the device
            if device.bDeviceClass == self._class:
                return True
            # ok, transverse all devices to find an
            # interface that matches our class
            for cfg in device:
                # find_descriptor: what's it?
                intf = usb.util.find_descriptor(cfg, bInterfaceClass=self._class)
                if intf is not None:
                    return True

            return False

    def list():
        result = []
        # for dev in usb.core.find(idVendor=0x0b4d, idProduct=0x1133):
        for dev in usb.core.find(
            find_all=True,
            custom_match=UsbDeviceEnumerator.class_filter(UsbDeviceEnumerator.PRINTER_DEVICE_CLASS),
        ):
            result.append(dev)
        return result


class UsbDeviceConfig(Model):
    #: Available usb devices
    devices = []
    device_names = List()

    def refresh(self):
        self.devices.clear()
        device_names = []
        for dev in UsbDeviceEnumerator.list():
            device_name = "{}:{}".format(dev.idVendor, dev.idProduct)
            log.info("Found device {}".format(device_name))
            self.devices.append(dev)
            device_names.append(device_name)
        self.device_names = device_names
        log.info(self.device_names)


class UsbDeviceTransport(DeviceTransport):

    #: Default config
    config = Instance(UsbDeviceConfig, ()).tag(config=True)

    def connect(self):
        pass


class UsbDevicePlugin(Plugin):
    """Plugin for handling usb device communication"""

    # -------------------------------------------------------------------------
    # UsbDevicePlugin API
    # -------------------------------------------------------------------------
