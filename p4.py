print("Prime numbers from 1 to 100 are : ")
for i in range(1,101):
    j=2
    f=0
    if i==1:
        continue
    while(j<i):
        if(i%j==0):
            f=1
            break
        j+=1
    else:
        print(i,end=" ")
    
        
#wap to print prime numbers for a range of 1 to 100
