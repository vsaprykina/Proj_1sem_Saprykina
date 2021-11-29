#Дан список размера N, все элементы которого, кроме последнего, упорядочены по возрастанию.
# Сделать список упорядоченным, переместив последний элемент на новую позицию.
import random
N = []
k = 1
n = input('Введите размер списка: ')
while type(n) != int:
    try:
        n = int(n)
    except ValueError:
        n = input('Это не число!!! Попробуйте снова: ')
for x in range(n):
    N.append(random.randint(0, n))
N.sort()
N.insert(random.randint(0, len(N)), N[-1])
N.pop(-1)
N.sort()
print('Упорядоченный список: ', N)