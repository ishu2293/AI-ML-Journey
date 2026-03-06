class student:
    def __init__(self, name, roll_no, marks):
        self.__name = name
        self.__roll_no = roll_no
        self.__matrks = marks
    def setter(self, name, roll_no, marks):
        if (name != ""):
            self.__name = name
        else:
            print("Name cannot be empty")
        if (roll_no>1 and roll_no<100):
            self.__roll_no = roll_no
        else:
            print("Roll_no should be between 1 and 100")
        if (marks > 0):
            self.__marks = marks
        else:
            print("marks cannot be negative")

    def getter(self):
        print(f"{self.__name}\n{self.__roll_no}\n{self.__marks}")

s1 = student("ishwari", 44, 90)
s1.setter("vaishnavi", 58, 80)
s1.getter()
s1.setter("", 101, -9)
