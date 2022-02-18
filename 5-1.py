i1 = int(input("첫 번째 사람 :"))
i2 = int(input("두 번째 사람 :"))

rule = [1, 2, 3, 1]  # 1, 2, 3 = 가위, 바위, 보

if i1 == i2:
    print("draw")
elif rule[i1 + 1] == i2:
    print("2p win")
elif rule[i2 + 1] == i1:
    print("1p win")
