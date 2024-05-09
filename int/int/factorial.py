number =int(input("enter a number to find its factorial"))
factorial =1

if number<0 :
    print("factorial is not defined for negative numbers")
elif number== 0 or number==1:
    print("factorial of",number,"is 1")
else :
    for i in range(2,number+1):
        factorial *= i
    print("factorial of",number,"is",factorial)


def facto(num):
    if num==0 or num==1:
        return 1
    else:
        return num * facto(num-1)
    
print(facto(6))

import mymodule
print(mymodule.mult(3,4))