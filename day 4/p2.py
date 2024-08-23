try:
    n = int(input("Enter a number"))
    if(n<1):
        print("Invalid input")
    elif(n==1):
        print("Neither composite nor prime")
    else:
        f=0
        for i in range(2,n):
            if(n%i==0):
                print("Composite number")
                f=1
                break
        if f==0:
            print("Prime number")
        
except ValueError:
    print("Only positive integer numbers are allowed ")
