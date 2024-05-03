import time
import matplotlib.pyplot as plt
#pip install matplotlib

# Top-down (recursive) approach
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

 # Bottom-up (dynamic programming) approach
def fibonacci_bottom_up(n):
    fib = [0] * (n+1)
    fib[1] = 1
    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]

# Task 2: Measure the degree of overlapping subproblem
n_values_2 = list(range(5, 51))
times_f4_computed = []

for n in n_values_2:
    start_time = time.time()
    fibonacci_bottom_up(n)
    end_time = time.time()
    times_f4_computed.append(end_time - start_time)

# Plotting the degree of overlapping subproblem
plt.plot(n_values_2, times_f4_computed)
plt.xlabel('n')
plt.ylabel('Execution Time (s)')
plt.title('Times F(4) Computed for F(5) to F(51)')
plt.show()