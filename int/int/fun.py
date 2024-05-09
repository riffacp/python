# def function1name(name):
#     print("hellooo" +name)
    
# function1name("nyna")    

# def function1name(num1,num2):
#     a=num1+num2
#     print("sum is ",a)
    
# function1name(8,2)    


# def function1name(num):
#     a=num*num
#     print("sq of num=",a)
    
# function1name(14)    

# def multi(a,b):
#     for i in range(1,b):
#         c=i*a
#         print(f'{i}*{a}={c}')
        
# multi(3,5)
    
# def feb(a,b,num):
#     print(a) 
#     print(b) 
#     for i in range(2,num+1):
#         c=a+b
#         a=b
#         b=c
#         print(c)    
        
# feb(0,1,12)

def fact(num):
    v=0
    i=0  
    while i<num :
        a=num*num-1
        v=v+a
        num-=1
        print(v)
        
        
fact(4) 
    