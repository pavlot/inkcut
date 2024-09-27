"""
Copyright (c) 2017, Vinylmark LLC.

Distributed under the terms of the GPL v3 License.

The full license is in the file LICENSE, distributed with this software.

Created on Jan 24, 2015

@author: jrm
@author: jjm
"""

import time
import pstats
from cProfile import Profile
from atom.api import Instance, Str, List, Int, Float, Tuple, Dict, Bool, observe
from inkcut.core.api import Model
from inkcut.core.utils import async_sleep, log
from inkcut.device.plugin import Device, DeviceConfig
from twisted.internet.defer import inlineCallbacks, DeferredList
from contextlib import contextmanager
from enaml.qt import QtGui

try:
    import RPi.GPIO as GPIO

    GPIO_AVAILABLE = True
except ImportError:
    GPIO_AVAILABLE = False

try:
    #: Moved here so I can still test it on the desktop
    from . import registration

    CM_AVAILABLE = True
except ImportError:
    registration = None
    CM_AVAILABLE = False

PROFILER = Profile()


class GraphtecCeLite50Config(DeviceConfig):
    pass

class GraphtecCeLite50Device(Device):

    config = Instance(GraphtecCeLite50Config, ())

# -----------------------------------------------------------


class ConditionConfig(DeviceConfig):
    tool = Str()
    offset = Int()
    speed = Int()
    force = Int()
    accel = Int()
    initial_down_force = Int()
    cut_line_pattern = Bool()
    ltype_up = Str()  # Should be float, but how it is parsed with units mm/inch?
    ltype_dwn = Str()  # Should be float, but how it is parsed with units mm/inch?
    up_mode = Str()  # TODO Discover values: 'up'
    tangential_mode = Int()  # TODO Discover values
    overcut_s_e = Str()  # 0.0mm,0.0mm
    d_adj = Bool()  # Off
    x = Float()
    y = Float()
