

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
        (battery_volts, battery_amps, solar_volts, solar_watts, state, mppt_state, off_reason, \
         error, load_on, load_amps, yield_total, yield_today, max_watts_today, \
         yield_yesterday, max_watts_yesterday,  day_num) = message[5:-1].split(",")

        return cls(
            battery_volts, 
            battery_amps, 
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

    def __init__(self, battery_volts, battery_amps, solar_volts, solar_watts, state, mppt_state, off_reason, \
                 error, load_on, load_amps, yield_total, yield_today, max_watts_today, \
                 yield_yesterday, max_watts_yesterday,  day_num) -> None:
        self._battery_volts = battery_volts 
        self._battery_amps = battery_amps 
        self._solar_volts = solar_volts 
        self._solar_watts = solar_watts 
        self._state = state 
        self.__mppt_state = mppt_state 
        self._off_reason = off_reason
        self._error = error
        self._load_on = load_on
        self._load_amps = load_amps
        self._yield_total = yield_total
        self._yield_today = yield_today
        self._max_watts_today = max_watts_today
        self._yield_yesterday = yield_yesterday
        self._max_watts_yesterday = max_watts_yesterday
        self._day_num = day_num

    def to_message(self):
        return f"mppt( {self._battery_volts},{self._battery_amps},{self._solar_volts}, {self._solar_watts}," \
               f"{self._state},{self._mppt_state},{self._off_reason},{self._error},{self._load_on}," \
               f"{self._load_amps},{self._yield_total},{self._yield_today},{self._max_watts_today}," \
               f"{self._yield_yesterday},{self._max_watts_yesterday}, {self._day_num})"

    @property
    def battery_volts(self):
        return float(self._battery_volts)/100.0

    @property
    def battery_amps(self):
        return float(self._battery_amps)/10.0

    @property
    def solar_volts(self):
        return float(self._solar_volts)

    @property
    def solar_watts(self):
        return float(self._solar_watts)

    @property
    def state(self):
        return States(int(self._state))

    @property
    def mppt_state(self):
        return MpptStates(int(self.__mppt_state))

    @property
    def off_reason(self):
        return OffReasons(int(self._off_reason, 16))

    @property
    def error(self):
        return Errors(int(self._error))

    @property
    def load_on(self):
        return self._load_on == 1

    @property
    def load_amps(self):
        return float(self._load_amps)/10.0

    @property
    def yield_total(self):
        return float(self._yield_total)/100.0

    @property
    def yield_today(self):
        return float(self._yield_today)/100.0

    @property
    def max_watts_today(self):
        return float(self._max_watts_today)

    @property
    def yield_yesterday(self):
        return float(self._yield_yesterday)/100.0

    @property
    def max_watts_yesterday(self):
        return float(self._max_watts_yesterday)

    @property
    def day_num(self):
        return int(self._day_num)
