#plot fibbonachi series with divide&conquer and dynamic programming

# for mesuring time
import time
# for plotting
import matplotlib.pyplot as plt 



# divide and conquer function
def fibonacci_dc(n):
    if n <= 1:
        return n
    else:
        return fibonacci_dc(n-1) + fibonacci_dc(n-2)



#dynamic programming function
# Function for nth fibonacci number - Dynamic Programming
# Taking 1st two fibonacci numbers as 0 and 1



def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-2])
    return fib[n]

# Driver Program



# Example usage
#print(fibonacci(6)) # Output: 8


#divide and conquer time and results



#dynamic programming time and results

x=[]
for i in range(35):
    x.append(i+1)




xdp=[]
for i in range(350):
    xdp.append(i+1)


# dynamic programming time 
ydp=[]

#time divide and conquer
ydc=[]

s_time_dc1 = time.time()

for i in range(35):
    start_time_dc = time.time()
    fibonacci_dc(i)
    end_time_dc = time.time()
    ydc.append(end_time_dc - start_time_dc)

e_time_dc1 = time.time()



s_time_dp = time.time()
for i in range(350):
    start_time_dp = time.time()
    fibonacci(i)
    end_time_dp = time.time()
    ydp.append(end_time_dp - start_time_dp)
e_time_dp = time.time()

print("Time taken to solve by dynamic programming:", e_time_dp - s_time_dp, "seconds")

print("Time taken to solve by divide and conquer:", e_time_dc1 - s_time_dc1, "seconds")




#plotting the results

# plotting the points 
plt.plot(x, ydc,color='r', label='D&C') 
plt.plot(xdp, ydp, color='b', label='D.P') 



# naming the x axis 
plt.xlabel('x - axis') 
# naming the y axis 
plt.ylabel('y - axis') 

# giving a title to my graph 
#plt.title('My first graph!') 

# function to show the plot 
plt.show() 
