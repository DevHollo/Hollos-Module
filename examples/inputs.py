from hollosmodule import (
    inputstr,
    inputint,
    inputfloat,
    maskedinput
)

string = inputstr("type word: ")
integer = inputint("type whole num: ")
decimal = inputfloat("type decimal num: ")
masked = maskedinput("type secret: ")

print(f"""
You typed:
string: {string}
integer: {integer}
decimal: {decimal}
masked: {masked}
""")