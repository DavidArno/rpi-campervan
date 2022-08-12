from enum import Flag

class OffReasons(Flag):
    NoInputPower = 0x001
    SwitchedOffPowerSwitch = 0x002
    SwitchedOffDeviceModeRegister = 0x004
    RemoteInput = 0x008
    ProtectionActive = 0x010
    Paygo = 0x020
    BMS = 0x040
    EngineShutdownDetection = 0x080
    AnalysingInputVoltage = 0x100