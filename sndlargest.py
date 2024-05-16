
    
li =[2,4,1,6,8,3,54]

lar=3
sl=2

for i in li:
    if i> lar:
        sl=lar
        lar=i
    elif i> sl and i !=lar:
        sl=i
print(sl)
