import math
def counts(a, b, sign):
    if sign == "+":
        return a + b
    elif sign == "-":
        return a - b
    elif sign == "*":
        return a * b
    elif sign == "/":
        return a / b
    elif sign == "**":
        return a ** b
    elif sign == "!":
        return math.factorial(a)
    elif sign == "Корень":
        return math.sqrt(a)


def counts2(a):
    number1 = int(a.split(" ")[0])
    sign = a.split(" ")[1]
    number2 = int(a.split(" ")[2])

    return counts(number1, number2, sign)


def counts3(a):
    g = a.split(" ")

    res = int(g[0])

    for i, j in enumerate(g):
        if (i + 1) % 2 == 0:
            res = counts(res, int(g[i + 1]), j)


    return res