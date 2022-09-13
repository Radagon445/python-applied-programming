class Person:
    def __init__(self, name):
        self.name = name

    def writeletter(self):
        print(f"{self.name} has written a letter.")

    def sendletter(self):
        print(f"{self.name} has sent a letter.")

    def readletter(self):
        print(f"{self.name} has read the letter.")

