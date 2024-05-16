num=int(input("enter a number"))
temp=num
sum=0
r=str(num)
l=len(r)
while num>0:
    
    rem=num%10
    num=num//10
    sum=sum+(rem**l)
print(sum)
if sum==temp:
    print("your number is an amstrong number")
else:
    print("your number is not an amstrong number")
    
    