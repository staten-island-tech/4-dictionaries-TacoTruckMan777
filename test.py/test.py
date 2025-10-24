def Casino(Q,first,second,third):
    times=0
    count_1=1
    count_2=0
    count_3=0
    while Q >= 1:
        if count_1 == 1:
            Q -= 1
            first += 1
            count_1 += 1
            count_2 +=1
            times += 1
        if count_2 == 1:
            Q -= 1
            second += 1
            count_2 +=1
            count_3=1
            times += 1
        if count_3 == 1:
            Q -= 1
            third += 1
            count_3=0
            count_1=1
            times += 1
        if first == 35:
            Q += 30
            first == 0
        if second == 100:
            Q += 60
            second == 0
        if third == 10:
            Q += 9
            third == 0
        if Q <= 0:
            for i in range(1):
                print(times)
Casino(48,3,10,4)