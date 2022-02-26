# В последовательности на n целых элементов найти среднее арифметическое элементов первой трети.

#import random

#d = int(input('Введите длину последовательности: '))
#spisok = [random.randint(-10, 10) for i in range(d)]

spisok = [10, 2, 5, 6, 8, -1, 9, 7, 8]
print(spisok)
print(f'Среднее арифметическое первой трети последовательности'
      f': {sum(spisok[:len(spisok) // 3]) / len(spisok[:len(spisok) // 3])}')
