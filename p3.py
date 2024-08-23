import math as a
for i in range(1,1001):
    n=int(a.log10(i))+1
    s=0
    copy=i
    while(copy>0):
        s=s+((copy%10)**n)
        copy//=10
    if s==i:
        print(i)

    
