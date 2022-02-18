n = list(input("input"))

n_sort = sorted(n)
text = ""

if n_sort == ["1", "2", "3", "4", "5"]:
    print("쌍둥이입니다")
else:
    for i in n_sort:
        if i not in ["1", "2", "3", "4", "5"]:
            text += " " + i

print(f"포합되지않은 숫자는{text}입니다")
