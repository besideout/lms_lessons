N = int(input())
num = 10
for i in range(1, N + 1):
    if i == num:
        num *= 10
    if (i * i) % num == i:
        print(i)
