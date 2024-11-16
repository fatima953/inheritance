class Nabiha:
    def __init__(self):
        print("parent class is ready!")
    def who(self):
        print("my mother")
    def work(self):
        print("home maker")
class Fatima(Nabiha):
    def __init__(self):
        super().__init__()
        print("child is ready")
    def whoisthis(self):
        print("it is me")
    def work(self):
        print("i am a student")
#object
child = Fatima()
child.whoisthis()
child.work()
child.who()
     