try:
    n=int(input("Enter no of numbers : "))
    if(n<1):
        print("INVALID INPUT")
    else:
        s=0
        for i in range(0,n):
            num=int(input("Enter number : "))
            s=s+num
        print("SUM =",s)
except:
    print("only integer number allowed")

#sum upto n numbers
