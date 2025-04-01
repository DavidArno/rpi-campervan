from rpi_campervan.data_sources.alarm_reasons import AlarmReasons
from rpi_campervan.data_sources.inverter import VictronInverter
from rpi_campervan.data_sources.modes import Modes
from rpi_campervan.data_sources.off_reasons import OffReasons
from rpi_campervan.data_sources.states import States

def test_from_usb_correctly_creates_an_object():
    usb_data = {
        "MODE" : "4",
        "CS" : "0", 
        "AC_OUT_V" : "123", 
        "AC_OUT_I" : "45",
        "V" : "678",
        "AR" : "1",
        "WARN" : "2",
        "OR" : "180"}

    object = VictronInverter.from_usb_data(usb_data)
    
    assert object.mode == Modes.Off
    assert object.state == States.Off
    assert object.out_volts == 1.23
    assert object.out_amps == 4.5
    assert object.in_volts == 6.78
    assert object.alarms == AlarmReasons.LowVoltage
    assert object.warnings == AlarmReasons.HighVoltage
    assert object.off_reason == OffReasons.AnalysingInputVoltage | OffReasons.EngineShutdownDetection
    