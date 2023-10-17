class Parent:
    def _init_(self, name):
        self.name = name

    def show_name(self):
        print("Name:", self.name)


class Child(Parent):
    def _init_(self, name, age):
        super()._init_(name)
        self.age = age

    def show_age(self):
        print("Age:", self.age)

child = Child("babu",25)

child.show_name()  
child.show_age()   