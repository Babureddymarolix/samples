class Grandparent:
    def _init_(self, grandparent_name):
        self.grandparent_name = grandparent_name

    def show_grandparent_name(self):
        print("Grandparent Name:", self.grandparent_name)

class Parent(Grandparent):
    def _init_(self, grandparent_name, parent_name):
        super()._init_(grandparent_name)
        self.parent_name = parent_name

    def show_parent_name(self):
        print("Parent Name:", self.parent_name)


class Child(Parent):
    def _init_(self, grandparent_name, parent_name, child_name):
        super()._init_(grandparent_name, parent_name)
        self.child_name = child_name

    def show_child_name(self):
        print("Child Name:", self.child_name)


child = Child("Grandma", "Mom", "Alice")


child.show_grandparent_name() 
child.show_parent_name()      
child.show_child_name()        