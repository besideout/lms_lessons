year = int(input())
if not 1900 < year < 1000000:
    print(year, '- цей рік не відповідає умовам')
elif year % 4 != 0:
    print(year, 'не високосний')
elif year % 100 == 0:
    if year % 400 == 0:
        print(year, 'високосний')
    else:
        print(year, 'не високосний')
else:
    print('високосний')

