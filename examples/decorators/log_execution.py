from hollosmodule import Decorators

decs = Decorators()

@decs.log_execution(log_to='file')
def hello():
    return "Hello, World!"

if __name__ == "__main__":
    print(hello())