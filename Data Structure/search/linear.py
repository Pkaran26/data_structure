def linearSearch(x,search):
    for i in range(len(x)):
        if x[i]==search:
            print("Found at ",i)

    if i==len(x):
        print("Not Found")
    return 0

x = [7,4,6,1,3,2,5]
linearSearch(x,2)