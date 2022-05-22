import tkinter as tk
from tkinter import ttk
import sqlite3 as sq


def open_dialog():
    Child(root, app)


def open_search_dialog():
    Search()


def open_update_dialog():
    Update()


class Main(tk.Frame):
    """Класс для главного окна"""

    def __init__(self, root):
        super().__init__(root)
        self.refresh_img = None
        self.tree = None
        self.delete_img = None
        self.search_img = None
        self.update_img = None
        self.btn_open_dialog = None
        self.add_img = None
        self.init_main()
        self.db = db
        self.view_records()

    def init_main(self):
        toolbar = tk.Frame(bg='#7c0f0f', bd=4)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.add_img = tk.PhotoImage(file="ad.gif")
        self.btn_open_dialog = tk.Button(toolbar, text='Добавить', command=open_dialog, bg='#3c4ccc', bd=0,
                                         compound=tk.TOP, image=self.add_img, padx=5, pady=2, border='5')
        self.btn_open_dialog.pack(side=tk.LEFT)

        self.update_img = tk.PhotoImage(file="edit.gif")
        btn_edit_dialog = tk.Button(toolbar, text="Редактировать", command=open_update_dialog, bg='#3c4ccc',
                                    bd=0, compound=tk.TOP, image=self.update_img, padx=5, pady=2, border='5')
        btn_edit_dialog.pack(side=tk.LEFT)

        self.delete_img = tk.PhotoImage(file="delete.gif")
        btn_delete = tk.Button(toolbar, text="Удалить запись", command=self.delete_records, bg='#3c4ccc',
                               bd=0, compound=tk.TOP, image=self.delete_img, padx=5, pady=2, border='5')
        btn_delete.pack(side=tk.LEFT)

        self.search_img = tk.PhotoImage(file="search.gif")
        btn_search = tk.Button(toolbar, text="Поиск записи", command=open_search_dialog, bg='#3c4ccc',
                               bd=0, compound=tk.TOP, image=self.search_img, padx=5, pady=2, border='5')
        btn_search.pack(side=tk.LEFT)

        self.refresh_img = tk.PhotoImage(file="reset.gif")
        btn_refresh = tk.Button(toolbar, text="Обновить экран", command=self.view_records, bg='#3c4ccc',
                                bd=0, compound=tk.TOP, image=self.refresh_img, padx=5, pady=2, border='5')
        btn_refresh.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self, columns=('klient', 'sotr', 'srok', 'proс', 'score'), height=15, show='headings')

        self.tree.column('klient', width=120, anchor=tk.CENTER)
        self.tree.column('sotr', width=130, anchor=tk.CENTER)
        self.tree.column('srok', width=120, anchor=tk.CENTER)
        self.tree.column('proс', width=140, anchor=tk.CENTER)
        self.tree.column('score', width=140, anchor=tk.CENTER)

        self.tree.heading('klient', text='Маршрут')
        self.tree.heading('sotr', text='Фамилия водителя')
        self.tree.heading('srok', text='Дата отправления')
        self.tree.heading('proс', text='Дата прибытия')
        self.tree.heading('score', text='Масса')

        self.tree.pack()

    def records(self, klient, sotr, srok, proc, score):
        self.db.insert_data(klient, sotr, srok, proc, score)
        self.view_records()

    def update_record(self, klient, sotr, srok, proc, score):
        self.db.cur.execute(
            "UPDATE vidacha SET klient=?, sotr=?, srok=?, proс=?, score=? WHERE klient=?",
            (klient, sotr, srok, proc, score, self.tree.set(self.tree.selection()[0], '#1')))
        self.db.con.commit()
        self.view_records()

    def view_records(self):
        self.db.cur.execute("SELECT * FROM vidacha")
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def delete_records(self):
        for selection_item in self.tree.selection():
            self.db.cur.execute("DELETE FROM vidacha WHERE klient=?", (self.tree.set(selection_item, '#1'),))
        self.db.con.commit()
        self.view_records()

    def search_records(self, score):
        score = ("%" + score + "%",)
        self.db.cur.execute("SELECT * FROM vidacha WHERE score LIKE ?", score)
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    # def search_records(self, score):
    #     score = (score,)
    #     self.db.cur.execute("""SELECT * FROM vidacha WHERE score>?""", score)
    #     [self.tree.delete(i) for i in self.tree.get_children()]
    #     [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]


class Child(tk.Toplevel):
    """Класс для дочернего окна"""

    def __init__(self, root, app):
        super().__init__(root)
        self.btn_ok = None
        self.entry_proc = None
        self.entry_score = None
        self.entry_srok = None
        self.entry_sotr = None
        self.entry_description = None
        self.init_child()
        self.view = app

    def init_child(self):
        self.title('Добавить')
        self.geometry('400x220+400+300')
        self.resizable(False, False)

        label_description = tk.Label(self, text='Маршрут')
        label_description.place(x=50, y=25)
        self.entry_description = ttk.Entry(self)
        self.entry_description.place(x=150, y=25)

        label_sotr = tk.Label(self, text='Фамилия водителя')
        label_sotr.place(x=50, y=50)
        self.entry_sotr = ttk.Entry(self)
        self.entry_sotr.place(x=150, y=50)

        label_srok = tk.Label(self, text='Дата отправки')
        label_srok.place(x=50, y=75)
        self.entry_srok = ttk.Entry(self)
        self.entry_srok.place(x=150, y=75)

        label_proc = tk.Label(self, text='Дата прибытия')
        label_proc.place(x=50, y=100)
        self.entry_proc = ttk.Entry(self)
        self.entry_proc.place(x=150, y=100)

        label_score = tk.Label(self, text='Масса')
        label_score.place(x=50, y=125)
        self.entry_score = ttk.Entry(self)
        self.entry_score.place(x=150, y=125)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=170)

        self.btn_ok = ttk.Button(self, text='Добавить')
        self.btn_ok.place(x=220, y=170)
        self.btn_ok.bind('<Button-1>', lambda event: self.view.records(self.entry_description.get(),
                                                                       self.entry_sotr.get(),
                                                                       self.entry_srok.get(),
                                                                       self.entry_proc.get(),
                                                                       self.entry_score.get()))

        self.grab_set()
        self.focus_set()


class Update(Child):
    def __init__(self):
        super().__init__(root, app)
        self.init_edit()
        self.view = app

    def init_edit(self):
        self.title("Редактировать запись")
        btn_edit = ttk.Button(self, text="Редактировать")
        btn_edit.place(x=205, y=170)
        btn_edit.bind('<Button-1>', lambda event: self.view.update_record(self.entry_description.get(),
                                                                          self.entry_sotr.get(),
                                                                          self.entry_srok.get(),
                                                                          self.entry_proc.get(),
                                                                          self.entry_score.get()))
        self.btn_ok.destroy()


class Search(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.entry_search = None
        self.init_search()
        self.view = app

    def init_search(self):
        self.title("Поиск")
        self.geometry("300x100+400+300")
        self.resizable(False, False)

        label_search = tk.Label(self, text="Поиск")
        label_search.place(x=50, y=20)

        self.entry_search = ttk.Entry(self)
        self.entry_search.place(x=105, y=20, width=150)

        btn_cancel = ttk.Button(self, text="Закрыть", command=self.destroy)
        btn_cancel.place(x=185, y=50)

        btn_search = ttk.Button(self, text="Поиск")
        btn_search.place(x=105, y=50)
        btn_search.bind('<Button-1>', lambda event: self.view.search_records(self.entry_search.get()))
        btn_search.bind('<Button-1>', lambda event: self.destroy(), add='+')


class DB:
    def __init__(self):
        with sq.connect('vidacha.db') as self.con:
            self.cur = self.con.cursor()
            self.cur.execute("""CREATE TABLE IF NOT EXISTS vidacha(
                klient TEXT,
                sotr TEXT NOT NULL,
                srok INTEGER NOT NULL DEFAULT 1,
                proс INTEGER,
                score INTEGER
                )""")

    def insert_data(self, klient, sotr, srok, proc, score):
        self.cur.execute("INSERT INTO vidacha(klient, sotr, srok, proс, score) VALUES (?, ?, ?, ?, ?)",
                         (klient, sotr, srok, proc, score))
        self.con.commit()


if __name__ == "__main__":
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title("ГРУЗОВЫЕ ПЕРЕВОЗКИ")
    root.geometry("650x450+300+200")
    root.resizable(False, False)
    root.mainloop()
