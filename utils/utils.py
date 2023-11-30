from utils.methods.load_file import _load
from utils.methods.save_file import _save

class utils_class:
    def __init__(self):
        pass

    def load(self, path):
        return _load(path)

    def save(self, path, text):
        return _save(path, text)