#Дан целочисленный список размера N. Найти количество различных элементов в данном списке.

from random import randint


n = int(input('Введите количество элементов: '))
List = []

count = 0  # заполнение списка
while count < n:
    count += 1
    List.append(randint(0, 2))

print(List)

List_unic = []  # Список для элементов без повтора

for element in List:
    if List.count(element) == 1:
        List_unic.append(element)

print('Количество уникальных элементов: ',
      len(List_unic))

