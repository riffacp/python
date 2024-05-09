import random
a=int(input("enter limit: "))
character="ehonlhp0329@#*!-"
password=""
for i in range(0,a):
    password+=random.choice(character)
print(password)