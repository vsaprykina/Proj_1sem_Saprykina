# Дан список размера N, и целые числа К и L(1<K<L<N). Найти сумму элементов списка с номерами от K до L включительно.
import random
n = input('Введите размер списка: ')
while type(n) != int:
    try:
        n = int(n)
    except ValueError:
        n = input('Это не число!!! Попробуйте снова: ')
if n == 1:
    print('Сумму элементов списка с номерами от K до L включительно: ', 1)
elif n == 2:
    N = []
    for x in range(2):
        N.append(random.randint(1, n))
    print('Сумму элементов списка с номерами от K до L включительно: ', sum(N))
elif n>2:
    N = []
    for x in range(n):
        N.append(random.randint(1, n))
    L = random.randrange(1, n)
    while L == 1:
        L = random.randrange(1, n)
    K = random.randrange(1, L)
    summa = 0
    for x in N:
        if K <= x <= L:
            summa += x
        else:
            ...
    print('Сумму элементов списка с номерами от K до L включительно: ', summa)







