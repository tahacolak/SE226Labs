'''
@author: tahacolak
'''
import math
#Question-1)
def factorial(x):
    if x == 0 or x == 1:
        return 1
    return x * factorial(x - 1)

x = int(input("Enter a number: "))  
print(f"Number {x}'s factorial = {factorial(x)}")

#Question-2)
term = lambda n, x: ((-1) ** n) * (x ** (2 * n + 1)) / factorial(2 * n + 1)

def sine_x(x, n):
    
    x = math.pi/180
    result = sum(term(i, x) for i in range(n))
    return result

x = float(input("Enter x in degrees: "))
n = int(input("Enter number of terms: "))
print(f"sin({x}) ≈ {sine_x(x, n)}")

#Question-3)
harmonic_sum = 0  # Global

def harmonic_recursive(n):
    global harmonic_sum
    if n == 0:
        return
    harmonic_recursive(n - 1)
    harmonic_sum += 1 / n

n = int(input("Enter n: "))
harmonic_recursive(n)
print(f"Harmonic sum H({n}) =", harmonic_sum)
