from enum import Enum

class States(Enum):
    Off = 0 
    LowPower = 1
    Fault = 2 
    Bulk = 3
    Absorption = 4
    Float = 5
    Storage = 6 
    ManualEqualize = 7 
    Inverting = 9 
    PowerSupply = 11 
    StartingUp = 245 
    RepeatedAbsorption = 246 
    AutoEqualizeRecondition = 247 
    BatterySafe = 248 
    ExternalControl = 252