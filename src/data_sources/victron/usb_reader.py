# type: ignore 
from serial import Serial

class VictronUsbReader:
    def __init__(self, usb : str) -> None:
        self.usb = usb

    def __enter__(self):
        self.port = Serial(self.usb, 19200, timeout=1)
        return self

    def __exit__(self, type, value, traceback) -> None:
        self.port.close()

    def __iter__(self):
        self.seek_pid = True
        self.package_read_complete = False
        return self

    def __next__(self):
        if self.package_read_complete:
            raise StopIteration()

        valid_entry = False

        while not valid_entry:
            while self.port.read() != b'\n':
                pass
            buffer = b""
            while (char := self.port.read()) != b'\r':
                buffer += char

            if self.seek_pid and not buffer.startswith(b"PID\t"):
                continue

            if buffer.startswith(b"Checksum\t"):
                self.package_read_complete = True

            self.seek_pid = False

            return buffer

