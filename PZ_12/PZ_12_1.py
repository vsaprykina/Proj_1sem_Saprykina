<<<<<<< HEAD
=======
# В соответствии с номером варианта перейти по ссылке на прототип.
# Реализовать его в IDE PyCharm Community с применением пакета tk.
# Получить интерфейс максимально приближенный к оригиналу
>>>>>>> github/master
# В соответствии с номером варианта перейти по ссылке на прототип.
# Реализовать его в IDE PyCharm Community с применением пакета tk.
# Получить интерфейс максимально приближенный к оригиналу
from tkinter import *
from tkinter.font import BOLD
from tkinter.ttk import Combobox
from tkinter.ttk import Checkbutton

root = Tk()
root.geometry('1391x646')
root['bg'] = '#ebecee'
var = IntVar()
Canvas(root, width=950, height=646, bg='#ffffff').place(x=205, y=0)
Label(text='Регистрация', width=10, bg='#FFFFFF', fg='#09f', font='arial 15').place(x=234, y=10)
Label(text='Создание нового сайта', width=60, bg='#09f', fg='#FFFFFF', font='arial 19').place(x=230, y=50)
Label(text='Email', width=10, bg='#FFFFFF', fg='#09c', font=('arial', 13, BOLD)).place(x=450, y=120)
Entry(textvariable=StringVar(value='@gmail.com'), fg='#999', width=27, bd='2', font='arial 15').place(x=544, y=118)
Label(text='Пароль', width=10, bg='#FFFFFF', fg='#09c', font=('arial', 13, BOLD)).place(x=445, y=160)
Entry(textvariable=StringVar(value='********'), fg='#999', width=27, bd='2', font='arial 15').place(x=544, y=158)
Label(text='Имя', width=10, bg='#FFFFFF', fg='#09c', font=('arial', 13, BOLD)).place(x=453, y=200)
Entry(textvariable=StringVar(value='Руслан'), fg='#999', width=27, bd='2', font='arial 15').place(x=544, y=198)
Label(text='Фамилия', width=10, bg='#FFFFFF', fg='#09c', font=('arial', 13, BOLD)).place(x=440, y=240)
Entry(textvariable=StringVar(value='Тертышный'), fg='#999', width=27, bd='2', font='arial 15').place(x=544, y=238)
Label(text='Никнейм', width=10, bg='#FFFFFF', fg='#09c', font=('arial', 13, BOLD)).place(x=440, y=280)
Entry(textvariable=StringVar(value='Tros'), fg='#999', width=27, bd='2', font='arial 15').place(x=544, y=278)
Label(text='Дата рождения', width=13, bg='#FFFFFF', fg='#09c', font=('arial', 13, BOLD)).place(x=400, y=320)
Spinbox(root, from_=0, to=31, width=6).place(x=544, y=323)
Spinbox(root, from_=0, to=12, width=6).place(x=604, y=323)
Spinbox(root, from_=1980, to=2004, width=6).place(x=664, y=323)
Label(text='Пол', width=6, bg='#FFFFFF', fg='#09c', font=('arial', 13, BOLD)).place(x=474, y=360)
Radiobutton(text='Мужчина', bg='white', variable=var, value=1).place(x=544, y=361)
Radiobutton(text='Женщина', bg='white', variable=var, value=2).place(x=644, y=361)
Label(text='Место проживания', width=15, bg='#FFFFFF', fg='#09c', font=('arial', 13, BOLD)).place(x=370, y=400)
combo = Combobox(root, width=40, values=['Другой город', 'Москва', 'Санкт-Петербург', 'Ростов-на-Дону'])
combo.current(0)
combo.place(x=544, y=400)
Label(text='Код безопасности', width=15, bg='#FFFFFF', fg='#09c', font=('arial', 13, BOLD)).place(x=370, y=440)
Entry(fg='#999', width=8, bd='2', font='arial 15').place(x=544, y=440)
chk = BooleanVar()
chk.set(True)
Checkbutton(root, text='Подтверждаю условия использования ulD сообщества', variable=chk).place(x=540, y=480)
Button(text="Регистрация", bg='#09c', fg='white', width=10, font='Arial 13').place(x=540, y=540)
root.mainloop()

