import pytest

# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import PlotterParameterTool


class TestPlotterParameterTool:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("PM-BS-001", "PM-BS-001")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = PlotterParameterTool()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("PM-BS-001", "PM-BS-001")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = PlotterParameterTool()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import PlotterParameterOffset


class TestPlotterParameterOffset:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0", "0")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = PlotterParameterOffset()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0", "0")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = PlotterParameterOffset()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import PlotterParameterSpeed


class TestPlotterParameterSpeed:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("1", "1")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = PlotterParameterSpeed()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("1", "1")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = PlotterParameterSpeed()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import PlotterParameterForce


class TestPlotterParameterForce:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("11", "11")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = PlotterParameterForce()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("11", "11")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = PlotterParameterForce()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import PlotterParameterAccel


class TestPlotterParameterAccel:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("1", "1")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = PlotterParameterAccel()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("1", "1")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = PlotterParameterAccel()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import PlotterParameterInitialDownForce


class TestPlotterParameterInitialDownForce:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("15", "15")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = PlotterParameterInitialDownForce()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("15", "15")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = PlotterParameterInitialDownForce()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import PlotterParameterCutLinePattern


class TestPlotterParameterCutLinePattern:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = PlotterParameterCutLinePattern()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = PlotterParameterCutLinePattern()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import PlotterParameterLtypeUp


class TestPlotterParameterLtypeUp:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.6mm", "0.6mm")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = PlotterParameterLtypeUp()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.6mm", "0.6mm")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = PlotterParameterLtypeUp()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import PlotterParameterLtypeDwn


class TestPlotterParameterLtypeDwn:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("8.0mm", "8.0mm")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = PlotterParameterLtypeDwn()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("8.0mm", "8.0mm")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = PlotterParameterLtypeDwn()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import PlotterParameterUpMode


class TestPlotterParameterUpMode:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("UP", "UP")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = PlotterParameterUpMode()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("UP", "UP")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = PlotterParameterUpMode()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import PlotterParameterTangentialMode


class TestPlotterParameterTangentialMode:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("1", "1")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = PlotterParameterTangentialMode()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("1", "1")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = PlotterParameterTangentialMode()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import PlotterParameterOvercutSE


class TestPlotterParameterOvercutSE:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.0mm,0.0mm", "0.0mm,0.0mm")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = PlotterParameterOvercutSE()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.0mm,0.0mm", "0.0mm,0.0mm")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = PlotterParameterOvercutSE()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import PlotterParameterDAdj


class TestPlotterParameterDAdj:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = PlotterParameterDAdj()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = PlotterParameterDAdj()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import PlotterParameterX


class TestPlotterParameterX:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.00", "0.00")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = PlotterParameterX()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.00", "0.00")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = PlotterParameterX()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import PlotterParameterY


class TestPlotterParameterY:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.00", "0.00")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = PlotterParameterY()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.00", "0.00")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = PlotterParameterY()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import PlotterParameterStepPass


class TestPlotterParameterStepPass:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("1", "1")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = PlotterParameterStepPass()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("1", "1")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = PlotterParameterStepPass()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import PlotterParameterOffsetForce


class TestPlotterParameterOffsetForce:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("10", "10")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = PlotterParameterOffsetForce()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("10", "10")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = PlotterParameterOffsetForce()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import PlotterParameterOffsetAngle


class TestPlotterParameterOffsetAngle:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("30", "30")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = PlotterParameterOffsetAngle()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("30", "30")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = PlotterParameterOffsetAngle()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import PlotterParameterDataSort


class TestPlotterParameterDataSort:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = PlotterParameterDataSort()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = PlotterParameterDataSort()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import PlotterParameterToolUpSpeed


class TestPlotterParameterToolUpSpeed:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("AUTO", "AUTO")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = PlotterParameterToolUpSpeed()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("AUTO", "AUTO")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = PlotterParameterToolUpSpeed()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import PlotterParameterConditionPriority


class TestPlotterParameterConditionPriority:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("PROGRAM", "PROGRAM")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = PlotterParameterConditionPriority()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("PROGRAM", "PROGRAM")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = PlotterParameterConditionPriority()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import PlotterParameterInitialBlade


class TestPlotterParameterInitialBlade:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("2mm BELOW", "2mm BELOW")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = PlotterParameterInitialBlade()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("2mm BELOW", "2mm BELOW")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = PlotterParameterInitialBlade()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import PlotterParameterToolUpMove


class TestPlotterParameterToolUpMove:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("ENABLED", "ENABLED")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = PlotterParameterToolUpMove()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("ENABLED", "ENABLED")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = PlotterParameterToolUpMove()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import PlotterParameterMarkScanMode


class TestPlotterParameterMarkScanMode:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = PlotterParameterMarkScanMode()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = PlotterParameterMarkScanMode()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import PlotterParameterNumberOfPoints


class TestPlotterParameterNumberOfPoints:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("2POINTS", "2POINTS")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = PlotterParameterNumberOfPoints()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("2POINTS", "2POINTS")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = PlotterParameterNumberOfPoints()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import PlotterParameterMarkDistanceXY


class TestPlotterParameterMarkDistanceXY:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.0mm,   0.0mm", "0.0mm,   0.0mm")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = PlotterParameterMarkDistanceXY()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.0mm,   0.0mm", "0.0mm,   0.0mm")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = PlotterParameterMarkDistanceXY()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import PlotterParameterSensingSpeed


class TestPlotterParameterSensingSpeed:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("NORMAL", "NORMAL")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = PlotterParameterSensingSpeed()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("NORMAL", "NORMAL")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = PlotterParameterSensingSpeed()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import PlotterParameterMarkType


class TestPlotterParameterMarkType:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("2", "2")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = PlotterParameterMarkType()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("2", "2")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = PlotterParameterMarkType()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import PlotterParameterDAdjMode


class TestPlotterParameterDAdjMode:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("USER", "USER")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = PlotterParameterDAdjMode()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("USER", "USER")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = PlotterParameterDAdjMode()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import PlotterParameterMarkDistAdjUnit


class TestPlotterParameterMarkDistAdjUnit:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("5mm", "5mm")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = PlotterParameterMarkDistAdjUnit()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("5mm", "5mm")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = PlotterParameterMarkDistAdjUnit()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import PlotterParameterMarkOffsetXY


class TestPlotterParameterMarkOffsetXY:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.0mm,  0.0mm", "0.0mm,  0.0mm")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = PlotterParameterMarkOffsetXY()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.0mm,  0.0mm", "0.0mm,  0.0mm")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = PlotterParameterMarkOffsetXY()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import PlotterParameterMarkAutoScan


class TestPlotterParameterMarkAutoScan:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("ON", "ON")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = PlotterParameterMarkAutoScan()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("ON", "ON")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = PlotterParameterMarkAutoScan()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import PlotterParameterPaperWeight


class TestPlotterParameterPaperWeight:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("ON", "ON")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = PlotterParameterPaperWeight()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("ON", "ON")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = PlotterParameterPaperWeight()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import PlotterParameterSensorOffsetAdj


class TestPlotterParameterSensorOffsetAdj:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.0mm,0.0mm", "0.0mm,0.0mm")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = PlotterParameterSensorOffsetAdj()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.0mm,0.0mm", "0.0mm,0.0mm")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = PlotterParameterSensorOffsetAdj()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import PlotterParameterMarkSize


class TestPlotterParameterMarkSize:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("20.0", "20.0")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = PlotterParameterMarkSize()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("20.0", "20.0")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = PlotterParameterMarkSize()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import PlotterParameterSensorAdjust


class TestPlotterParameterSensorAdjust:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = PlotterParameterSensorAdjust()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = PlotterParameterSensorAdjust()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import PlotterParameterSensingLevelXY


class TestPlotterParameterSensingLevelXY:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("70,80", "70,80")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = PlotterParameterSensingLevelXY()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("70,80", "70,80")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = PlotterParameterSensingLevelXY()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import PlotterParameterFactorySensorGain


class TestPlotterParameterFactorySensorGain:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0", "0")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = PlotterParameterFactorySensorGain()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0", "0")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = PlotterParameterFactorySensorGain()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import PlotterParameterFactoryBaseLevel


class TestPlotterParameterFactoryBaseLevel:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0", "0")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = PlotterParameterFactoryBaseLevel()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0", "0")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = PlotterParameterFactoryBaseLevel()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import (
    PlotterParameterFactorySensingLevelXY,
)


class TestPlotterParameterFactorySensingLevelXY:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0,0", "0,0")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = PlotterParameterFactorySensingLevelXY()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0,0", "0,0")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = PlotterParameterFactorySensingLevelXY()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import PlotterParameterUserSensorGain


class TestPlotterParameterUserSensorGain:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0", "0")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = PlotterParameterUserSensorGain()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0", "0")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = PlotterParameterUserSensorGain()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import PlotterParameterUserBaseLevel


class TestPlotterParameterUserBaseLevel:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0", "0")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = PlotterParameterUserBaseLevel()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0", "0")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = PlotterParameterUserBaseLevel()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import PlotterParameterUserSensingLevelXY


class TestPlotterParameterUserSensingLevelXY:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0,0", "0,0")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = PlotterParameterUserSensingLevelXY()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0,0", "0,0")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = PlotterParameterUserSensingLevelXY()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import (
    PlotterParameterRmSensorLevelAdjSelect,
)


class TestPlotterParameterRmSensorLevelAdjSelect:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("USER", "USER")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = PlotterParameterRmSensorLevelAdjSelect()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("USER", "USER")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = PlotterParameterRmSensorLevelAdjSelect()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import PlotterParameterExpand


class TestPlotterParameterExpand:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("10.0mm", "10.0mm")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = PlotterParameterExpand()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("10.0mm", "10.0mm")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = PlotterParameterExpand()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import PlotterParameterRotate


class TestPlotterParameterRotate:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = PlotterParameterRotate()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = PlotterParameterRotate()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import PlotterParameterMirror


class TestPlotterParameterMirror:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = PlotterParameterMirror()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = PlotterParameterMirror()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import PlotterParameterScale


class TestPlotterParameterScale:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("1", "1")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = PlotterParameterScale()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("1", "1")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = PlotterParameterScale()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import PlotterParameterInitialFeed


class TestPlotterParameterInitialFeed:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = PlotterParameterInitialFeed()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = PlotterParameterInitialFeed()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import PlotterParameterFeedSpeed


class TestPlotterParameterFeedSpeed:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("NORMAL", "NORMAL")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = PlotterParameterFeedSpeed()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("NORMAL", "NORMAL")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = PlotterParameterFeedSpeed()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import PlotterParameterAutoPreFeed


class TestPlotterParameterAutoPreFeed:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = PlotterParameterAutoPreFeed()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = PlotterParameterAutoPreFeed()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import PlotterParameterAutoPreFeedLength


class TestPlotterParameterAutoPreFeedLength:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("300.0mm", "300.0mm")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = PlotterParameterAutoPreFeedLength()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("300.0mm", "300.0mm")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = PlotterParameterAutoPreFeedLength()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import PlotterParameterPageLength


class TestPlotterParameterPageLength:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("500.0mm", "500.0mm")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = PlotterParameterPageLength()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("500.0mm", "500.0mm")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = PlotterParameterPageLength()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import PlotterParameterPreFeed


class TestPlotterParameterPreFeed:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("300.0mm", "300.0mm")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = PlotterParameterPreFeed()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("300.0mm", "300.0mm")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = PlotterParameterPreFeed()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import PlotterParameterPanelCutting


class TestPlotterParameterPanelCutting:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = PlotterParameterPanelCutting()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = PlotterParameterPanelCutting()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import PlotterParameterDivideLength


class TestPlotterParameterDivideLength:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("100.0cm", "100.0cm")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = PlotterParameterDivideLength()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("100.0cm", "100.0cm")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = PlotterParameterDivideLength()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import PlotterParameterBaudRate


class TestPlotterParameterBaudRate:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0", "0")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = PlotterParameterBaudRate()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0", "0")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = PlotterParameterBaudRate()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import PlotterParameterParity


class TestPlotterParameterParity:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("NONE", "NONE")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = PlotterParameterParity()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("NONE", "NONE")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = PlotterParameterParity()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import PlotterParameterDataBit


class TestPlotterParameterDataBit:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("8 BIT", "8 BIT")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = PlotterParameterDataBit()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("8 BIT", "8 BIT")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = PlotterParameterDataBit()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import PlotterParameterHandshake


class TestPlotterParameterHandshake:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("HARDWIRE", "HARDWIRE")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = PlotterParameterHandshake()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("HARDWIRE", "HARDWIRE")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = PlotterParameterHandshake()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import PlotterParameterCommand


class TestPlotterParameterCommand:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("HP-GL", "HP-GL")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = PlotterParameterCommand()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("HP-GL", "HP-GL")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = PlotterParameterCommand()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import PlotterParameterGpGlStepSize


class TestPlotterParameterGpGlStepSize:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.100mm", "0.100mm")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = PlotterParameterGpGlStepSize()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.100mm", "0.100mm")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = PlotterParameterGpGlStepSize()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import PlotterParameterHpGlOrigin


class TestPlotterParameterHpGlOrigin:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("LOWER LEFT", "LOWER LEFT")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = PlotterParameterHpGlOrigin()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("LOWER LEFT", "LOWER LEFT")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = PlotterParameterHpGlOrigin()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import PlotterParameterHpGlModelEmulated


class TestPlotterParameterHpGlModelEmulated:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("7586", "7586")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = PlotterParameterHpGlModelEmulated()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("7586", "7586")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = PlotterParameterHpGlModelEmulated()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import PlotterParameterCircleResolution


class TestPlotterParameterCircleResolution:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("DEFAULT", "DEFAULT")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = PlotterParameterCircleResolution()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("DEFAULT", "DEFAULT")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = PlotterParameterCircleResolution()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import PlotterParameterCommandColSemiCol


class TestPlotterParameterCommandColSemiCol:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("ENABLED", "ENABLED")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = PlotterParameterCommandColSemiCol()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("ENABLED", "ENABLED")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = PlotterParameterCommandColSemiCol()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import PlotterParameterCommandW


class TestPlotterParameterCommandW:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("TOOL UP", "TOOL UP")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = PlotterParameterCommandW()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("TOOL UP", "TOOL UP")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = PlotterParameterCommandW()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import PlotterParameterMoveStep


class TestPlotterParameterMoveStep:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.1mm", "0.1mm")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = PlotterParameterMoveStep()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.1mm", "0.1mm")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = PlotterParameterMoveStep()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import PlotterParameterLanguageSelection


class TestPlotterParameterLanguageSelection:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("English", "English")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = PlotterParameterLanguageSelection()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("English", "English")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = PlotterParameterLanguageSelection()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import PlotterParameterLengthUnit


class TestPlotterParameterLengthUnit:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("METRIC", "METRIC")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = PlotterParameterLengthUnit()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("METRIC", "METRIC")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = PlotterParameterLengthUnit()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import PlotterParameterMediaSensor


class TestPlotterParameterMediaSensor:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("ENABLED", "ENABLED")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = PlotterParameterMediaSensor()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("ENABLED", "ENABLED")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = PlotterParameterMediaSensor()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import PlotterParameterPushRollerSensor


class TestPlotterParameterPushRollerSensor:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("DISABLED", "DISABLED")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = PlotterParameterPushRollerSensor()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("DISABLED", "DISABLED")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = PlotterParameterPushRollerSensor()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import PlotterParameterFanPower


class TestPlotterParameterFanPower:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("WEAK", "WEAK")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = PlotterParameterFanPower()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("WEAK", "WEAK")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = PlotterParameterFanPower()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import PlotterParameterBeepForKeyOpe


class TestPlotterParameterBeepForKeyOpe:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = PlotterParameterBeepForKeyOpe()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = PlotterParameterBeepForKeyOpe()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import PlotterParameterCopySpace


class TestPlotterParameterCopySpace:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("1.00mm", "1.00mm")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = PlotterParameterCopySpace()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("1.00mm", "1.00mm")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = PlotterParameterCopySpace()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value
