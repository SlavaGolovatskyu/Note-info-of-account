from pymongo import MongoClient
from tkinter import *
from tkinter import messagebox

cluster = MongoClient("YOUR CONNECT TO THE DATABASE (MongoDB)")

db = cluster["testdata"]
collection = db["testcoll"]

width = 300
height = 300

class DeleteAccountFromBD:
    def __init__(self, parent):
        self.main = parent
        self.root = Toplevel(parent)
        self.root.title('Email Accounts')
        self.root.resizable(False, False)
        self.root.geometry(f'{width}x{height}+300+150')
        self.root['bg'] = '#ccc'

        self.__EmailName = Entry(self.root, bg='#0f0505', fg='#ffffff',
                                 width=20, font='Consolas 12', justify='center')

        self.__backs = Button(self.root, text='Назад',
                              bg='#0f0505', fg='#ffffff',
                              activebackground='#ffffff', activeforeground='#0f0505',
                              width='15', command=self.__back)

        self.__delete_info = Button(self.root, text='Удалить аккаунт\nиз базы данных.',
                                    bg='#0f0505', fg='#ffffff',
                                    activebackground='#ffffff', activeforeground='#0f0505',
                                    width='15', command=self.__delete_account_info)

        self.__EmailName.bind('<Button-1>', self.deletePlaceHolder)

    def deletePlaceHolder(self, event):
        self.__EmailName.delete(0, END)

    def __delete_account_info(self):
        self.get_login = self.__EmailName.get()
        if self.get_login:
            if collection.count_documents({'login': self.get_login}) == 0:
                messagebox.showerror('Ошибка', 'Аккаунта с таким логином нету.')
            else:
                collection.delete_one({'login': self.get_login})
                messagebox.showinfo('Успешно', 'Аккаунт удален из базы данных.')
        else:
            messagebox.showerror('Ошибка', 'Вы не ввели данные.')

    def __back(self):
        self.root.destroy()
        self.main.deiconify()

    def run(self):
        self.draw_window()
        self.__EmailName.insert(0, 'Логин аккаунта')
        self.root.mainloop()

    def draw_window(self):
        self.__EmailName.place(x=width / 5, y=50)
        self.__backs.place(x=width / 3.5, y=100)
        self.__delete_info.place(x=width / 3.5, y=150)
