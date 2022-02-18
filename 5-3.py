def count_1(n):
    if type(n) != "int":
        n = int(n)
    text = ""
    cnt = 0
    for i in range(1, n + 1):
        text += str(i)

        for j in str(i):
            if j == "1":
                cnt += 1
    return(text, str(cnt))


res = count_1(input("input :"))
print(res)
