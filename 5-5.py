n = input("input : ")
rev_n = []
for i in n:
    rev_n.insert(0, i)
rev = ""
for i in rev_n:
    rev += i
res = int(n) + int(rev)

print(res)
