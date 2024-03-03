from hollosmodule import Decorators

decs = Decorators()

@decs.delay_execution(3)
def say_hello():
    print("Hello World!")

if __name__ == "__main__":
    say_hello()