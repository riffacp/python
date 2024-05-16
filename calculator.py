def sum(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def multi(a,b):
    print(a*b)
def div(a,b):
    print(a/b)

def calculator():
    a=int(input("enter a number"))
    b=int(input("enter another number"))
    print("1=sum\n2=sub\n3=multi\n4=div")
    c=int(input("enter any  operation"))
    if c==1:
        sum(a,b)
    elif c==2:
        sub(a,b)
    elif c==3:
        multi(a,b)
    elif c==4:
        div(a,b)
    else:
        print('invalid')
    
calculator()
    
    