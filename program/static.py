class MyClass:
    static_variable = 0

    def _init_(self, value):
        self.instance_variable = value

    def increment_static_variable(self):
        MyClass.static_variable += 1
obj1 = MyClass()
obj2 = MyClass()
print("Static Variable before increment:", MyClass.static_variable)
obj1.increment_static_variable()
print("Static Variable after increment from obj1:", MyClass.static_variable)
obj2.increment_static_variable()
print("Static Variable after increment from obj2:", MyClass.static_variable)




class Student:
    total_students = 0
    def _init_(self, name):
        self.name = name
        Student.total_students += 1
    def get_total_students():
        return Student.total_students
student1 = Student()
student2 = Student()
student3 = Student()
total_students = Student.get_total_students()

print(f"Total students: {total_students}")