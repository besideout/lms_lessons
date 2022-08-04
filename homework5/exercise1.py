num = int(input())
counter = 0
while num > 0:
    last = num % 10
    num //= 10
    pre_last = num % 10
    if last == pre_last:
        counter += 1
        num //= 10
if counter > 0:
    print('YES')
else:
    print('NO')