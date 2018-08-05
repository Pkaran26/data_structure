def bubble(x): 
    temp = 0   
    for i in range(len(x)-1,0,-1):
        for j in range(i,-1,-1):
            if x[i] < x[j]:
                temp = x[i]
                x[i] = x[j]
                x[j] = temp
    print(x)
    return 0

x = [50,102,68,75,25,5,1,3,15,20,10,21,23,48]
bubble(x)