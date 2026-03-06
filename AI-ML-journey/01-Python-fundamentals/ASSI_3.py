#-------------1
# name = input("Enter a string: ")
# i = 0
# j = len(name)-1
# while (i  < j):
#     if name[i] != name[j]:
#         print("False")
#         break
#     i += 1
#     j -= 1
# else:
#     print("True")
         
    

#---------2
# num = [2, 4, 6, 7, 8]
# sum = 0
# for i in num:
#     sum += i

# print(sum/len(num))  
  

#--------------3
# list1 = []
# list2 = []

# print("List1 elements")
# for i in range(0, 3, 1):
#     num = int(input("Enter a number: "))
#     list1.append(num)

# print("List2 elements")
# for j in range(0, 3, 1):
#     num2 = int(input("Enter a number: "))
#     list2.append(num2)

# for k in list2:
#     list1.append(k)

# list1.sort()
# print(list1)


#-----------4
# tup = (1, 2, 3, 4, 5, 6, 7, 8)
# even = []
# odd = []

# for i in tup:
#     if(i%2 == 0):
#         even.append(i)
#     else:
#         odd.append(i)

# print("Even numbers:")
# print(even)
# print("odd numbers:")
# print(odd)               

#---------------5
# student = {
#     "Ishwari": 90,
#     "pranita": 70,
#     "saee": 76,
#     "vaishnavi": 85
# }
# print("Choose\nA: Add a student\nB: Update marks\nC: Search for a student\nD: Display all students and marks" )
# ch = input("Enter option: ").upper()
# match ch:
#     case "A":
#         key = input("Enter student: ")
#         value = int(input("Enter marks: "))
#         student[key] = value
#         print(student)
#     case "B":
#         key = input("Enter student you want to update: ")
#         if key in student:
#             value = int(input("Enter new marks: "))
#             student[key] = value
#             print("Updated:", student)
#         else:
#             print("Student not found")
#     case "C":
#         key = input("Enter student you want to search: ")
#         if key in student:
#             print(f"Student found, marks = {student[key]}")
#         else:
#             print("Student not found")
#     case "D":
#         print(student.items())
#     case _:
#         print("Invalid")

#-------------6
# words = ["apple", "banana", "kiwi", "cherry", "mango"]
# count = {}
# for ch in words:
#     fruit_len = len(ch)
#     count[ch] = fruit_len
# print(count)    


#-------------------7
# sentence = input("Enter a string: ")
# count = 0
# for ch in sentence:
#     if(ch == " "):
#         count +=1
# print(count)        


#----------------8
# list1 = {1, 2, 3, 4}
# list2 = {5, 6, 4, 8}
# if(list1.intersection(list2)):
#     print("Has common element")
# else:
#     print("No common element")

#---------------9
# list = [1, 2, 4, 4, 5, 2, 7, 1]
# seen = set()
# duplicate = set()
# for ch in list:
#     if ch in seen:
#         duplicate.add(ch)
#     else:
#         seen.add(ch)
# print(f"Duplicates are: {duplicate}") 


#----------------10
words = input("Enter a string: ")
seen = set()
duplicate = set()
for ch in words:
    if ch in seen:
        duplicate.add(ch)
    else:
        seen.add(ch)
print(f"unique characters are: {seen}")
count = 0
for i in seen:
    count +=1
print(f"count of unique character is: {count}")
