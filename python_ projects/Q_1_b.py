K=[2,3.14,[2,'Alice'],2-3j]
A=(K[2][0]==K[0])
B=((K[2][0]==K[0])and((int(abs(K[3])))+1==K[0]))
C=(K[2][1]==int)
if A==1 and B==1 and C==1:
    print('All of the conditions are True')
elif A==1 and B==1 and C==0:
    print('3 is False , the rest is True')
elif A==1 and B==0 and C==1:
    print('2 is False , the rest is True')
elif A==1 and B==0 and C==0:
    print('1 is True , the rest is False')
elif A==0 and B==1 and C==1:
    print('1 is False , the rest is True')
elif A==0 and B==1 and C==0:
    print('2 is True , the rest is False')
elif A==0 and B==0 and C==1:
    print('3 is True , the rest is False')
else:
    print('All of the condutions are False')
    

