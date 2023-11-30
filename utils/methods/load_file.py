import os

def _load(path):
    if os.path.isfile(path):
        f = open(path, "r")
        content = f.read() 
        f.close()
        print(content)
        print("file loaded from: " + path)
    else:
        print("file not found")