def _save(path, text):
    f = open(path, "w")
    f.write(text)
    f.close()
    print("file saved to: " + path)
