from enum import Enum

class Errors(Enum):
    NoError = 0
    BatteryVoltageTooHigh = 2
    ChargerTemperatureTooHigh = 17
    ChargerOverCurrent = 18
    ChargerCurrentReversed = 19
    BulkTimeLimitExceeded = 20
    CurrentSensorIssue = 21
    TerminalsOverheated = 26
    ConverterIssue = 28
    InputVoltageTooHigh = 33
    InputCurrentTooHigh = 34
    InputShutdownExcessVoltage = 38
    InputShutdownCurrentInOffMode = 39
    LostCommunicationWithOneOfDevices = 65
    SynchronisedChargingDeviceConfigurationIssue = 66
    BMSConnectionLost = 67
    NetworkMisconfigured = 68
    FactoryCalibrationDataLost = 116
    InvalidincompatibleFirmware = 117
    UserSettingsInvalid = 119