from src.scanner.scanner import *

code = "{ Sample program in TINY language - computes factorial } read x; if x < 10 then y := x + 1; end;"

scanner = Scanner(code)

tokens = scanner.tokenize()

for token in tokens:
    print(token)