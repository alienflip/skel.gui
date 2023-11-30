from operation.methods.test_op import _test_op

class operations_class:
    def __init__(self):
        pass

    def test_op(self, data):
        output = _test_op(data)
        print("operation output: ", output)
        return output