total=0
count=0
avg=0
n=0
while True:
    try:
        st=input("Enter number : ")
        if(st=="done"):
            print("total = ",total)
            print("count = ",count)
            print("average = ",avg)
        else:
            n=int(st)
    except:
        print("Only integer number accepted")
    else:
        total+=n
        count+=1
        avg=total/count
