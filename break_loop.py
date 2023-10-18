for i in range(1,4):
    for j in range(1,4):
        print("running i=", i,"j=",j)
        if(i==2 and j==1):
            print("Break inner loop at i=2 and j=1")
            break
