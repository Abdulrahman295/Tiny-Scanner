from enum import Enum, auto

class TokenType(Enum):
    SEMICOLON = auto() 
    IF = auto()
    THEN = auto()
    END = auto()
    REPEAT = auto()
    UNTIL = auto()
    IDENTIFIER = auto()
    ASSIGN = auto()
    READ = auto()
    WRITE = auto()
    LESSTHAN = auto()
    EQUAL = auto()
    PLUS = auto()
    MINUS = auto()
    MULT = auto()
    DIV = auto()
    OPENBRACKET = auto()
    CLOSEDBRACKET = auto()
    NUMBER = auto()

    def __str__(self):
        return self.name