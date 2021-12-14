# На трех участках выращиваются следующие сельскохозяйственные культуры: картофель, лук, морковь, горох, капуста, редис.
# Определить, какие из этих культур имеются на каждом участке, имеются хотя бы на одном из участков и не имеются ни на
# одном участке
culturi = ["картофель", "лук", "морковь", "горох", "капуста", "редис"]  # создаем список культур

# создаем три списка в которых будем хранить -
uchastokKaz = []  # культуры которые имеются на каждом участке
uchastokOdin = []  # культуры которые имеются хотя бы на одном участке
uchastokNo = []  # культуры которые не имеются ни на одном участке

# создаем три множества с разными культурами
uchastok1 = {"картофель", "горох", "капуста"}
uchastok2 = {"картофель", "лук", "морковь"}
uchastok3 = {"картофель", "капуста"}

for ovosh in culturi:  # проходимся по всем культурам
    kolvo = 0  # задаем колво 0
    if ovosh in uchastok1:  # если такая культура есть в участке1 то -
        kolvo = kolvo + 1  # увеличиваем колво на 1
    if ovosh in uchastok2:  # если такая культура есть в участке2 то -
        kolvo = kolvo + 1  # увеличиваем колво на 1
    if ovosh in uchastok3:  # если такая культура есть в участке3 то -
        kolvo = kolvo + 1  # увеличиваем колво на 1

    if kolvo == 3:  # если колво ровняется 3 - это значит что на всех трех участках есть эта культура и тогда -
        uchastokKaz.append(
            ovosh)  # добавляем эту культуру (ovosh) к списку uchastokKaz (культуры которые имеются на каждом участке)

    if kolvo > 0:  # если колво больше 0 - это значит что хотя бы на одном участке есть эта культура и тогда -
        uchastokOdin.append(
            ovosh)  # добавляем эту культуру (ovosh) к списку uchastokOdin (культуры которые имеются хотя бы на одном
                        # участке)

    if kolvo == 0:  # если колво ровняется 0 - это значит что этой культуры нет нигде и тогда -
        uchastokNo.append(
            ovosh)  # добавляем эту культуру (ovosh) к списку uchastokNo (культуры которые не имеются ни на одном участке)

# выводим получивщиеся списки
print("Культуры которые имеются на каждом участке:")
print(uchastokKaz)

print("Культуры которые имеются хотя бы на одном участке:")
print(uchastokOdin)

print("Культуры которые не имеются ни на одном участке:")
print(uchastokNo)