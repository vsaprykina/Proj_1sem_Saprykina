# Дан список размера N, и целые числа К и L(1<K<L<N). Найти сумму элементов списка с номерами от K до L включительно.

from random import randint

n = int(input('Введите размер списка: '))
List = []
a = 0
while a < n: #заполнение списка
    a += 1
    List.append(randint(-10, 10))
print('Ваш список: ', List)

if n < 3:
    print('Сумма элементов списка: ',
sum(List))
else:
    k = randint(2, n)
    I = randint(2, n)
    if k > I:
        k, I = I, k
    print(f'Сумма элементов списка с номерами от {k} до {I} включительно: ',
sum(List[k:I]))







