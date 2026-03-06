#-------------1
# salary = int(input("Enter the salary: "))
# if (salary<30_000):
#     print(f"Tax rate is: {(5/100)*salary}")
# elif (salary >= 30_000 and salary<=70_000):
#     print(f"Tax rate is: {(15/100)*salary}")
# else:
#     print(f"Tax rate is: {(25/100)*salary}")   

#-----------------2
# def even_no(a, b):
#     while (a<b):
#         if(a%2 == 0):
#             print(a)
#         a +=1

# even_no(5, 20)        


#---------------3
# def digit(n):
#     while(n>0):
#         num = n%10
#         print(num)
#         n = n//10
# digit(312)  
   
#---------------4
# def count(n):
#     cnt = 0
#     while(n>0):
#         n = n//10
#         cnt +=1
#     print(f"Count of numbers is: {cnt}")
# count(3126)    

     
#-----------------5
# def sum(n):
#     sum = 0
#     while(n>0):
#         num = n%10
#         sum +=num
#         n = n//10
#     print(f"Sum is: {sum}")    
# sum(312)


#------------------6
# def divisible():
#     i = 1
#     while(i <= 100):
#         if(i%3 == 0 and i%5 == 0):
#             print(i)
#         i +=1
# divisible()                


#--------------10
# num = 12

# def guess():
#     user_num = int(input("Enter your guessing number: "))
#     if(user_num > num):
#         print("Too high ")
#     elif (user_num < num):
#         print("Too low")
#     elif (user_num == num):
#         print("Correct!")

# guess()  
              

#--------------7
# def num_guess():
#     if(num < 0):
#         print("Negative")
#     if(num > 0):
#         print("Positive")

# while(True):
#     choice = input("Enter your choice: ")
#     if(choice == "quit"):
#         break
#     num = int(input("Enter a number: "))
#     num_guess()

#--------------------8
# a = 8
# b = 2
# ope = "i" 
# match ope:  
#     case "+":  
#         print(f"Addition is: {a + b}")
#     case "-":  
#         print(f"subtraction is: {a - b}")  
#     case "*":  
#         print(f"Multiplication is: {a * b}") 
#     case "/":  
#         print(f"Division is: {a / b}")
#     case _:
#         print("Invalid !!")

#------------------9
def is_prime(n):
    if (n == 2):
        print("True")
    else:
        for i in range(2, n-1):
            if(n%i == 0):
                print("False")
                break
        print("True")
is_prime(7)                        
