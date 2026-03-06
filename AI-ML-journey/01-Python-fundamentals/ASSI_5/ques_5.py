try:
    with open("data.txt", "r") as f:
        f.read()

except FileNotFoundError:
    print("File not found !")  

else:
    print("Successfully read")    

finally:
    print("Code done !!")          
