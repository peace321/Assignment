import time
import matplotlib.pyplot as plt

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

# Task 1: Measure execution time for F(1) to F(100) using both methods
n_values = list(range(1, 40))
execution_time_recursive = []
execution_time_bottom_up = []

for n in n_values:
    start_time = time.time()
    fibonacci_recursive(n)
    end_time = time.time()
    execution_time_recursive.append(end_time - start_time)

for n in n_values:
    start_time = time.time()
    fibonacci_bottom_up(n)
    end_time = time.time()
    execution_time_bottom_up.append(end_time - start_time)

# Plotting execution time for both methods
plt.plot(n_values, execution_time_recursive, label='Recursive')
plt.plot(n_values, execution_time_bottom_up, label='Bottom-Up')
plt.xlabel('n')
plt.ylabel('Execution Time (s)')
plt.title('Execution Time of Fibonacci Calculation')
plt.legend()
plt.show()