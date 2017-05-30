class myClass:
    def __init__(self):
        self.data = []
    def printSomething(self):
        print self.data


_myClass = myClass()

_myClass.printSomething()
_myClass.data.append("Test")
_myClass.printSomething()
