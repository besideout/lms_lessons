a = int(input())
summa = 0
counter, srednee = 0, 0
maxim = a
minim = a
parne = 0
neparne = 0
while a != 0:
    counter += 1
    summa += a
    srednee = summa + counter
    if a > maxim:
        maxim = a
    if a < minim:
        minim = a
    if a % 2 == 0:
        parne += 1
    if a % 2 != 0:
        neparne += 1
    a = int(input())
print('Сума чисел:', summa)
print('Середнє арифметичне усіх введених чисел:', srednee)
print(f'Mаксимальне і мінімальне значення: {maxim}, {minim}')
print(f'Кількість парних та кількість не парних чисел: {parne}, {neparne}')
