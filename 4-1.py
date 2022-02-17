import random


def Check_Num(n):
    if n > N:
        return("down")
    elif n < N:
        return("up")
    else:
        return("success")


N = random.randint(1, 100)
while True:
    n = int(input("수 입력 :"))
    res = Check_Num(n)
    print(res)
    if res == "success":
        break
