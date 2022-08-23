from rpi_campervan.data_sources.modes import Modes
from rpi_campervan.data_sources.states import States
from rpi_campervan.data_sources.alarm_reasons import AlarmReasons
from rpi_campervan.data_sources.off_reasons import OffReasons

class VictronInverter:

    @classmethod
    def from_usb_data(cls, data : dict[str, str]):
        return cls(
            data["MODE"], 
            data["CS"], 
            data["AC_OUT_V"], 
            data["AC_OUT_I"],
            data["V"],
            data["AR"],
            data["WARN"],
            data["OR"][-3:])

    @classmethod
    def from_message(cls, message : str):
        (mode, state, out_volts, out_amps, in_volts, alarms, warnings, off_reason) = message[4:-1].split(",")
        return cls(
            mode, 
            state, 
            out_volts, 
            out_amps, 
            in_volts, 
            alarms, 
            warnings, 
            off_reason)

    def __init__(self, mode, state, out_volts, out_amps, in_volts, alarms, warnings, off_reason) -> None:
        self._mode = mode
        self._state = state
        self._out_volts = out_volts
        self._out_amps = out_amps
        self._in_volts = in_volts
        self._alarms = alarms
        self._warnings = warnings
        self._off_reason = off_reason

    def to_message(self):
        return f"inv({self._mode},{self._state},{self._out_volts},{self._out_amps},{self._in_volts}," \
               f"{self._in_volts},{self._alarms},{self._warnings},{self._off_reason})"

    @property
    def mode(self):
        return Modes(int(self._mode))

    @property
    def state(self):
        return States(int(self._state))

    @property
    def out_volts(self):
        return float(self._out_volts)/100.0

    @property
    def out_amps(self):
        return float(self._out_amps)/10.0

    @property
    def in_volts(self):
        return float(self._in_volts)/100.0

    @property
    def alarms(self):
        return AlarmReasons(int(self._alarms))

    @property
    def warnings(self):
        return AlarmReasons(int(self._warnings))

    @property
    def off_reason(self):
        return OffReasons(int(self._off_reason, 16))
