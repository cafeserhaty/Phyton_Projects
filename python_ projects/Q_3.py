#The func is (x^4) -5*(x^3) -3*(x) + 37
#The integral will be from 0 to 2
#The discretization steps will start at 1 and double 9 times
#The real sum is 54.4
import numpy as np
func = lambda x : (x**4)-5*(x**3)-3*(x)+37
real_sum = 54.4
step = 1
total_sum = 0
start = 0
finish = 2
delta_x = (finish-start)/2
k=0
for i in range(0,10):
    for j in np.linspace(start, finish, num = step):
        total_sum = total_sum + delta_x*((func(start+(k*delta_x))+func(start+((k+1)*delta_x)))/2)
        k=k+1
    print('The sum with ', step, ' steps is ', round(total_sum,5),' and error percentage is ',round((abs(((real_sum-total_sum)/real_sum))*100),5),'%\n')
    total_sum=0
    step=2*step
    delta_x = (finish-start)/step
    k=0







