import sys
import os


def get_path():
    def safe_chdir(path):
        try:
            os.chdir(path)
        except UnicodeEncodeError:
            encoded_path = path.encode('utf-8').decode('utf-8')
            os.chdir(encoded_path)

    if getattr(sys, 'frozen', False):
        safe_chdir(os.path.dirname(sys.executable))
    else:
        safe_chdir(os.path.dirname(os.path.abspath(__file__)))
    cwd = os.getcwd()
    return cwd
