from atom.api import Instance, Str


def plotter_parameter_factory(parameter_name):
    parameter_name_to_class = {
        "TOOL": Tool,
        "OFFSET": Offset,
        "SPEED": Speed,
        "FORCE": Force,
        "ACCEL.": Accel,
        "INITIAL DOWN FORCE": InitialDownForce,
        "CUT LINE PATTERN": CutLinePattern,
        "LTYPE UP": LtypeUp,
        "LTYPE DWN": LtypeDwn,
        "UP MODE": UpMode,
        "TANGENTIAL MODE": TangentialMode,
        "OVERCUT S.E.": OvercutSE,
        "D. ADJ.": DAdj,
        "X": X,
        "Y": Y,
        "STEP PASS": StepPass,
        "OFFSET FORCE": OffsetForce,
        "OFFSET ANGLE": OffsetAngle,
        "DATA SORT": DataSort,
        "TOOL UP SPEED": ToolUpSpeed,
        "CONDITION PRIORITY": ConditionPriority,
        "INITIAL BLADE": InitialBlade,
        "TOOL UP MOVE": ToolUpMove,
        "MARK SCAN MODE": MarkScanMode,
        "NUMBER OF POINTS": NumberOfPoints,
        "MARK DISTANCE x,y": MarkDistanceXY,
        "SENSING SPEED": SensingSpeed,
        "MARK TYPE": MarkType,
        "D. ADJ. MODE": DAdjMode,
        "MARK DIST.ADJ.UNIT": MarkDistAdjUnit,
        "MARK OFFSET x,y": MarkOffsetXY,
        "MARK AUTO SCAN": MarkAutoScan,
        "PAPER-WEIGHT": PaperWeight,
        "SENSOR OFFSET ADJ.": SensorOffsetAdj,
        "MARK SIZE": MarkSize,
        "SENSOR ADJUST": SensorAdjust,
        "SENSING LEVEL(X,Y)": SensingLevelXY,
        "FACTORY SENSOR GAIN": FactorySensorGain,
        "FACTORY BASE LEVEL": FactoryBaseLevel,
        "FACTORY SENSING LEVEL(X,Y)": FactorySensingLevelXY,
        "USER SENSOR GAIN": UserSensorGain,
        "USER BASE LEVEL": UserBaseLevel,
        "USER SENSING LEVEL(X,Y)": UserSensingLevelXY,
        "RM SENSOR LEVEL ADJ SELECT": RmSensorLevelAdjSelect,
        "EXPAND": Expand,
        "ROTATE": Rotate,
        "MIRROR": Mirror,
        "SCALE": Scale,
        "INITIAL FEED": InitialFeed,
        "FEED SPEED": FeedSpeed,
        "AUTO PRE FEED": AutoPreFeed,
        "AUTO PRE FEED LENGTH": AutoPreFeedLength,
        "PAGE LENGTH": PageLength,
        "PRE FEED": PreFeed,
        "PANEL CUTTING": PanelCutting,
        "DIVIDE LENGTH": DivideLength,
        "BAUD RATE": BaudRate,
        "PARITY": Parity,
        "DATA BIT": DataBit,
        "HANDSHAKE": Handshake,
        "COMMAND": Command,
        "GP-GL STEP SIZE": GpGlStepSize,
        "HP-GL ORIGIN": HpGlOrigin,
        "HP-GL MODEL EMULATED": HpGlModelEmulated,
        "CIRCLE RESOLUTION": CircleResolution,
        "COMMAND ':',';'": CommandColSemiCol,
        "COMMAND 'W'": CommandW,
        "MOVE STEP": MoveStep,
        "LANGUAGE SELECTION": LanguageSelection,
        "LENGTH UNIT": LengthUnit,
        "MEDIA SENSOR": MediaSensor,
        "PUSH ROLLER SENSOR": PushRollerSensor,
        "FAN POWER": FanPower,
        "BEEP FOR KEY OPE.": BeepForKeyOpe,
        "COPY SPACE": CopySpace,
    }

    class_name = parameter_name_to_class.get(parameter_name, None)
    if not class_name:
        return None

    return class_name()


# ----------------------------------------------------------------------------------------------------


class PlotterParameter:
    def __init__(self):
        self._name = "Tool"
        self._device_name = "TOOL"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------
    def get_name(self):
        return self._name

    # ------------------------------------------------------------------------------------------------
    def get_device_name(self):
        return self._device_name

    # ------------------------------------------------------------------------------------------------
    def get_value(self):
        return self._value

    # ------------------------------------------------------------------------------------------------
    def set_value(self, value):
        self._value = value

    # ------------------------------------------------------------------------------------------------
    def is_readonly(self):
        return self._is_readonly

    def get_update_command(self):
        raise Exception("get_update_command not implemented")


# ----------------------------------------------------------------------------------------------------


class Tool(PlotterParameter):

    def __init__(self):
        self._name = "Tool"
        self._device_name = "TOOL"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class Offset(PlotterParameter):

    def __init__(self):
        self._name = "Offset"
        self._device_name = "OFFSET"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class Speed(PlotterParameter):

    def __init__(self):
        self._name = "Speed"
        self._device_name = "SPEED"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class Force(PlotterParameter):

    def __init__(self):
        self._name = "Force"
        self._device_name = "FORCE"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class Accel(PlotterParameter):

    def __init__(self):
        self._name = "Accel"
        self._device_name = "ACCEL."
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class InitialDownForce(PlotterParameter):

    def __init__(self):
        self._name = "Initial down force"
        self._device_name = "INITIAL DOWN FORCE"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class CutLinePattern(PlotterParameter):

    def __init__(self):
        self._name = "Cut line pattern"
        self._device_name = "CUT LINE PATTERN"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class LtypeUp(PlotterParameter):

    def __init__(self):
        self._name = "Ltype up"
        self._device_name = "LTYPE UP"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class LtypeDwn(PlotterParameter):

    def __init__(self):
        self._name = "Ltype dwn"
        self._device_name = "LTYPE DWN"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class UpMode(PlotterParameter):

    def __init__(self):
        self._name = "Up mode"
        self._device_name = "UP MODE"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class TangentialMode(PlotterParameter):

    def __init__(self):
        self._name = "Tangential mode"
        self._device_name = "TANGENTIAL MODE"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class OvercutSE(PlotterParameter):

    def __init__(self):
        self._name = "Overcut se"
        self._device_name = "OVERCUT S.E."
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class DAdj(PlotterParameter):

    def __init__(self):
        self._name = "D adj"
        self._device_name = "D. ADJ."
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class X(PlotterParameter):

    def __init__(self):
        self._name = "X"
        self._device_name = "X"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class Y(PlotterParameter):

    def __init__(self):
        self._name = "Y"
        self._device_name = "Y"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class Tool(PlotterParameter):

    def __init__(self):
        self._name = "Tool"
        self._device_name = "TOOL"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class Offset(PlotterParameter):

    def __init__(self):
        self._name = "Offset"
        self._device_name = "OFFSET"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class Speed(PlotterParameter):

    def __init__(self):
        self._name = "Speed"
        self._device_name = "SPEED"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class Force(PlotterParameter):

    def __init__(self):
        self._name = "Force"
        self._device_name = "FORCE"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class Accel(PlotterParameter):

    def __init__(self):
        self._name = "Accel"
        self._device_name = "ACCEL."
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class InitialDownForce(PlotterParameter):

    def __init__(self):
        self._name = "Initial down force"
        self._device_name = "INITIAL DOWN FORCE"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class CutLinePattern(PlotterParameter):

    def __init__(self):
        self._name = "Cut line pattern"
        self._device_name = "CUT LINE PATTERN"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class LtypeUp(PlotterParameter):

    def __init__(self):
        self._name = "Ltype up"
        self._device_name = "LTYPE UP"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class LtypeDwn(PlotterParameter):

    def __init__(self):
        self._name = "Ltype dwn"
        self._device_name = "LTYPE DWN"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class UpMode(PlotterParameter):

    def __init__(self):
        self._name = "Up mode"
        self._device_name = "UP MODE"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class TangentialMode(PlotterParameter):

    def __init__(self):
        self._name = "Tangential mode"
        self._device_name = "TANGENTIAL MODE"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class OvercutSE(PlotterParameter):

    def __init__(self):
        self._name = "Overcut se"
        self._device_name = "OVERCUT S.E."
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class DAdj(PlotterParameter):

    def __init__(self):
        self._name = "D adj"
        self._device_name = "D. ADJ."
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class X(PlotterParameter):

    def __init__(self):
        self._name = "X"
        self._device_name = "X"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class Y(PlotterParameter):

    def __init__(self):
        self._name = "Y"
        self._device_name = "Y"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class Tool(PlotterParameter):

    def __init__(self):
        self._name = "Tool"
        self._device_name = "TOOL"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class Offset(PlotterParameter):

    def __init__(self):
        self._name = "Offset"
        self._device_name = "OFFSET"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class Speed(PlotterParameter):

    def __init__(self):
        self._name = "Speed"
        self._device_name = "SPEED"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class Force(PlotterParameter):

    def __init__(self):
        self._name = "Force"
        self._device_name = "FORCE"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class Accel(PlotterParameter):

    def __init__(self):
        self._name = "Accel"
        self._device_name = "ACCEL."
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class InitialDownForce(PlotterParameter):

    def __init__(self):
        self._name = "Initial down force"
        self._device_name = "INITIAL DOWN FORCE"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class CutLinePattern(PlotterParameter):

    def __init__(self):
        self._name = "Cut line pattern"
        self._device_name = "CUT LINE PATTERN"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class LtypeUp(PlotterParameter):

    def __init__(self):
        self._name = "Ltype up"
        self._device_name = "LTYPE UP"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class LtypeDwn(PlotterParameter):

    def __init__(self):
        self._name = "Ltype dwn"
        self._device_name = "LTYPE DWN"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class UpMode(PlotterParameter):

    def __init__(self):
        self._name = "Up mode"
        self._device_name = "UP MODE"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class TangentialMode(PlotterParameter):

    def __init__(self):
        self._name = "Tangential mode"
        self._device_name = "TANGENTIAL MODE"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class OvercutSE(PlotterParameter):

    def __init__(self):
        self._name = "Overcut se"
        self._device_name = "OVERCUT S.E."
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class DAdj(PlotterParameter):

    def __init__(self):
        self._name = "D adj"
        self._device_name = "D. ADJ."
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class X(PlotterParameter):

    def __init__(self):
        self._name = "X"
        self._device_name = "X"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class Y(PlotterParameter):

    def __init__(self):
        self._name = "Y"
        self._device_name = "Y"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class Tool(PlotterParameter):

    def __init__(self):
        self._name = "Tool"
        self._device_name = "TOOL"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class Offset(PlotterParameter):

    def __init__(self):
        self._name = "Offset"
        self._device_name = "OFFSET"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class Speed(PlotterParameter):

    def __init__(self):
        self._name = "Speed"
        self._device_name = "SPEED"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class Force(PlotterParameter):

    def __init__(self):
        self._name = "Force"
        self._device_name = "FORCE"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class Accel(PlotterParameter):

    def __init__(self):
        self._name = "Accel"
        self._device_name = "ACCEL."
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class InitialDownForce(PlotterParameter):

    def __init__(self):
        self._name = "Initial down force"
        self._device_name = "INITIAL DOWN FORCE"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class CutLinePattern(PlotterParameter):

    def __init__(self):
        self._name = "Cut line pattern"
        self._device_name = "CUT LINE PATTERN"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class LtypeUp(PlotterParameter):

    def __init__(self):
        self._name = "Ltype up"
        self._device_name = "LTYPE UP"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class LtypeDwn(PlotterParameter):

    def __init__(self):
        self._name = "Ltype dwn"
        self._device_name = "LTYPE DWN"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class UpMode(PlotterParameter):

    def __init__(self):
        self._name = "Up mode"
        self._device_name = "UP MODE"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class TangentialMode(PlotterParameter):

    def __init__(self):
        self._name = "Tangential mode"
        self._device_name = "TANGENTIAL MODE"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class OvercutSE(PlotterParameter):

    def __init__(self):
        self._name = "Overcut se"
        self._device_name = "OVERCUT S.E."
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class DAdj(PlotterParameter):

    def __init__(self):
        self._name = "D adj"
        self._device_name = "D. ADJ."
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class X(PlotterParameter):

    def __init__(self):
        self._name = "X"
        self._device_name = "X"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class Y(PlotterParameter):

    def __init__(self):
        self._name = "Y"
        self._device_name = "Y"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class Tool(PlotterParameter):

    def __init__(self):
        self._name = "Tool"
        self._device_name = "TOOL"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class Offset(PlotterParameter):

    def __init__(self):
        self._name = "Offset"
        self._device_name = "OFFSET"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class Speed(PlotterParameter):

    def __init__(self):
        self._name = "Speed"
        self._device_name = "SPEED"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class Force(PlotterParameter):

    def __init__(self):
        self._name = "Force"
        self._device_name = "FORCE"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class Accel(PlotterParameter):

    def __init__(self):
        self._name = "Accel"
        self._device_name = "ACCEL."
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class InitialDownForce(PlotterParameter):

    def __init__(self):
        self._name = "Initial down force"
        self._device_name = "INITIAL DOWN FORCE"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class CutLinePattern(PlotterParameter):

    def __init__(self):
        self._name = "Cut line pattern"
        self._device_name = "CUT LINE PATTERN"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class LtypeUp(PlotterParameter):

    def __init__(self):
        self._name = "Ltype up"
        self._device_name = "LTYPE UP"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class LtypeDwn(PlotterParameter):

    def __init__(self):
        self._name = "Ltype dwn"
        self._device_name = "LTYPE DWN"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class UpMode(PlotterParameter):

    def __init__(self):
        self._name = "Up mode"
        self._device_name = "UP MODE"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class TangentialMode(PlotterParameter):

    def __init__(self):
        self._name = "Tangential mode"
        self._device_name = "TANGENTIAL MODE"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class OvercutSE(PlotterParameter):

    def __init__(self):
        self._name = "Overcut se"
        self._device_name = "OVERCUT S.E."
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class DAdj(PlotterParameter):

    def __init__(self):
        self._name = "D adj"
        self._device_name = "D. ADJ."
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class X(PlotterParameter):

    def __init__(self):
        self._name = "X"
        self._device_name = "X"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class Y(PlotterParameter):

    def __init__(self):
        self._name = "Y"
        self._device_name = "Y"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class Tool(PlotterParameter):

    def __init__(self):
        self._name = "Tool"
        self._device_name = "TOOL"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class Offset(PlotterParameter):

    def __init__(self):
        self._name = "Offset"
        self._device_name = "OFFSET"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class Speed(PlotterParameter):

    def __init__(self):
        self._name = "Speed"
        self._device_name = "SPEED"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class Force(PlotterParameter):

    def __init__(self):
        self._name = "Force"
        self._device_name = "FORCE"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class Accel(PlotterParameter):

    def __init__(self):
        self._name = "Accel"
        self._device_name = "ACCEL."
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class InitialDownForce(PlotterParameter):

    def __init__(self):
        self._name = "Initial down force"
        self._device_name = "INITIAL DOWN FORCE"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class CutLinePattern(PlotterParameter):

    def __init__(self):
        self._name = "Cut line pattern"
        self._device_name = "CUT LINE PATTERN"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class LtypeUp(PlotterParameter):

    def __init__(self):
        self._name = "Ltype up"
        self._device_name = "LTYPE UP"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class LtypeDwn(PlotterParameter):

    def __init__(self):
        self._name = "Ltype dwn"
        self._device_name = "LTYPE DWN"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class UpMode(PlotterParameter):

    def __init__(self):
        self._name = "Up mode"
        self._device_name = "UP MODE"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class TangentialMode(PlotterParameter):

    def __init__(self):
        self._name = "Tangential mode"
        self._device_name = "TANGENTIAL MODE"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class OvercutSE(PlotterParameter):

    def __init__(self):
        self._name = "Overcut se"
        self._device_name = "OVERCUT S.E."
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class DAdj(PlotterParameter):

    def __init__(self):
        self._name = "D adj"
        self._device_name = "D. ADJ."
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class X(PlotterParameter):

    def __init__(self):
        self._name = "X"
        self._device_name = "X"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class Y(PlotterParameter):

    def __init__(self):
        self._name = "Y"
        self._device_name = "Y"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class Tool(PlotterParameter):

    def __init__(self):
        self._name = "Tool"
        self._device_name = "TOOL"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class Offset(PlotterParameter):

    def __init__(self):
        self._name = "Offset"
        self._device_name = "OFFSET"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class Speed(PlotterParameter):

    def __init__(self):
        self._name = "Speed"
        self._device_name = "SPEED"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class Force(PlotterParameter):

    def __init__(self):
        self._name = "Force"
        self._device_name = "FORCE"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class Accel(PlotterParameter):

    def __init__(self):
        self._name = "Accel"
        self._device_name = "ACCEL."
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class InitialDownForce(PlotterParameter):

    def __init__(self):
        self._name = "Initial down force"
        self._device_name = "INITIAL DOWN FORCE"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class CutLinePattern(PlotterParameter):

    def __init__(self):
        self._name = "Cut line pattern"
        self._device_name = "CUT LINE PATTERN"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class LtypeUp(PlotterParameter):

    def __init__(self):
        self._name = "Ltype up"
        self._device_name = "LTYPE UP"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class LtypeDwn(PlotterParameter):

    def __init__(self):
        self._name = "Ltype dwn"
        self._device_name = "LTYPE DWN"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class UpMode(PlotterParameter):

    def __init__(self):
        self._name = "Up mode"
        self._device_name = "UP MODE"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class TangentialMode(PlotterParameter):

    def __init__(self):
        self._name = "Tangential mode"
        self._device_name = "TANGENTIAL MODE"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class OvercutSE(PlotterParameter):

    def __init__(self):
        self._name = "Overcut se"
        self._device_name = "OVERCUT S.E."
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class DAdj(PlotterParameter):

    def __init__(self):
        self._name = "D adj"
        self._device_name = "D. ADJ."
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class X(PlotterParameter):

    def __init__(self):
        self._name = "X"
        self._device_name = "X"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class Y(PlotterParameter):

    def __init__(self):
        self._name = "Y"
        self._device_name = "Y"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class Tool(PlotterParameter):

    def __init__(self):
        self._name = "Tool"
        self._device_name = "TOOL"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class Offset(PlotterParameter):

    def __init__(self):
        self._name = "Offset"
        self._device_name = "OFFSET"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class Speed(PlotterParameter):

    def __init__(self):
        self._name = "Speed"
        self._device_name = "SPEED"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class Force(PlotterParameter):

    def __init__(self):
        self._name = "Force"
        self._device_name = "FORCE"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class Accel(PlotterParameter):

    def __init__(self):
        self._name = "Accel"
        self._device_name = "ACCEL."
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class InitialDownForce(PlotterParameter):

    def __init__(self):
        self._name = "Initial down force"
        self._device_name = "INITIAL DOWN FORCE"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class CutLinePattern(PlotterParameter):

    def __init__(self):
        self._name = "Cut line pattern"
        self._device_name = "CUT LINE PATTERN"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class LtypeUp(PlotterParameter):

    def __init__(self):
        self._name = "Ltype up"
        self._device_name = "LTYPE UP"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class LtypeDwn(PlotterParameter):

    def __init__(self):
        self._name = "Ltype dwn"
        self._device_name = "LTYPE DWN"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class UpMode(PlotterParameter):

    def __init__(self):
        self._name = "Up mode"
        self._device_name = "UP MODE"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class TangentialMode(PlotterParameter):

    def __init__(self):
        self._name = "Tangential mode"
        self._device_name = "TANGENTIAL MODE"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class OvercutSE(PlotterParameter):

    def __init__(self):
        self._name = "Overcut se"
        self._device_name = "OVERCUT S.E."
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class DAdj(PlotterParameter):

    def __init__(self):
        self._name = "D adj"
        self._device_name = "D. ADJ."
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class X(PlotterParameter):

    def __init__(self):
        self._name = "X"
        self._device_name = "X"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class Y(PlotterParameter):

    def __init__(self):
        self._name = "Y"
        self._device_name = "Y"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class StepPass(PlotterParameter):

    def __init__(self):
        self._name = "Step pass"
        self._device_name = "STEP PASS"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class OffsetForce(PlotterParameter):

    def __init__(self):
        self._name = "Offset force"
        self._device_name = "OFFSET FORCE"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class OffsetAngle(PlotterParameter):

    def __init__(self):
        self._name = "Offset angle"
        self._device_name = "OFFSET ANGLE"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class DataSort(PlotterParameter):

    def __init__(self):
        self._name = "Data sort"
        self._device_name = "DATA SORT"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class ToolUpSpeed(PlotterParameter):

    def __init__(self):
        self._name = "Tool up speed"
        self._device_name = "TOOL UP SPEED"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class ConditionPriority(PlotterParameter):

    def __init__(self):
        self._name = "Condition priority"
        self._device_name = "CONDITION PRIORITY"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class InitialBlade(PlotterParameter):

    def __init__(self):
        self._name = "Initial blade"
        self._device_name = "INITIAL BLADE"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class ToolUpMove(PlotterParameter):

    def __init__(self):
        self._name = "Tool up move"
        self._device_name = "TOOL UP MOVE"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class MarkScanMode(PlotterParameter):

    def __init__(self):
        self._name = "Mark scan mode"
        self._device_name = "MARK SCAN MODE"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class NumberOfPoints(PlotterParameter):

    def __init__(self):
        self._name = "Number of points"
        self._device_name = "NUMBER OF POINTS"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class MarkDistanceXY(PlotterParameter):

    def __init__(self):
        self._name = "Mark distance x,y"
        self._device_name = "MARK DISTANCE x,y"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class SensingSpeed(PlotterParameter):

    def __init__(self):
        self._name = "Sensing speed"
        self._device_name = "SENSING SPEED"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class MarkType(PlotterParameter):

    def __init__(self):
        self._name = "Mark type"
        self._device_name = "MARK TYPE"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class DAdjMode(PlotterParameter):

    def __init__(self):
        self._name = "D adj mode"
        self._device_name = "D. ADJ. MODE"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class MarkDistAdjUnit(PlotterParameter):

    def __init__(self):
        self._name = "Mark distadjunit"
        self._device_name = "MARK DIST.ADJ.UNIT"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class MarkOffsetXY(PlotterParameter):

    def __init__(self):
        self._name = "Mark offset x,y"
        self._device_name = "MARK OFFSET x,y"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class MarkAutoScan(PlotterParameter):

    def __init__(self):
        self._name = "Mark auto scan"
        self._device_name = "MARK AUTO SCAN"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class PaperWeight(PlotterParameter):

    def __init__(self):
        self._name = "Paper-weight"
        self._device_name = "PAPER-WEIGHT"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class SensorOffsetAdj(PlotterParameter):

    def __init__(self):
        self._name = "Sensor offset adj"
        self._device_name = "SENSOR OFFSET ADJ."
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class MarkSize(PlotterParameter):

    def __init__(self):
        self._name = "Mark size"
        self._device_name = "MARK SIZE"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class SensorAdjust(PlotterParameter):

    def __init__(self):
        self._name = "Sensor adjust"
        self._device_name = "SENSOR ADJUST"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class SensingLevelXY(PlotterParameter):

    def __init__(self):
        self._name = "Sensing level(x,y)"
        self._device_name = "SENSING LEVEL(X,Y)"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class FactorySensorGain(PlotterParameter):

    def __init__(self):
        self._name = "Factory sensor gain"
        self._device_name = "FACTORY SENSOR GAIN"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class FactoryBaseLevel(PlotterParameter):

    def __init__(self):
        self._name = "Factory base level"
        self._device_name = "FACTORY BASE LEVEL"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class FactorySensingLevelXY(PlotterParameter):

    def __init__(self):
        self._name = "Factory sensing level(x,y)"
        self._device_name = "FACTORY SENSING LEVEL(X,Y)"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class UserSensorGain(PlotterParameter):

    def __init__(self):
        self._name = "User sensor gain"
        self._device_name = "USER SENSOR GAIN"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class UserBaseLevel(PlotterParameter):

    def __init__(self):
        self._name = "User base level"
        self._device_name = "USER BASE LEVEL"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class UserSensingLevelXY(PlotterParameter):

    def __init__(self):
        self._name = "User sensing level(x,y)"
        self._device_name = "USER SENSING LEVEL(X,Y)"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class RmSensorLevelAdjSelect(PlotterParameter):

    def __init__(self):
        self._name = "Rm sensor level adj select"
        self._device_name = "RM SENSOR LEVEL ADJ SELECT"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class Expand(PlotterParameter):

    def __init__(self):
        self._name = "Expand"
        self._device_name = "EXPAND"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class Rotate(PlotterParameter):

    def __init__(self):
        self._name = "Rotate"
        self._device_name = "ROTATE"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class Mirror(PlotterParameter):

    def __init__(self):
        self._name = "Mirror"
        self._device_name = "MIRROR"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class Scale(PlotterParameter):

    def __init__(self):
        self._name = "Scale"
        self._device_name = "SCALE"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class InitialFeed(PlotterParameter):

    def __init__(self):
        self._name = "Initial feed"
        self._device_name = "INITIAL FEED"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class FeedSpeed(PlotterParameter):

    def __init__(self):
        self._name = "Feed speed"
        self._device_name = "FEED SPEED"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class AutoPreFeed(PlotterParameter):

    def __init__(self):
        self._name = "Auto pre feed"
        self._device_name = "AUTO PRE FEED"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class AutoPreFeedLength(PlotterParameter):

    def __init__(self):
        self._name = "Auto pre feed length"
        self._device_name = "AUTO PRE FEED LENGTH"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class PageLength(PlotterParameter):

    def __init__(self):
        self._name = "Page length"
        self._device_name = "PAGE LENGTH"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class PreFeed(PlotterParameter):

    def __init__(self):
        self._name = "Pre feed"
        self._device_name = "PRE FEED"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class PanelCutting(PlotterParameter):

    def __init__(self):
        self._name = "Panel cutting"
        self._device_name = "PANEL CUTTING"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class DivideLength(PlotterParameter):

    def __init__(self):
        self._name = "Divide length"
        self._device_name = "DIVIDE LENGTH"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class BaudRate(PlotterParameter):

    def __init__(self):
        self._name = "Baud rate"
        self._device_name = "BAUD RATE"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class Parity(PlotterParameter):

    def __init__(self):
        self._name = "Parity"
        self._device_name = "PARITY"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class DataBit(PlotterParameter):

    def __init__(self):
        self._name = "Data bit"
        self._device_name = "DATA BIT"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class Handshake(PlotterParameter):

    def __init__(self):
        self._name = "Handshake"
        self._device_name = "HANDSHAKE"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class Command(PlotterParameter):

    def __init__(self):
        self._name = "Command"
        self._device_name = "COMMAND"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class GpGlStepSize(PlotterParameter):

    def __init__(self):
        self._name = "Gp-gl step size"
        self._device_name = "GP-GL STEP SIZE"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class HpGlOrigin(PlotterParameter):

    def __init__(self):
        self._name = "Hp-gl origin"
        self._device_name = "HP-GL ORIGIN"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class HpGlModelEmulated(PlotterParameter):

    def __init__(self):
        self._name = "Hp-gl model emulated"
        self._device_name = "HP-GL MODEL EMULATED"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class CircleResolution(PlotterParameter):

    def __init__(self):
        self._name = "Circle resolution"
        self._device_name = "CIRCLE RESOLUTION"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class CommandColSemiCol(PlotterParameter):

    def __init__(self):
        self._name = "Command ':',';'"
        self._device_name = "COMMAND ':',';'"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class CommandW(PlotterParameter):

    def __init__(self):
        self._name = "Command 'w'"
        self._device_name = "COMMAND 'W'"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class MoveStep(PlotterParameter):

    def __init__(self):
        self._name = "Move step"
        self._device_name = "MOVE STEP"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class LanguageSelection(PlotterParameter):

    def __init__(self):
        self._name = "Language selection"
        self._device_name = "LANGUAGE SELECTION"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class LengthUnit(PlotterParameter):

    def __init__(self):
        self._name = "Length unit"
        self._device_name = "LENGTH UNIT"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class MediaSensor(PlotterParameter):

    def __init__(self):
        self._name = "Media sensor"
        self._device_name = "MEDIA SENSOR"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class PushRollerSensor(PlotterParameter):

    def __init__(self):
        self._name = "Push roller sensor"
        self._device_name = "PUSH ROLLER SENSOR"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class FanPower(PlotterParameter):

    def __init__(self):
        self._name = "Fan power"
        self._device_name = "FAN POWER"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class BeepForKeyOpe(PlotterParameter):

    def __init__(self):
        self._name = "Beep for key ope"
        self._device_name = "BEEP FOR KEY OPE."
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class CopySpace(PlotterParameter):

    def __init__(self):
        self._name = "Copy space"
        self._device_name = "COPY SPACE"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""
