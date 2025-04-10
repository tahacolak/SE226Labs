import math_utils

if __name__ == "__main__":
    ops = {
        '+': math_utils.add,
        '-': math_utils.subtract,
        '*': math_utils.multiply,
        '/': math_utils.divide,
        '**': math_utils.power,
        '%': math_utils.mod
    }
    try:
        x = float(input("x: "))
        y = float(input("y: "))
        op = input("Op: ")
        if op in ops:
            print("Result:", ops[op](x, y))
        else:
            print("Invalid op")
    except:
        print("Input error")
