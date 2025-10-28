def Casino(Q,first,second,third,machine):
    times=0
    while Q >= 1:
        quarter= quarter-1

        if machine == 0:
            Q-=1
            machine+=1
            first+=1
        if machine==1:
            Q-=1
            machine+=1
            second+=1
        if machine == 2:
            Q-=1
            machine+=1
            third+=1
            machine+0
        if first==35:
            Q+=35
            first=0
        if second==100:
            Q+=60
            second=0
        if third==10:
            Q+=9
            third=0
Casino(49,3,10,9)

