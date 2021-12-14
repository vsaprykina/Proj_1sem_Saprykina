#Дан целочисленный список размера N. Найти количество различных элементов в данном списке.

from random import randint
dlina_spiska = int(input("Введите длину списка:"))
spisok = []
for i in range(dlina_spiska):
    spisok.append(randint(-10, 10))
print("Список:", end = ' ')
for i in range(dlina_spiska):
	print(spisok[i],end=';')
print()

k = 0
for i in range(dlina_spiska):
	if not spisok[i] in spisok[0:i]:
		k += 1
print(k)

input()
