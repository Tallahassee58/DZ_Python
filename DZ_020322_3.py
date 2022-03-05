# e - последняя цифра
# m - предпоследняя цифра
for i in range(1,101,1):
    if i == 100:
        print(i,'процентов')
        continue
    e = i - (i // 10) * 10
    m = (i // 10)
    if m == 1:
        print(i, 'процентов')
        continue
    if e == 1:
        print(i, 'процент')
    else:
        if 1 < e < 5:
            print(i, 'процентa')
        else:
            print(i, 'процентов')


