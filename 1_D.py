def sqrt_function(x1: int, x2: int, x3: int):
    if c < 0:
        return "NO SOLUTION"
    elif x1 == 0:
        if x2 == x3*x3:
            return "MANY SOLUTIONS"
        else:
            return "NO SOLUTION"
    elif x2 == 0:
        if (x3*x3) % x1 == 0:
            return int(x3*x3/x1)
        else:
            return "NO SOLUTION"
    elif x3 == 0:
        if (-x2) % x1 == 0:
            return int(-x2/x1)
        else:
            return "NO SOLUTION"
    else:
        if (x3*x3 - x2) % x1 == 0:
            return int((x3*x3 - x2)/x1)
        else:
            return "NO SOLUTION"

if __name__ == "__main__":
    a = int(input())
    b = int(input())
    c = int(input())
    answer = sqrt_function(a, b, c)
    if type(answer) is int:
        if (answer * a + b) >= 0:
            print(answer)
        else:
            print("NO SOLUTION")
    else:
        print(answer)
