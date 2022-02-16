def print_reverse(num):
    num = str(num)
    res = ""
    for i in range(len(num)):
        res += num[len(num) - 1 - i]
    print(res)


print_reverse(980135)
