def pow(n,a):
    if a==0:
        return 1
    else:
        return n*pow(n,a-1)
        
print(pow(2,3))        