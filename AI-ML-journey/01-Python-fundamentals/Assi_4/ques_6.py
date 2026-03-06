from abc import ABC, abstractmethod
class employee:
    @abstractmethod
    def calculate_salary():
        pass
class intern(employee):
    def calculate_salary(self):
        print("intern salary")
class fullTime(employee):
    def calculate_salary(self):
        print("FullTimeEmployee salary")

i = intern()
i.calculate_salary()
f = fullTime()
f.calculate_salary()