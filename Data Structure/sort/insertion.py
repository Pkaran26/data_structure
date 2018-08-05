def insertion(x):
    temp = 0
    for i in range(len(x)):
        for j in range(0,i):
            if x[i]<x[j]:
                temp = x[i]
                x[i] = x[j]
                x[j] = temp
    print(x)
    return 0

x = [7,2,4,6,1,3,5,9,8]
insertion(x)