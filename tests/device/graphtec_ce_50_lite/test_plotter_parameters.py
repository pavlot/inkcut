import pytest

# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import Tool


class TestTool:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("PM-BS-001", "PM-BS-001")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = Tool()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("PM-BS-001", "PM-BS-001")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = Tool()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import Offset


class TestOffset:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0", "0")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = Offset()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0", "0")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = Offset()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import Speed


class TestSpeed:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("1", "1")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = Speed()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("1", "1")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = Speed()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import Force


class TestForce:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("11", "11")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = Force()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("11", "11")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = Force()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import Accel


class TestAccel:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("1", "1")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = Accel()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("1", "1")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = Accel()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import InitialDownForce


class TestInitialDownForce:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("15", "15")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = InitialDownForce()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("15", "15")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = InitialDownForce()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import CutLinePattern


class TestCutLinePattern:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = CutLinePattern()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = CutLinePattern()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import LtypeUp


class TestLtypeUp:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.6mm", "0.6mm")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = LtypeUp()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.6mm", "0.6mm")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = LtypeUp()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import LtypeDwn


class TestLtypeDwn:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("8.0mm", "8.0mm")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = LtypeDwn()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("8.0mm", "8.0mm")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = LtypeDwn()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import UpMode


class TestUpMode:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("UP", "UP")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = UpMode()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("UP", "UP")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = UpMode()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import TangentialMode


class TestTangentialMode:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("1", "1")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = TangentialMode()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("1", "1")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = TangentialMode()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import OvercutSE


class TestOvercutSE:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.0mm,0.0mm", "0.0mm,0.0mm")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = OvercutSE()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.0mm,0.0mm", "0.0mm,0.0mm")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = OvercutSE()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import DAdj


class TestDAdj:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = DAdj()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = DAdj()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import X


class TestX:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.00", "0.00")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = X()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.00", "0.00")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = X()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import Y


class TestY:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.00", "0.00")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = Y()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.00", "0.00")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = Y()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import Tool


class TestTool:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("PEN", "PEN")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = Tool()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("PEN", "PEN")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = Tool()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import Offset


class TestOffset:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0", "0")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = Offset()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0", "0")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = Offset()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import Speed


class TestSpeed:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("10", "10")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = Speed()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("10", "10")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = Speed()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import Force


class TestForce:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("12", "12")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = Force()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("12", "12")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = Force()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import Accel


class TestAccel:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("2", "2")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = Accel()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("2", "2")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = Accel()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import InitialDownForce


class TestInitialDownForce:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("15", "15")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = InitialDownForce()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("15", "15")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = InitialDownForce()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import CutLinePattern


class TestCutLinePattern:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = CutLinePattern()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = CutLinePattern()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import LtypeUp


class TestLtypeUp:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.6mm", "0.6mm")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = LtypeUp()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.6mm", "0.6mm")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = LtypeUp()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import LtypeDwn


class TestLtypeDwn:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("8.0mm", "8.0mm")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = LtypeDwn()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("8.0mm", "8.0mm")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = LtypeDwn()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import UpMode


class TestUpMode:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("UP", "UP")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = UpMode()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("UP", "UP")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = UpMode()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import TangentialMode


class TestTangentialMode:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = TangentialMode()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = TangentialMode()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import OvercutSE


class TestOvercutSE:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.0mm,0.0mm", "0.0mm,0.0mm")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = OvercutSE()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.0mm,0.0mm", "0.0mm,0.0mm")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = OvercutSE()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import DAdj


class TestDAdj:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = DAdj()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = DAdj()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import X


class TestX:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.00", "0.00")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = X()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.00", "0.00")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = X()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import Y


class TestY:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.00", "0.00")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = Y()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.00", "0.00")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = Y()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import Tool


class TestTool:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("PM-BS-001", "PM-BS-001")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = Tool()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("PM-BS-001", "PM-BS-001")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = Tool()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import Offset


class TestOffset:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0", "0")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = Offset()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0", "0")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = Offset()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import Speed


class TestSpeed:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("30", "30")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = Speed()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("30", "30")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = Speed()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import Force


class TestForce:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("12", "12")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = Force()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("12", "12")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = Force()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import Accel


class TestAccel:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("2", "2")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = Accel()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("2", "2")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = Accel()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import InitialDownForce


class TestInitialDownForce:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("15", "15")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = InitialDownForce()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("15", "15")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = InitialDownForce()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import CutLinePattern


class TestCutLinePattern:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = CutLinePattern()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = CutLinePattern()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import LtypeUp


class TestLtypeUp:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.6mm", "0.6mm")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = LtypeUp()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.6mm", "0.6mm")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = LtypeUp()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import LtypeDwn


class TestLtypeDwn:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("8.0mm", "8.0mm")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = LtypeDwn()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("8.0mm", "8.0mm")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = LtypeDwn()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import UpMode


class TestUpMode:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("UP", "UP")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = UpMode()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("UP", "UP")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = UpMode()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import TangentialMode


class TestTangentialMode:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = TangentialMode()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = TangentialMode()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import OvercutSE


class TestOvercutSE:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.0mm,0.0mm", "0.0mm,0.0mm")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = OvercutSE()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.0mm,0.0mm", "0.0mm,0.0mm")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = OvercutSE()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import DAdj


class TestDAdj:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = DAdj()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = DAdj()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import X


class TestX:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.00", "0.00")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = X()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.00", "0.00")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = X()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import Y


class TestY:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.00", "0.00")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = Y()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.00", "0.00")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = Y()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import Tool


class TestTool:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("PM-BS-001", "PM-BS-001")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = Tool()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("PM-BS-001", "PM-BS-001")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = Tool()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import Offset


class TestOffset:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0", "0")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = Offset()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0", "0")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = Offset()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import Speed


class TestSpeed:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("20", "20")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = Speed()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("20", "20")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = Speed()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import Force


class TestForce:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("17", "17")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = Force()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("17", "17")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = Force()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import Accel


class TestAccel:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("1", "1")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = Accel()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("1", "1")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = Accel()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import InitialDownForce


class TestInitialDownForce:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("15", "15")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = InitialDownForce()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("15", "15")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = InitialDownForce()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import CutLinePattern


class TestCutLinePattern:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = CutLinePattern()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = CutLinePattern()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import LtypeUp


class TestLtypeUp:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.6mm", "0.6mm")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = LtypeUp()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.6mm", "0.6mm")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = LtypeUp()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import LtypeDwn


class TestLtypeDwn:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("8.0mm", "8.0mm")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = LtypeDwn()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("8.0mm", "8.0mm")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = LtypeDwn()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import UpMode


class TestUpMode:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("UP", "UP")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = UpMode()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("UP", "UP")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = UpMode()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import TangentialMode


class TestTangentialMode:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = TangentialMode()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = TangentialMode()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import OvercutSE


class TestOvercutSE:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.0mm,0.0mm", "0.0mm,0.0mm")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = OvercutSE()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.0mm,0.0mm", "0.0mm,0.0mm")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = OvercutSE()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import DAdj


class TestDAdj:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = DAdj()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = DAdj()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import X


class TestX:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.00", "0.00")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = X()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.00", "0.00")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = X()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import Y


class TestY:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.00", "0.00")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = Y()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.00", "0.00")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = Y()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import Tool


class TestTool:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("PM-BS-001", "PM-BS-001")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = Tool()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("PM-BS-001", "PM-BS-001")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = Tool()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import Offset


class TestOffset:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0", "0")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = Offset()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0", "0")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = Offset()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import Speed


class TestSpeed:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("10", "10")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = Speed()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("10", "10")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = Speed()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import Force


class TestForce:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("17", "17")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = Force()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("17", "17")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = Force()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import Accel


class TestAccel:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("1", "1")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = Accel()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("1", "1")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = Accel()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import InitialDownForce


class TestInitialDownForce:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("15", "15")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = InitialDownForce()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("15", "15")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = InitialDownForce()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import CutLinePattern


class TestCutLinePattern:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = CutLinePattern()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = CutLinePattern()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import LtypeUp


class TestLtypeUp:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.6mm", "0.6mm")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = LtypeUp()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.6mm", "0.6mm")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = LtypeUp()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import LtypeDwn


class TestLtypeDwn:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("8.0mm", "8.0mm")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = LtypeDwn()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("8.0mm", "8.0mm")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = LtypeDwn()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import UpMode


class TestUpMode:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("UP", "UP")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = UpMode()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("UP", "UP")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = UpMode()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import TangentialMode


class TestTangentialMode:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = TangentialMode()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = TangentialMode()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import OvercutSE


class TestOvercutSE:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.0mm,0.0mm", "0.0mm,0.0mm")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = OvercutSE()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.0mm,0.0mm", "0.0mm,0.0mm")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = OvercutSE()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import DAdj


class TestDAdj:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = DAdj()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = DAdj()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import X


class TestX:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.00", "0.00")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = X()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.00", "0.00")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = X()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import Y


class TestY:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.00", "0.00")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = Y()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.00", "0.00")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = Y()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import Tool


class TestTool:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("PM-BS-001", "PM-BS-001")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = Tool()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("PM-BS-001", "PM-BS-001")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = Tool()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import Offset


class TestOffset:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0", "0")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = Offset()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0", "0")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = Offset()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import Speed


class TestSpeed:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("3", "3")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = Speed()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("3", "3")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = Speed()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import Force


class TestForce:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("20", "20")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = Force()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("20", "20")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = Force()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import Accel


class TestAccel:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("1", "1")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = Accel()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("1", "1")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = Accel()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import InitialDownForce


class TestInitialDownForce:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("15", "15")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = InitialDownForce()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("15", "15")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = InitialDownForce()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import CutLinePattern


class TestCutLinePattern:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = CutLinePattern()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = CutLinePattern()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import LtypeUp


class TestLtypeUp:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.6mm", "0.6mm")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = LtypeUp()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.6mm", "0.6mm")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = LtypeUp()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import LtypeDwn


class TestLtypeDwn:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("8.0mm", "8.0mm")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = LtypeDwn()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("8.0mm", "8.0mm")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = LtypeDwn()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import UpMode


class TestUpMode:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("UP", "UP")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = UpMode()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("UP", "UP")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = UpMode()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import TangentialMode


class TestTangentialMode:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = TangentialMode()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = TangentialMode()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import OvercutSE


class TestOvercutSE:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.0mm,0.0mm", "0.0mm,0.0mm")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = OvercutSE()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.0mm,0.0mm", "0.0mm,0.0mm")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = OvercutSE()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import DAdj


class TestDAdj:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = DAdj()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = DAdj()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import X


class TestX:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.00", "0.00")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = X()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.00", "0.00")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = X()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import Y


class TestY:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.00", "0.00")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = Y()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.00", "0.00")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = Y()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import Tool


class TestTool:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("PM-BS-001", "PM-BS-001")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = Tool()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("PM-BS-001", "PM-BS-001")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = Tool()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import Offset


class TestOffset:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0", "0")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = Offset()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0", "0")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = Offset()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import Speed


class TestSpeed:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("25", "25")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = Speed()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("25", "25")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = Speed()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import Force


class TestForce:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("17", "17")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = Force()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("17", "17")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = Force()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import Accel


class TestAccel:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("2", "2")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = Accel()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("2", "2")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = Accel()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import InitialDownForce


class TestInitialDownForce:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("15", "15")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = InitialDownForce()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("15", "15")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = InitialDownForce()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import CutLinePattern


class TestCutLinePattern:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = CutLinePattern()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = CutLinePattern()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import LtypeUp


class TestLtypeUp:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.6mm", "0.6mm")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = LtypeUp()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.6mm", "0.6mm")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = LtypeUp()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import LtypeDwn


class TestLtypeDwn:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("8.0mm", "8.0mm")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = LtypeDwn()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("8.0mm", "8.0mm")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = LtypeDwn()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import UpMode


class TestUpMode:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("UP", "UP")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = UpMode()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("UP", "UP")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = UpMode()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import TangentialMode


class TestTangentialMode:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = TangentialMode()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = TangentialMode()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import OvercutSE


class TestOvercutSE:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.0mm,0.0mm", "0.0mm,0.0mm")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = OvercutSE()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.0mm,0.0mm", "0.0mm,0.0mm")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = OvercutSE()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import DAdj


class TestDAdj:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = DAdj()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = DAdj()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import X


class TestX:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.00", "0.00")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = X()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.00", "0.00")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = X()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import Y


class TestY:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.00", "0.00")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = Y()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.00", "0.00")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = Y()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import Tool


class TestTool:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("PM-BS-001", "PM-BS-001")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = Tool()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("PM-BS-001", "PM-BS-001")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = Tool()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import Offset


class TestOffset:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0", "0")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = Offset()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0", "0")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = Offset()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import Speed


class TestSpeed:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("5", "5")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = Speed()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("5", "5")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = Speed()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import Force


class TestForce:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("26", "26")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = Force()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("26", "26")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = Force()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import Accel


class TestAccel:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("1", "1")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = Accel()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("1", "1")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = Accel()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import InitialDownForce


class TestInitialDownForce:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("15", "15")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = InitialDownForce()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("15", "15")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = InitialDownForce()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import CutLinePattern


class TestCutLinePattern:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = CutLinePattern()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = CutLinePattern()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import LtypeUp


class TestLtypeUp:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.6mm", "0.6mm")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = LtypeUp()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.6mm", "0.6mm")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = LtypeUp()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import LtypeDwn


class TestLtypeDwn:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("8.0mm", "8.0mm")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = LtypeDwn()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("8.0mm", "8.0mm")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = LtypeDwn()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import UpMode


class TestUpMode:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("UP", "UP")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = UpMode()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("UP", "UP")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = UpMode()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import TangentialMode


class TestTangentialMode:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = TangentialMode()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = TangentialMode()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import OvercutSE


class TestOvercutSE:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.0mm,0.0mm", "0.0mm,0.0mm")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = OvercutSE()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.0mm,0.0mm", "0.0mm,0.0mm")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = OvercutSE()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import DAdj


class TestDAdj:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = DAdj()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = DAdj()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import X


class TestX:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.00", "0.00")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = X()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.00", "0.00")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = X()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import Y


class TestY:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.00", "0.00")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = Y()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.00", "0.00")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = Y()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import StepPass


class TestStepPass:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("1", "1")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = StepPass()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("1", "1")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = StepPass()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import OffsetForce


class TestOffsetForce:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("10", "10")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = OffsetForce()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("10", "10")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = OffsetForce()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import OffsetAngle


class TestOffsetAngle:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("30", "30")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = OffsetAngle()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("30", "30")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = OffsetAngle()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import DataSort


class TestDataSort:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = DataSort()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = DataSort()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import ToolUpSpeed


class TestToolUpSpeed:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("AUTO", "AUTO")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = ToolUpSpeed()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("AUTO", "AUTO")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = ToolUpSpeed()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import ConditionPriority


class TestConditionPriority:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("PROGRAM", "PROGRAM")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = ConditionPriority()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("PROGRAM", "PROGRAM")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = ConditionPriority()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import InitialBlade


class TestInitialBlade:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("2mm BELOW", "2mm BELOW")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = InitialBlade()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("2mm BELOW", "2mm BELOW")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = InitialBlade()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import ToolUpMove


class TestToolUpMove:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("ENABLED", "ENABLED")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = ToolUpMove()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("ENABLED", "ENABLED")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = ToolUpMove()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import MarkScanMode


class TestMarkScanMode:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = MarkScanMode()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = MarkScanMode()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import NumberOfPoints


class TestNumberOfPoints:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("2POINTS", "2POINTS")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = NumberOfPoints()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("2POINTS", "2POINTS")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = NumberOfPoints()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import MarkDistanceXY


class TestMarkDistanceXY:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.0mm,   0.0mm", "0.0mm,   0.0mm")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = MarkDistanceXY()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.0mm,   0.0mm", "0.0mm,   0.0mm")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = MarkDistanceXY()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import SensingSpeed


class TestSensingSpeed:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("NORMAL", "NORMAL")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = SensingSpeed()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("NORMAL", "NORMAL")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = SensingSpeed()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import MarkType


class TestMarkType:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("2", "2")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = MarkType()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("2", "2")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = MarkType()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import DAdjMode


class TestDAdjMode:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("USER", "USER")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = DAdjMode()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("USER", "USER")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = DAdjMode()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import MarkDistAdjUnit


class TestMarkDistAdjUnit:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("5mm", "5mm")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = MarkDistAdjUnit()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("5mm", "5mm")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = MarkDistAdjUnit()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import MarkOffsetXY


class TestMarkOffsetXY:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.0mm,  0.0mm", "0.0mm,  0.0mm")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = MarkOffsetXY()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.0mm,  0.0mm", "0.0mm,  0.0mm")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = MarkOffsetXY()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import MarkAutoScan


class TestMarkAutoScan:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("ON", "ON")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = MarkAutoScan()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("ON", "ON")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = MarkAutoScan()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import PaperWeight


class TestPaperWeight:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("ON", "ON")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = PaperWeight()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("ON", "ON")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = PaperWeight()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import SensorOffsetAdj


class TestSensorOffsetAdj:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.0mm,0.0mm", "0.0mm,0.0mm")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = SensorOffsetAdj()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.0mm,0.0mm", "0.0mm,0.0mm")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = SensorOffsetAdj()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import MarkSize


class TestMarkSize:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("20.0", "20.0")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = MarkSize()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("20.0", "20.0")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = MarkSize()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import SensorAdjust


class TestSensorAdjust:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = SensorAdjust()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = SensorAdjust()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import SensingLevelXY


class TestSensingLevelXY:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("70,80", "70,80")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = SensingLevelXY()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("70,80", "70,80")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = SensingLevelXY()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import FactorySensorGain


class TestFactorySensorGain:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0", "0")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = FactorySensorGain()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0", "0")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = FactorySensorGain()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import FactoryBaseLevel


class TestFactoryBaseLevel:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0", "0")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = FactoryBaseLevel()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0", "0")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = FactoryBaseLevel()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import FactorySensingLevelXY


class TestFactorySensingLevelXY:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0,0", "0,0")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = FactorySensingLevelXY()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0,0", "0,0")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = FactorySensingLevelXY()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import UserSensorGain


class TestUserSensorGain:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0", "0")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = UserSensorGain()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0", "0")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = UserSensorGain()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import UserBaseLevel


class TestUserBaseLevel:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0", "0")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = UserBaseLevel()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0", "0")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = UserBaseLevel()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import UserSensingLevelXY


class TestUserSensingLevelXY:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0,0", "0,0")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = UserSensingLevelXY()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0,0", "0,0")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = UserSensingLevelXY()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import RmSensorLevelAdjSelect


class TestRmSensorLevelAdjSelect:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("USER", "USER")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = RmSensorLevelAdjSelect()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("USER", "USER")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = RmSensorLevelAdjSelect()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import Expand


class TestExpand:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("10.0mm", "10.0mm")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = Expand()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("10.0mm", "10.0mm")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = Expand()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import Rotate


class TestRotate:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = Rotate()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = Rotate()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import Mirror


class TestMirror:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = Mirror()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = Mirror()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import Scale


class TestScale:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("1", "1")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = Scale()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("1", "1")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = Scale()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import InitialFeed


class TestInitialFeed:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = InitialFeed()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = InitialFeed()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import FeedSpeed


class TestFeedSpeed:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("NORMAL", "NORMAL")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = FeedSpeed()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("NORMAL", "NORMAL")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = FeedSpeed()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import AutoPreFeed


class TestAutoPreFeed:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = AutoPreFeed()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = AutoPreFeed()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import AutoPreFeedLength


class TestAutoPreFeedLength:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("300.0mm", "300.0mm")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = AutoPreFeedLength()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("300.0mm", "300.0mm")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = AutoPreFeedLength()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import PageLength


class TestPageLength:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("500.0mm", "500.0mm")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = PageLength()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("500.0mm", "500.0mm")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = PageLength()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import PreFeed


class TestPreFeed:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("300.0mm", "300.0mm")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = PreFeed()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("300.0mm", "300.0mm")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = PreFeed()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import PanelCutting


class TestPanelCutting:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = PanelCutting()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = PanelCutting()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import DivideLength


class TestDivideLength:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("100.0cm", "100.0cm")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = DivideLength()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("100.0cm", "100.0cm")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = DivideLength()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import BaudRate


class TestBaudRate:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0", "0")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = BaudRate()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0", "0")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = BaudRate()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import Parity


class TestParity:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("NONE", "NONE")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = Parity()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("NONE", "NONE")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = Parity()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import DataBit


class TestDataBit:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("8 BIT", "8 BIT")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = DataBit()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("8 BIT", "8 BIT")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = DataBit()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import Handshake


class TestHandshake:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("HARDWIRE", "HARDWIRE")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = Handshake()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("HARDWIRE", "HARDWIRE")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = Handshake()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import Command


class TestCommand:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("HP-GL", "HP-GL")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = Command()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("HP-GL", "HP-GL")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = Command()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import GpGlStepSize


class TestGpGlStepSize:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.100mm", "0.100mm")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = GpGlStepSize()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.100mm", "0.100mm")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = GpGlStepSize()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import HpGlOrigin


class TestHpGlOrigin:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("LOWER LEFT", "LOWER LEFT")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = HpGlOrigin()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("LOWER LEFT", "LOWER LEFT")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = HpGlOrigin()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import HpGlModelEmulated


class TestHpGlModelEmulated:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("7586", "7586")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = HpGlModelEmulated()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("7586", "7586")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = HpGlModelEmulated()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import CircleResolution


class TestCircleResolution:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("DEFAULT", "DEFAULT")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = CircleResolution()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("DEFAULT", "DEFAULT")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = CircleResolution()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import CommandColSemiCol


class TestCommandColSemiCol:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("ENABLED", "ENABLED")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = CommandColSemiCol()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("ENABLED", "ENABLED")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = CommandColSemiCol()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import CommandW


class TestCommandW:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("TOOL UP", "TOOL UP")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = CommandW()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("TOOL UP", "TOOL UP")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = CommandW()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import MoveStep


class TestMoveStep:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.1mm", "0.1mm")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = MoveStep()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("0.1mm", "0.1mm")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = MoveStep()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import LanguageSelection


class TestLanguageSelection:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("English", "English")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = LanguageSelection()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("English", "English")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = LanguageSelection()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import LengthUnit


class TestLengthUnit:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("METRIC", "METRIC")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = LengthUnit()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("METRIC", "METRIC")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = LengthUnit()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import MediaSensor


class TestMediaSensor:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("ENABLED", "ENABLED")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = MediaSensor()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("ENABLED", "ENABLED")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = MediaSensor()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import PushRollerSensor


class TestPushRollerSensor:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("DISABLED", "DISABLED")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = PushRollerSensor()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("DISABLED", "DISABLED")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = PushRollerSensor()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import FanPower


class TestFanPower:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("WEAK", "WEAK")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = FanPower()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("WEAK", "WEAK")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = FanPower()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import BeepForKeyOpe


class TestBeepForKeyOpe:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = BeepForKeyOpe()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("OFF", "OFF")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = BeepForKeyOpe()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value


# ----------------------------------------------------------------------------------------------------
from inkcut.device.graphtec_ce_50_lite.plotter_parameters import CopySpace


class TestCopySpace:

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("1.00mm", "1.00mm")])
    def test_value_from_string(self, input_value, expected_value):
        parameter = CopySpace()
        parameter.set_value(input_value)
        assert parameter.get_value() == expected_value

    # ------------------------------------------------------------------------------------------------

    # TODO PTAR Update this method if required with other values
    @pytest.mark.parametrize("input_value,expected_value", [("1.00mm", "1.00mm")])
    def test_get_update_command(self, input_value, expected_value):
        parameter = CopySpace()
        parameter.set_value(input_value)
        if parameter.is_readonly():
            assert parameter.get_update_command() == ""
            return

        assert parameter.get_update_command() == expected_value
