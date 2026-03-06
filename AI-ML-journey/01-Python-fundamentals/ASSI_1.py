#---------1
# a = input("Enter your name: ")
# b = input("Enter your age: ")

# print("hell0", a,", you are ", b, "years old!")

#-------------3
# a = int(input("Enter num1: "))
# b = int(input("Enter num2: "))
# c = float(input("Enter num3: "))

# d = float(a + b + c)/3
# print(d)

#------------2
# a = int(input("Enter num 1: "))
# b = int(input("Enter num 2: "))
# print(f"Sum is: {a + b}")
# print(f"Difference is: {a - b}")
# print(f"Product is: {a * b}")
# print(f"Quotient is: {a / b}")

#-------------4
# num = input("Enter a number: ")
# inum = int(num)
# print(f"Num is {inum} Type is: {type(inum)}")
# fnum = float(num)
# print(f"Num is {fnum} Type is: {type(fnum)}")
# print(f"Num is {num} Type is: {type(num)}")

#----------------5
# x = 10 + 3 * 2 ** 2
# print(x)

#-----------------6
# a = int(input("Enter num 1: "))
# b = int(input("Enter num 2: "))

# temp = a
# a = b
# b = temp

# print(f"num 1 is: {a} and num 2 is: {b}")

#----------------7
# temp = input("Enter temperature in celsius: ")
# temp = float(temp)
# fah = (temp * (9/5)) + 32
# print(f"Fahrenhiet temperature is: {fah}")

#--------------8
# rad = int(input("Enter radius: "))
# print(f"Area of circle is: {3.14*rad*rad}")

#------------9
# p = input("Enter principle: ")
# r = input("Enter rate: ")
# t = input("Enter time: ")
# print(f"Simple interest is: {(float(p)*float(r)*float(t))/100}")

#-------------10
num = float(input("Enter a number: "))
inum = int(num)
print(f"Integer part is: {inum}")
print(f"Fractional part is: {round(num-inum, 2)}")
