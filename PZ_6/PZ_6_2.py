#Дан целочисленный список размера N. Найти количество различных элементов в данном списке.

from _ast import For
import random
n = int(input("Введите n: "))
N = []
for i in range (n) :
    N.append(random.randint(1, n))
N.sort()
print(N)

