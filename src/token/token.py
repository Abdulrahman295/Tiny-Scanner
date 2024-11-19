from src.token.tokenType import *

class Token:
    def __init__(self, token_type: TokenType, token_value: str):
        self.token_type = token_type
        self.token_value = token_value

    def set_type(self, token_type):
        self.token_type = token_type

    def get_type(self):
        return self.token_type

    def set_value(self, token_value):
        self.token_value = token_value

    def get_value(self):
        return self.token_value

    def __str__(self):
        return f"{self.token_value} , {self.token_type}"