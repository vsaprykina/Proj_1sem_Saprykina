"""
Практическая №10 №1
Средствами языка Python сформировать текстовый файл (.txt), содержайщий последовательность из целых положительных и
отрицательных чисел. Сформировать новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
обработку элементов:
1.Исходные данные:
2.Количество элементов:
3.Сумма элементов:
4.Элементы до n-1 умножены на элемент n:
"""

from random import randint

file_data = []     # генерация содрежимого исходного файла
count = 0
while count < 10:
    file_data.append(str(randint(-10, 10)))
    count += 1


print(",".join(file_data), file=open('file_10_1.txt', 'w'))     # запись содержимого в исходный файл

new_file = open('file_new10_1.txt', 'w')     # новый .txt файл
print('Исходные данные:', open('file_10_1.txt').read(), file=new_file)    # 1
print('Количество элементов:', len(open('file_10_1.txt').read().split(',')), file=new_file)    # 2
print('Сумма элементов:', sum(list(map(int, open('file_10_1.txt').read().split(',')))), file=new_file)    #3


new_file_data = list(map(int, open('file_10_1.txt').read().split(',')))  # получение списка из файла с исходными данными

for n in range(0, len(new_file_data) - 1):           # цикл к 4 пункту + конвертация каждого элемента в строковый тип
    new_file_data[n] = new_file_data[n] * new_file_data[-1]
    new_file_data[n] = str(new_file_data[n])
new_file_data[-1] = str(new_file_data[-1])


print('Элементы до n-1 умножены на элемент n:', ",".join(new_file_data), file = new_file)    # 4

new_file.close()
