from enum import Enum

class MpptStates(Enum):
    Off = 0
    VoltageOrCurrentLimited = 1
    TrackerActive = 2