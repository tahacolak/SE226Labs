def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return x / y if y != 0 else "Error"
def power(x, y): return x ** y
def mod(x, y): return x % y

if __name__ == "__main__":
    print(add(2, 3), divide(5, 0))
