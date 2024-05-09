#multiplication table
a=int(input("enter a number"))
b=int(input("enter a limit"))
for i in range(1,b+1):
    c=i*a
    print(f'{i}*{a}={c}')