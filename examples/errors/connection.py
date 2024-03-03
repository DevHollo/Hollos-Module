from hollosmodule import Exceptions

err = Exceptions()

def is_connected():
    """
    pretend there is code here
    """

def connect_to_server():
    if not is_connected():
        raise err.ConnectionError("Unable to establish connection to the server")

try:
    connect_to_server()
except err.ConnectionError as e:
    print(e)