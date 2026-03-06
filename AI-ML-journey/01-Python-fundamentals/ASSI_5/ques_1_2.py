with open("names.txt", "w") as f:
    f.write("My name is\nIshwari\nI am writing\nCode")

# with open("names.txt", "r") as f:
#     print(f.read())

with open("names.txt", "a") as f:
    f.write("\nprogram run successfully !!")

with open("names.txt", "r") as f:
    print(f.read())    