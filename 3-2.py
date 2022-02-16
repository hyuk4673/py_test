from turtle import clear


def gcd(x, y):
    for i in range(1, min(x, y)+1):
        if (x % i == 0) & (y % i == 0):
            res = i
    return(res)


print(gcd(50, 70))
