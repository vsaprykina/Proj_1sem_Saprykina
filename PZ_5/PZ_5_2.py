# Описать функцию ShiftLeft3(A, B, C), выполняющую левый циклический сдвиг значение A переходит в C, значение C — в B,
# значение B — в A (A, B, C) — вещественные
# параметры, являющиеся одновременно входными и выходными). С помощью этой функции
# выполнить левый циклический сдвиг для двух данных наборов из трех чисел: (A1, B1, C1) и (A2, B2, C2)
def ShiftLeft3(a, b, c):
    a, b, c = b, c, a
    return a, b, c


print('Первый набор чисел')
a1 = float(input('Введите первое число '))
b1 = float(input('Введите второе число '))
c1 = float(input('Введите третье число '))

print('Результат сдвига: ', ShiftLeft3(a1, b1, c1))

print('Второй набор чисел')
a2 = float(input('Введите первое число '))
b2 = float(input('Введите второе число '))
c2 = float(input('Введите третье число '))

print('Результат сдвига: ', ShiftLeft3(a2, b2, c2))