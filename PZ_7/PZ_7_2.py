#Дана строка, состоящая из русских слов, набранных заглавными буквами и разделенных пробелами (одним или несколькими).
#Преобразовать каждое слово в строке, заменив в нем все предыдущие вхождения его последней буквы на символ «.» (точка).
string = input('Введите строку символов: ')

word_list = string.split()

for i in range(0, len(word_list)):
    a = 0
    word = word_list[i]
    end_word = word[-1]
    while a < len(word):
        if word[a] == end_word:
            new_word = word.replace(word[a], '.')
        a += 1
print(new_word)