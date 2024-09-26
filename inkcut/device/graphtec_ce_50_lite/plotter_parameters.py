from atom.api import Instance, Str


def plotter_parameter_factory(parameter_name):
    parameter_name_to_class = {
        "TOOL": PlotterParameterTool,
        "OFFSET": PlotterParameterOffset,
        "SPEED": PlotterParameterSpeed,
        "FORCE": PlotterParameterForce,
        "ACCEL.": PlotterParameterAccel,
        "INITIAL DOWN FORCE": PlotterParameterInitialDownForce,
        "CUT LINE PATTERN": PlotterParameterCutLinePattern,
        "LTYPE UP": PlotterParameterLtypeUp,
        "LTYPE DWN": PlotterParameterLtypeDwn,
        "UP MODE": PlotterParameterUpMode,
        "TANGENTIAL MODE": PlotterParameterTangentialMode,
        "OVERCUT S.E.": PlotterParameterOvercutSE,
        "D. ADJ.": PlotterParameterDAdj,
        "X": PlotterParameterX,
        "Y": PlotterParameterY,
        "STEP PASS": PlotterParameterStepPass,
        "OFFSET FORCE": PlotterParameterOffsetForce,
        "OFFSET ANGLE": PlotterParameterOffsetAngle,
        "DATA SORT": PlotterParameterDataSort,
        "TOOL UP SPEED": PlotterParameterToolUpSpeed,
        "CONDITION PRIORITY": PlotterParameterConditionPriority,
        "INITIAL BLADE": PlotterParameterInitialBlade,
        "TOOL UP MOVE": PlotterParameterToolUpMove,
        "MARK SCAN MODE": PlotterParameterMarkScanMode,
        "NUMBER OF POINTS": PlotterParameterNumberOfPoints,
        "MARK DISTANCE x,y": PlotterParameterMarkDistanceXY,
        "SENSING SPEED": PlotterParameterSensingSpeed,
        "MARK TYPE": PlotterParameterMarkType,
        "D. ADJ. MODE": PlotterParameterDAdjMode,
        "MARK DIST.ADJ.UNIT": PlotterParameterMarkDistAdjUnit,
        "MARK OFFSET x,y": PlotterParameterMarkOffsetXY,
        "MARK AUTO SCAN": PlotterParameterMarkAutoScan,
        "PAPER-WEIGHT": PlotterParameterPaperWeight,
        "SENSOR OFFSET ADJ.": PlotterParameterSensorOffsetAdj,
        "MARK SIZE": PlotterParameterMarkSize,
        "SENSOR ADJUST": PlotterParameterSensorAdjust,
        "SENSING LEVEL(X,Y)": PlotterParameterSensingLevelXY,
        "FACTORY SENSOR GAIN": PlotterParameterFactorySensorGain,
        "FACTORY BASE LEVEL": PlotterParameterFactoryBaseLevel,
        "FACTORY SENSING LEVEL(X,Y)": PlotterParameterFactorySensingLevelXY,
        "USER SENSOR GAIN": PlotterParameterUserSensorGain,
        "USER BASE LEVEL": PlotterParameterUserBaseLevel,
        "USER SENSING LEVEL(X,Y)": PlotterParameterUserSensingLevelXY,
        "RM SENSOR LEVEL ADJ SELECT": PlotterParameterRmSensorLevelAdjSelect,
        "EXPAND": PlotterParameterExpand,
        "ROTATE": PlotterParameterRotate,
        "MIRROR": PlotterParameterMirror,
        "SCALE": PlotterParameterScale,
        "INITIAL FEED": PlotterParameterInitialFeed,
        "FEED SPEED": PlotterParameterFeedSpeed,
        "AUTO PRE FEED": PlotterParameterAutoPreFeed,
        "AUTO PRE FEED LENGTH": PlotterParameterAutoPreFeedLength,
        "PAGE LENGTH": PlotterParameterPageLength,
        "PRE FEED": PlotterParameterPreFeed,
        "PANEL CUTTING": PlotterParameterPanelCutting,
        "DIVIDE LENGTH": PlotterParameterDivideLength,
        "BAUD RATE": PlotterParameterBaudRate,
        "PARITY": PlotterParameterParity,
        "DATA BIT": PlotterParameterDataBit,
        "HANDSHAKE": PlotterParameterHandshake,
        "COMMAND": PlotterParameterCommand,
        "GP-GL STEP SIZE": PlotterParameterGpGlStepSize,
        "HP-GL ORIGIN": PlotterParameterHpGlOrigin,
        "HP-GL MODEL EMULATED": PlotterParameterHpGlModelEmulated,
        "CIRCLE RESOLUTION": PlotterParameterCircleResolution,
        "COMMAND ':',';'": PlotterParameterCommandColSemiCol,
        "COMMAND 'W'": PlotterParameterCommandW,
        "MOVE STEP": PlotterParameterMoveStep,
        "LANGUAGE SELECTION": PlotterParameterLanguageSelection,
        "LENGTH UNIT": PlotterParameterLengthUnit,
        "MEDIA SENSOR": PlotterParameterMediaSensor,
        "PUSH ROLLER SENSOR": PlotterParameterPushRollerSensor,
        "FAN POWER": PlotterParameterFanPower,
        "BEEP FOR KEY OPE.": PlotterParameterBeepForKeyOpe,
        "COPY SPACE": PlotterParameterCopySpace,
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


class PlotterParameterTool(PlotterParameter):

    def __init__(self):
        self._name = "Tool"
        self._device_name = "TOOL"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class PlotterParameterOffset(PlotterParameter):

    def __init__(self):
        self._name = "Offset"
        self._device_name = "OFFSET"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class PlotterParameterSpeed(PlotterParameter):

    def __init__(self):
        self._name = "Speed"
        self._device_name = "SPEED"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class PlotterParameterForce(PlotterParameter):

    def __init__(self):
        self._name = "Force"
        self._device_name = "FORCE"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class PlotterParameterAccel(PlotterParameter):

    def __init__(self):
        self._name = "Accel"
        self._device_name = "ACCEL."
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class PlotterParameterInitialDownForce(PlotterParameter):

    def __init__(self):
        self._name = "Initial down force"
        self._device_name = "INITIAL DOWN FORCE"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class PlotterParameterCutLinePattern(PlotterParameter):

    def __init__(self):
        self._name = "Cut line pattern"
        self._device_name = "CUT LINE PATTERN"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class PlotterParameterLtypeUp(PlotterParameter):

    def __init__(self):
        self._name = "Ltype up"
        self._device_name = "LTYPE UP"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class PlotterParameterLtypeDwn(PlotterParameter):

    def __init__(self):
        self._name = "Ltype dwn"
        self._device_name = "LTYPE DWN"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class PlotterParameterUpMode(PlotterParameter):

    def __init__(self):
        self._name = "Up mode"
        self._device_name = "UP MODE"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class PlotterParameterTangentialMode(PlotterParameter):

    def __init__(self):
        self._name = "Tangential mode"
        self._device_name = "TANGENTIAL MODE"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class PlotterParameterOvercutSE(PlotterParameter):

    def __init__(self):
        self._name = "Overcut se"
        self._device_name = "OVERCUT S.E."
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class PlotterParameterDAdj(PlotterParameter):

    def __init__(self):
        self._name = "D adj"
        self._device_name = "D. ADJ."
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class PlotterParameterX(PlotterParameter):

    def __init__(self):
        self._name = "X"
        self._device_name = "X"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class PlotterParameterY(PlotterParameter):

    def __init__(self):
        self._name = "Y"
        self._device_name = "Y"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class PlotterParameterStepPass(PlotterParameter):

    def __init__(self):
        self._name = "Step pass"
        self._device_name = "STEP PASS"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class PlotterParameterOffsetForce(PlotterParameter):

    def __init__(self):
        self._name = "Offset force"
        self._device_name = "OFFSET FORCE"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class PlotterParameterOffsetAngle(PlotterParameter):

    def __init__(self):
        self._name = "Offset angle"
        self._device_name = "OFFSET ANGLE"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class PlotterParameterDataSort(PlotterParameter):

    def __init__(self):
        self._name = "Data sort"
        self._device_name = "DATA SORT"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class PlotterParameterToolUpSpeed(PlotterParameter):

    def __init__(self):
        self._name = "Tool up speed"
        self._device_name = "TOOL UP SPEED"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class PlotterParameterConditionPriority(PlotterParameter):

    def __init__(self):
        self._name = "Condition priority"
        self._device_name = "CONDITION PRIORITY"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class PlotterParameterInitialBlade(PlotterParameter):

    def __init__(self):
        self._name = "Initial blade"
        self._device_name = "INITIAL BLADE"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class PlotterParameterToolUpMove(PlotterParameter):

    def __init__(self):
        self._name = "Tool up move"
        self._device_name = "TOOL UP MOVE"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class PlotterParameterMarkScanMode(PlotterParameter):

    def __init__(self):
        self._name = "Mark scan mode"
        self._device_name = "MARK SCAN MODE"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class PlotterParameterNumberOfPoints(PlotterParameter):

    def __init__(self):
        self._name = "Number of points"
        self._device_name = "NUMBER OF POINTS"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class PlotterParameterMarkDistanceXY(PlotterParameter):

    def __init__(self):
        self._name = "Mark distance x,y"
        self._device_name = "MARK DISTANCE x,y"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class PlotterParameterSensingSpeed(PlotterParameter):

    def __init__(self):
        self._name = "Sensing speed"
        self._device_name = "SENSING SPEED"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class PlotterParameterMarkType(PlotterParameter):

    def __init__(self):
        self._name = "Mark type"
        self._device_name = "MARK TYPE"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class PlotterParameterDAdjMode(PlotterParameter):

    def __init__(self):
        self._name = "D adj mode"
        self._device_name = "D. ADJ. MODE"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class PlotterParameterMarkDistAdjUnit(PlotterParameter):

    def __init__(self):
        self._name = "Mark distadjunit"
        self._device_name = "MARK DIST.ADJ.UNIT"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class PlotterParameterMarkOffsetXY(PlotterParameter):

    def __init__(self):
        self._name = "Mark offset x,y"
        self._device_name = "MARK OFFSET x,y"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class PlotterParameterMarkAutoScan(PlotterParameter):

    def __init__(self):
        self._name = "Mark auto scan"
        self._device_name = "MARK AUTO SCAN"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class PlotterParameterPaperWeight(PlotterParameter):

    def __init__(self):
        self._name = "Paper-weight"
        self._device_name = "PAPER-WEIGHT"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class PlotterParameterSensorOffsetAdj(PlotterParameter):

    def __init__(self):
        self._name = "Sensor offset adj"
        self._device_name = "SENSOR OFFSET ADJ."
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class PlotterParameterMarkSize(PlotterParameter):

    def __init__(self):
        self._name = "Mark size"
        self._device_name = "MARK SIZE"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class PlotterParameterSensorAdjust(PlotterParameter):

    def __init__(self):
        self._name = "Sensor adjust"
        self._device_name = "SENSOR ADJUST"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class PlotterParameterSensingLevelXY(PlotterParameter):

    def __init__(self):
        self._name = "Sensing level(x,y)"
        self._device_name = "SENSING LEVEL(X,Y)"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class PlotterParameterFactorySensorGain(PlotterParameter):

    def __init__(self):
        self._name = "Factory sensor gain"
        self._device_name = "FACTORY SENSOR GAIN"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class PlotterParameterFactoryBaseLevel(PlotterParameter):

    def __init__(self):
        self._name = "Factory base level"
        self._device_name = "FACTORY BASE LEVEL"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class PlotterParameterFactorySensingLevelXY(PlotterParameter):

    def __init__(self):
        self._name = "Factory sensing level(x,y)"
        self._device_name = "FACTORY SENSING LEVEL(X,Y)"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class PlotterParameterUserSensorGain(PlotterParameter):

    def __init__(self):
        self._name = "User sensor gain"
        self._device_name = "USER SENSOR GAIN"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class PlotterParameterUserBaseLevel(PlotterParameter):

    def __init__(self):
        self._name = "User base level"
        self._device_name = "USER BASE LEVEL"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class PlotterParameterUserSensingLevelXY(PlotterParameter):

    def __init__(self):
        self._name = "User sensing level(x,y)"
        self._device_name = "USER SENSING LEVEL(X,Y)"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class PlotterParameterRmSensorLevelAdjSelect(PlotterParameter):

    def __init__(self):
        self._name = "Rm sensor level adj select"
        self._device_name = "RM SENSOR LEVEL ADJ SELECT"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class PlotterParameterExpand(PlotterParameter):

    def __init__(self):
        self._name = "Expand"
        self._device_name = "EXPAND"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class PlotterParameterRotate(PlotterParameter):

    def __init__(self):
        self._name = "Rotate"
        self._device_name = "ROTATE"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class PlotterParameterMirror(PlotterParameter):

    def __init__(self):
        self._name = "Mirror"
        self._device_name = "MIRROR"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class PlotterParameterScale(PlotterParameter):

    def __init__(self):
        self._name = "Scale"
        self._device_name = "SCALE"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class PlotterParameterInitialFeed(PlotterParameter):

    def __init__(self):
        self._name = "Initial feed"
        self._device_name = "INITIAL FEED"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class PlotterParameterFeedSpeed(PlotterParameter):

    def __init__(self):
        self._name = "Feed speed"
        self._device_name = "FEED SPEED"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class PlotterParameterAutoPreFeed(PlotterParameter):

    def __init__(self):
        self._name = "Auto pre feed"
        self._device_name = "AUTO PRE FEED"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class PlotterParameterAutoPreFeedLength(PlotterParameter):

    def __init__(self):
        self._name = "Auto pre feed length"
        self._device_name = "AUTO PRE FEED LENGTH"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class PlotterParameterPageLength(PlotterParameter):

    def __init__(self):
        self._name = "Page length"
        self._device_name = "PAGE LENGTH"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class PlotterParameterPreFeed(PlotterParameter):

    def __init__(self):
        self._name = "Pre feed"
        self._device_name = "PRE FEED"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class PlotterParameterPanelCutting(PlotterParameter):

    def __init__(self):
        self._name = "Panel cutting"
        self._device_name = "PANEL CUTTING"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class PlotterParameterDivideLength(PlotterParameter):

    def __init__(self):
        self._name = "Divide length"
        self._device_name = "DIVIDE LENGTH"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class PlotterParameterBaudRate(PlotterParameter):

    def __init__(self):
        self._name = "Baud rate"
        self._device_name = "BAUD RATE"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class PlotterParameterParity(PlotterParameter):

    def __init__(self):
        self._name = "Parity"
        self._device_name = "PARITY"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class PlotterParameterDataBit(PlotterParameter):

    def __init__(self):
        self._name = "Data bit"
        self._device_name = "DATA BIT"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class PlotterParameterHandshake(PlotterParameter):

    def __init__(self):
        self._name = "Handshake"
        self._device_name = "HANDSHAKE"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class PlotterParameterCommand(PlotterParameter):

    def __init__(self):
        self._name = "Command"
        self._device_name = "COMMAND"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class PlotterParameterGpGlStepSize(PlotterParameter):

    def __init__(self):
        self._name = "Gp-gl step size"
        self._device_name = "GP-GL STEP SIZE"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class PlotterParameterHpGlOrigin(PlotterParameter):

    def __init__(self):
        self._name = "Hp-gl origin"
        self._device_name = "HP-GL ORIGIN"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class PlotterParameterHpGlModelEmulated(PlotterParameter):

    def __init__(self):
        self._name = "Hp-gl model emulated"
        self._device_name = "HP-GL MODEL EMULATED"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class PlotterParameterCircleResolution(PlotterParameter):

    def __init__(self):
        self._name = "Circle resolution"
        self._device_name = "CIRCLE RESOLUTION"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class PlotterParameterCommandColSemiCol(PlotterParameter):

    def __init__(self):
        self._name = "Command ':',';'"
        self._device_name = "COMMAND ':',';'"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class PlotterParameterCommandW(PlotterParameter):

    def __init__(self):
        self._name = "Command 'w'"
        self._device_name = "COMMAND 'W'"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class PlotterParameterMoveStep(PlotterParameter):

    def __init__(self):
        self._name = "Move step"
        self._device_name = "MOVE STEP"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class PlotterParameterLanguageSelection(PlotterParameter):

    def __init__(self):
        self._name = "Language selection"
        self._device_name = "LANGUAGE SELECTION"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class PlotterParameterLengthUnit(PlotterParameter):

    def __init__(self):
        self._name = "Length unit"
        self._device_name = "LENGTH UNIT"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class PlotterParameterMediaSensor(PlotterParameter):

    def __init__(self):
        self._name = "Media sensor"
        self._device_name = "MEDIA SENSOR"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class PlotterParameterPushRollerSensor(PlotterParameter):

    def __init__(self):
        self._name = "Push roller sensor"
        self._device_name = "PUSH ROLLER SENSOR"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class PlotterParameterFanPower(PlotterParameter):

    def __init__(self):
        self._name = "Fan power"
        self._device_name = "FAN POWER"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class PlotterParameterBeepForKeyOpe(PlotterParameter):

    def __init__(self):
        self._name = "Beep for key ope"
        self._device_name = "BEEP FOR KEY OPE."
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""


# ----------------------------------------------------------------------------------------------------


class PlotterParameterCopySpace(PlotterParameter):

    def __init__(self):
        self._name = "Copy space"
        self._device_name = "COPY SPACE"
        self._value = None
        self._is_readonly = True

    # ------------------------------------------------------------------------------------------------

    def get_update_command(self):
        return ""
