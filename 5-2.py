used_word = []
text = ""
round = 1

while True:
    err = 0
    word = input(f"{round}번째 단어 :")
    if word in used_word:
        print("사용된 단어")
        err = 1

    if round != 1:
        if word[0] != used_word[0][-1]:
            print("잘못된 첫글자")
            err = 1

    if err == 0:
        used_word.insert(0, word)
        text += word
        print(text)
        text += " -> "
        round += 1
