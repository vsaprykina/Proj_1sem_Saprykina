# Программа возвращает истину, если хотя бы два числа из трёх равны
while True:
    try:
        a = int(input('Введите первое число: '))
        b = int(input('Введите второе число: '))
        c = int(input('Введите третье число: '))
        break
    except:
        print('Неправильно введены значения. Вводите целые числа')
if a == b:
    print(True)
elif b == c:
    print(True)
elif a == c:
    print(True)
else:
    print(False)