from src.scanner.scannerState import *
from src.token.token import *

class Scanner:
    def __init__(self, code: str):
        self.code = code
        self.current_state = ScannerState.START
        self.current_lexeme = ""
        self.tokens = []


    def set_state(self, state: ScannerState):
        self.current_state = state

    def get_state(self) -> ScannerState:
        return self.current_state

    def tokenize(self) -> list[Token]:
        index = 0

        while index < len(self.code):
            current_char = self.code[index]

            if self.current_state == ScannerState.START:
                index = self.handle_start_state(index, current_char)

            elif self.current_state == ScannerState.INCOMMENT:
                index = self.handle_comment_state(index, current_char)

            elif self.current_state == ScannerState.INNUM:
                index = self.handle_number_state(index, current_char)

            elif self.current_state == ScannerState.INID:
                index = self.handle_identifier_state(index, current_char)

            elif self.current_state == ScannerState.INASSIGN:
                index = self.handle_assign_state(index, current_char)


        # finalize any remaining tokens
        if self.current_lexeme:
            if self.current_state == ScannerState.INNUM:
                self.tokens.append(Token(TokenType.NUMBER, self.current_lexeme))
            elif self.current_state == ScannerState.INID:
                keyword_tokens = {
                    'if': TokenType.IF,
                    'then': TokenType.THEN,
                    'end': TokenType.END,
                    'repeat': TokenType.REPEAT,
                    'until': TokenType.UNTIL,
                    'read': TokenType.READ,
                    'write': TokenType.WRITE
                }

                token_type = keyword_tokens.get(self.current_lexeme, TokenType.IDENTIFIER)
                self.tokens.append(Token(token_type, self.current_lexeme))

        return self.tokens

    def handle_start_state(self, index: int, current_char: str) -> int:
        if current_char.isspace():
            return index + 1

        elif current_char.isdigit():
            self.current_state = ScannerState.INNUM
            self.current_lexeme += current_char
            return index + 1

        elif current_char.isalpha():
            self.current_state = ScannerState.INID
            self.current_lexeme += current_char
            return index + 1

        elif current_char == '{':
            self.current_state = ScannerState.INCOMMENT
            return index + 1

        elif current_char == ':':
            self.current_state = ScannerState.INASSIGN
            self.current_lexeme += current_char
            return index + 1

        elif current_char in ['+', '-', '*', '/', '<', '=', ';', '(', ')']:
            operator_tokens = {
                '+': TokenType.PLUS,
                '-': TokenType.MINUS,
                '*': TokenType.MULT,
                '/': TokenType.DIV,
                '<': TokenType.LESSTHAN,
                '=': TokenType.EQUAL,
                ';': TokenType.SEMICOLON,
                '(': TokenType.OPENBRACKET,
                ')': TokenType.CLOSEDBRACKET
            }
            self.tokens.append(Token(operator_tokens[current_char], current_char))
            self.current_lexeme = ""
            return index + 1

        else:
            raise ValueError(f"Unrecognized character: {current_char}")

    def handle_comment_state(self, index: int, current_char: str) -> int:
        if current_char == '}':
            self.current_state = ScannerState.START

        return index + 1

    def handle_number_state(self, index: int, current_char: str) -> int:
        if current_char.isdigit():
            self.current_lexeme += current_char
            return index + 1

        else:
            self.tokens.append(Token(TokenType.NUMBER, self.current_lexeme))
            self.current_lexeme = ""
            self.current_state = ScannerState.START
            return index

    def handle_identifier_state(self, index: int, current_char: str) -> int:
        if current_char.isalnum():
            self.current_lexeme += current_char
            return index + 1

        else:
            keyword_tokens = {
                'if': TokenType.IF,
                'then': TokenType.THEN,
                'end': TokenType.END,
                'repeat': TokenType.REPEAT,
                'until': TokenType.UNTIL,
                'read': TokenType.READ,
                'write': TokenType.WRITE
            }

            token_type = keyword_tokens.get(self.current_lexeme, TokenType.IDENTIFIER)
            self.tokens.append(Token(token_type, self.current_lexeme))
            self.current_lexeme = ""
            self.current_state = ScannerState.START
            return index

    def handle_assign_state(self, index: int, current_char: str) -> int:
        if current_char == '=':
            self.current_lexeme += current_char
            self.tokens.append(Token(TokenType.ASSIGN, self.current_lexeme))
            self.current_lexeme = ""
            self.current_state = ScannerState.START
            return index + 1

        else:
            raise ValueError(f"Unrecognized character in assign: {current_char}")