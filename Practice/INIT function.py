#INIT()automatic call function.
# we can create class without init() no problem (compiler will automatically implicit).
# if we create a init() we can also keep empty
class Student:
    def __int__(self):
        self.x=20
        self.y=30
        print("constructor invoke")
mystudent=Student()
print()