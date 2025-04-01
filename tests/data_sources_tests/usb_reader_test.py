from rpi_campervan.data_sources.inverter import VictronUsbReader


def test_serial_data_is_correctly_decoded_into_a_data_packet():
    test_data = "V\t26200\r\nI\t0\r\nP\t0\r\nCE\t0\r\nSOC\t1000\r\nTTG\t-1\r\nAlarm\tOFF\r\n" \
                "Relay\tOFF\r\nAR\t0\r\nBMV\t700\r\nFW\t0307\r\nChecksum\t0\r\nPID\t0x200\r\n" \
                "V\t26201\r\nI\t0\r\nP\t0\r\nCE\t0\r\nSOC\t1000\r\nTTG\t-1\r\nAlarm\tOFF\r\n" \
                "Relay\tOFF\r\nAR\t0\r\nBMV\t700\r\nFW\t0307\r\nChecksum\t0\r\nPID\t0x201\r\n" \
                "V\t26202\r\nI\t0\r\nP\t0\r\nCE\t0\r\nSOC\t1000\r\nTTG\t-1\r\nAlarm\tOFF\r\n" \
                "Relay\tOFF\r\nAR\t0\r\nBMV\t700\r\nFW\t0307\r\nChecksum\t0"

    dict = {}
    for item in VictronUsbReader(lambda : _MockSerial()):
        dict

class _MockSerial:
    def __init__(this, test_data):
        this._test_data = test_data
        this._index = 0

        def close(this):
            pass

        def read(this):
            char = this._test_data[this._index]
            this._index += 1
            return char
