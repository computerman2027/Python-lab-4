try:
    n = int(input("Enter a number : "))
    if(n<1):
        print("INVALID INPUT")
    elif(n==1):
        print("Neither composite nor prime")
    else:
        for i in range(2,n):
            if(n%i==0):
                print("Composite number")
                break
        else:
            print("Prime number")
        
except ValueError:
    print("Error : Only positive integer numbers are allowed ")

#WAP TO FIND WHETHER A NUMBER IS PRIME OR NOT
