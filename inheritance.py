class Parent():
    def __init__(self, last_name, eye_color):
        print("Parent Constructor called")
        self.last_name = last_name
        self.eye_color = eye_color

class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print("Child Constructor called")
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys

billy_cyrus = Parent("Cyrus","Blue")
print(billy_cyrus.eye_color)

ben_cyrus = Child("Cyrus","Blue",10)
miley_cyrus = Child("Cyrus","Blue",12)
print(ben_cyrus.number_of_toys)
