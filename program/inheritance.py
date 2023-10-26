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




class Parent1:
    def method1(self):
        print("Method from Parent1")

class Parent2:
    def method2(self):
        print("Method from Parent2")

class Child(Parent1, Parent2):
    def child_method(self):
        print("Method from Child")

child = Child()
child.method1()  
child.method2() 

child.child_method()  


class Parent:
    def method(self):
        print("Method from Parent")

class Child1(Parent):
    def child1_method(self):
        print("Method from Child1")


class Child2(Parent):
    def child2_method(self):
        print("Method from Child2")

child1 = Child1()
child2 = Child2()


child1.method()        
child1.child1_method()  

child2.method()        
child2.child2_method()   




