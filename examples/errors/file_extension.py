from hollosmodule import Exceptions
from tkinter import filedialog
import os

err = Exceptions()

def get_file():
    file = filedialog.askopenfilename(filetypes=[("All Files", "*.*")])
    return file

def check_file(file: str, supported_files: list):
    if os.path.splitext(file)[1] in supported_files:
        return True
    else:
        raise err.UnsupportedFileExtensionError(os.path.splitext(file)[1])