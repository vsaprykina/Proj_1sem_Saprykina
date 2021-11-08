# Дано целое число N(>0). Найти сумму 1^n + 2^n-1+...+ N^14
n = input('Введите число n: ')
while type(n) != int:
    try:
        n = int(n)
    except ValueError:
        print('Введите целое число: ')
        n = input('n: ')
i = 1
s = 0
while 1 <= n:
    m = i**n
    s = s + m
    i+=1
    n-=1
print(s)