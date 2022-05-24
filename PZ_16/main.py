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

    def init_main(self) -> object:
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

        self.tree = ttk.Treeview(self, columns=('route', 'driver', 'start', 'finish', 'weight'), height=15, show='headings')

        self.tree.column('route', width=120, anchor=tk.CENTER)
        self.tree.column('driver', width=130, anchor=tk.CENTER)
        self.tree.column('start', width=120, anchor=tk.CENTER)
        self.tree.column('finish', width=140, anchor=tk.CENTER)
        self.tree.column('weight', width=140, anchor=tk.CENTER)

        self.tree.heading('route', text='Маршрут')
        self.tree.heading('driver', text='Фамилия водителя')
        self.tree.heading('start', text='Дата отправления')
        self.tree.heading('finish', text='Дата прибытия')
        self.tree.heading('weight', text='Масса')

        self.tree.pack()

    def records(self, route, driver, start, finish, weight):
        self.db.insert_data(route, driver, start, finish, weight)
        self.view_records()

    def update_record(self, route, driver, start, finish, weight):
        self.db.cur.execute(
            "UPDATE tagging SET route=?, driver=?, start=?, finish=?, weight=? WHERE route=?",
            (route, driver, start, finish, weight, self.tree.set(self.tree.selection()[0], '#1')))
        self.db.con.commit()
        self.view_records()

    def view_records(self):
        self.db.cur.execute("SELECT * FROM tagging")
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def delete_records(self):
        for selection_item in self.tree.selection():
            self.db.cur.execute("DELETE FROM tagging WHERE route=?", (self.tree.set(selection_item, '#1'),))
        self.db.con.commit()
        self.view_records()

    def search_records(self, weight):
        weight = ("%" + weight + "%",)
        self.db.cur.execute("SELECT * FROM tagging WHERE weight LIKE ?", weight)
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    # def search_records(self, weight):
    #     weight = (weight,)
    #     self.db.cur.execute("""SELECT * FROM tagging WHERE weight>?""", weight)
    #     [self.tree.delete(i) for i in self.tree.get_children()]
    #     [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]


class Child(tk.Toplevel):
    """Класс для дочернего окна"""

    def __init__(self, root, app):
        super().__init__(root)
        self.btn_ok = None
        self.entry_finish = None
        self.entry_weight = None
        self.entry_start = None
        self.entry_driver = None
        self.entry_road = None
        self.init_child()
        self.view = app

    def init_child(self):
        self.title('Добавить')
        self.geometry('400x220+400+300')
        self.resizable(False, False)

        label_road = tk.Label(self, text='Маршрут')
        label_road.place(x=50, y=25)
        self.entry_road = ttk.Entry(self)
        self.entry_road.place(x=150, y=25)

        label_driver = tk.Label(self, text='Фамилия водителя')
        label_driver.place(x=50, y=50)
        self.entry_driver = ttk.Entry(self)
        self.entry_driver.place(x=150, y=50)

        label_start = tk.Label(self, text='Дата отправки')
        label_start.place(x=50, y=75)
        self.entry_start = ttk.Entry(self)
        self.entry_start.place(x=150, y=75)

        label_finish = tk.Label(self, text='Дата прибытия')
        label_finish.place(x=50, y=100)
        self.entry_finish = ttk.Entry(self)
        self.entry_finish.place(x=150, y=100)

        label_weight = tk.Label(self, text='Масса')
        label_weight.place(x=50, y=125)
        self.entry_weight = ttk.Entry(self)
        self.entry_weight.place(x=150, y=125)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=170)

        self.btn_ok = ttk.Button(self, text='Добавить')
        self.btn_ok.place(x=220, y=170)
        self.btn_ok.bind('<Button-1>', lambda event: self.view.records(self.entry_road.get(),
                                                                       self.entry_driver.get(),
                                                                       self.entry_start.get(),
                                                                       self.entry_finish.get(),
                                                                       self.entry_weight.get()))

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
        btn_edit.bind('<Button-1>', lambda event: self.view.update_record(self.entry_road.get(),
                                                                          self.entry_driver.get(),
                                                                          self.entry_start.get(),
                                                                          self.entry_finish.get(),
                                                                          self.entry_weight.get()))
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
        with sq.connect('tagging.db') as self.con:
            self.cur = self.con.cursor()
            self.cur.execute("""CREATE TABLE IF NOT EXISTS tagging(
                route TEXT,
                driver TEXT NOT NULL,
                start INTEGER NOT NULL DEFAULT 1,
                finish INTEGER,
                weight INTEGER
                )""")

    def insert_data(self, route, driver, start, finish, weight):
        self.cur.execute("INSERT INTO tagging(route, driver, start, finish, weight) VALUES (?, ?, ?, ?, ?)",
                         (route, driver, start, finish, weight))
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
