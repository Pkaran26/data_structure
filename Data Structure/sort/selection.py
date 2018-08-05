def selection(x):
    m = 0
    for i in range(len(x)):
        for j in range(i,len(x)):
            if x[i] > x[j]:
                m = x[j]
                x[j] = x[i]
                x[i] = m
    print(x)
    return 0

x = [7,2,4,6,1,3,5,9,8]
selection(x)