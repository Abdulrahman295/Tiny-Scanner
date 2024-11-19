from enum import Enum, auto

class ScannerState(Enum):
    START = auto()
    INCOMMENT = auto()
    INNUM = auto()
    INID = auto()
    INASSIGN = auto()
    DONE = auto()

    def __str__(self):
        return self.name