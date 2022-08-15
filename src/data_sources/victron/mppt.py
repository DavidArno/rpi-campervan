from mppt_states import MpptStates
from states import States
from errors import Errors
from off_reasons import OffReasons

class VictronMppt:

    @classmethod
    def from_usb_data(cls, data : dict[str, str]):
        return cls(
            data['V'],
            data['I'],
            data['VPV'],
            data['PPV'],
            data['CS'],
            data['MPPT'],
            data["OR"][-3:],
            data['ERR'],
            1 if data['LOAD'] == 'ON' else 0,
            data['IL'],
            data['H19'],
            data['H20'],
            data['H21'],
            data['H22'],
            data['H23'],
            data['HSDS'])

    @classmethod
    def from_message(cls, message : str):
        (batt_volts, batt_amps, solar_volts, solar_watts, state, mppt_state, off_reason, \
         error, load_on, load_amps, yield_total, yield_today, max_watts_today, \
         yield_yesterday, max_watts_yesterday,  day_num) = message[5:-1].split(",")

        return cls(
            batt_volts, 
            batt_amps, 
            solar_volts, 
            solar_watts, 
            state, 
            mppt_state, 
            off_reason,
            error,
            load_on,
            load_amps,
            yield_total,
            yield_today,
            max_watts_today,
            yield_yesterday,
            max_watts_yesterday,
            day_num)

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
        return f"mppt({self._mode},{self._state},{self._out_volts},{self._out_amps},{self._in_volts}," \
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
