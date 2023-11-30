import numpy as np

def compare(data):
    ideal = np.array([1, 2, 3])
    is_correct = (np.array(data)==ideal).all()
    print("test success: ", is_correct)
    