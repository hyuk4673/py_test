import random

answer = []
while len(answer) < 3:
    temp = random.randint(1, 9)
    if temp not in answer:
        answer.append(temp)

round = 0
while True:
    round += 1
    print(f"round {round}")
    strike = 0
    ball = 0
    for i in range(3):
        user = int(input(f"{i+1}번째 수"))
        if user == answer[i]:
            strike += 1
        elif user in answer:
            ball += 1
    if (strike == 0) & (ball == 0):
        print("out")
    else:
        print(f"strike : {strike}, ball : {ball}")

    if strike == 3:
        print("win")
        break
    if round == 9:
        print("lose")
        break
