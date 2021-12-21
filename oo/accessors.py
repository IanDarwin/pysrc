""" Demonstrate having private methods and controlled accessors.
Adapted from https://docs.python.org/3/library/functions.html#property
"""
class Accessors:
    def __init__(self):
        self._x = None
        self._meaning = 42

    def getx(self):
        print("In getx()")
        return self._x

    def setx(self, value):
        print("In setx()")
        self._x = value

    def delx(self):
        print("In delx()")
        del self._x

    x = property(getx, setx, delx, "I'm the 'x' property.")

    @property
    def meaning(self):
        """Get the meaning of life"""
        return self._meaning

def main():
    print("Starting")
    obj = Accessors()
    print(obj.x)        # Invokes get method
    obj.x = 42          # Invokes set method
    print(obj.x)        # Invokes get method
    del obj.x           # Invokes del method
    print(dir(obj))
    print("Finally, the meaning of life is...", obj.meaning)

if __name__ == '__main__':
    main()
