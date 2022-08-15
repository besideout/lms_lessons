spisok = [int(i) for i in input().split()]
k = int(input())
for i in range(k + 1, len(spisok)):
    spisok[i - 1] = spisok[i]
spisok.pop()
print(' '.join([str(i) for i in spisok]))