class Student():
    name = ""
    student_class = "9H"
    age = 13
    height = 180

    # Create Constructor
    def __init__(self):
        print("Creating a Student")
    
    # Changing Details
    def change(self):
        self.name = input("Provide a name: ")
        self.stduent_class = input("Provide a student class: ")
        self.age = input("Provide an age: ")
        self.height = input("Provide a height: ")

    # Displaying Details
    def display(self):
        print(self.name)
        print(self.student_class)
        print(self.age)
        print(self.height)

object = Student()
object.change()
object.display()