class VictronUsbReader:
    def __init__(self, serial_provider : function) -> None:
        self._serial_provider = serial_provider

    def __enter__(self):
        self._port = self._serial_provider()
        return self

    def __exit__(self, type, value, traceback) -> None:
        self._port.close()

    def __iter__(self):
        self._seek_pid = True
        self._package_read_complete = False
        return self

    def __next__(self):
        if self._package_read_complete:
            raise StopIteration()

        valid_entry = False

        while not valid_entry:
            while self._port.read() != b'\n':
                pass
            buffer = b""
            while (char := self._port.read()) != b'\r':
                buffer += char

            if self.seek_pid and not buffer.startswith(b"PID\t"):
                continue

            if buffer.startswith(b"Checksum\t"):
                self._package_read_complete = True

            self._seek_pid = False

            return buffer

