# Организовать словарь avto, содержащий 3 ключа (марки авто)
# и списки из трех моделей в качестве значений. Обеспечить отображение вторых моделей по каждому авто, всех моделей словаря.
avto = {
    "lada": ["lada vesta", "lada xray", "lada granta"],
    "renault": ["renault duster", "renault logan", "renault master"],
    "mazda": ["mazda miata", "mazda rx7", "mazda 3 sedan"]
}

print("Вторые модели по каждому авто:")
for cars in avto:
    print(avto[cars][1])

print("\nВсе модели словаря:")
for cars in avto:
    for models in avto[cars]:
        print(models)
