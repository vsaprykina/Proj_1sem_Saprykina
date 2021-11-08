# Дано вещественное число X и целое число N (>0). Найдите значение выражения X - X^3/(3!) + X^5/(5!) - ...
# ... + (-1)^N - X^2-N+1/((2-N+1)!) (N! = 12 ... N). Полученное число является приближённым значением функции
# sin в точке X.
x = float(input("введите вещественное число x: "))
while type(x) != float:
    try:
        x = float(x)
    except ValueError:
        print('Введите вещественное число: ')
        x = input('x: ')
n = int(input("введите целое число n: "))
while type(n) != int:
    try:
        n = int(n)
    except ValueError:
        print('Введите целое число: ')
        n = input('n: ')
i = 1
v = 3
fact = 1
sin = 0
g = 3
k = 1
while i <= n:
    while k <= g:
        fact *= k
        k += 1
    g += 2
    m = x**v / fact
    if i % 2 == 1:
        sin = sin + m
    else:
        sin = sin - m
    i += 1
    v += 2
    d = x - sin
print('Приближённое значение функции sin в точке x: ', d)


