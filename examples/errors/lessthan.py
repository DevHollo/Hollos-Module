from hollosmodule import Exceptions

e = Exceptions()

num = float(input("enter a number greater than 1: "))

if num <= 1.0 or num == 1.0:
    raise e.LessThanError("number must be greater than 1!")