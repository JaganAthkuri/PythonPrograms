class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getname(self):
        print("Your name is ", self.name)


s1 = student("Ravi", 25)
print(s1.age)
print(s1.name)
s1.getname()