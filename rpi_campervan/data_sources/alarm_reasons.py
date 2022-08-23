from enum import Flag

class AlarmReasons(Flag):
    NoAlarms = 0
    LowVoltage = 1
    HighVoltage = 2 
    LowSOC = 4
    LowStarterVoltage = 8 
    HighStarterVoltage = 16 
    LowTemperature = 32
    HighTemperature = 64 
    MidVoltage = 128
    Overload = 256
    DCRipple = 512 
    LowVoltageACOut = 1024
    HighVoltageACOut = 2048