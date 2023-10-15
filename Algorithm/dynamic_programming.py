# for mesuring time
import time
# for plotting
import matplotlib.pyplot as plt 




def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-2])
    return fib[n]

xdp=[]
for i in range(350):
    xdp.append(i+1)


ydp=[]


for i in range(350):
    start_time_dp = time.time()
    fibonacci(i)
    end_time_dp = time.time()
    ydp.append(end_time_dp - start_time_dp)





plt.plot(xdp, ydp, color='b', label='D.P') 
plt.show() 
