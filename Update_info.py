from pymongo import MongoClient
from tkinter import *
from tkinter import messagebox

cluster = MongoClient("mongodb+srv://slavsup15:s9hVixpgjK1gbFM8@cluster0.hgr2y.mongodb.net/testdata?retryWrites=true&w=majority")

db = cluster["testdata"]
collection = db["testcoll"]

width = 300
height = 300

class UpdateInfoOfAccount:
    def __init__(self, parent):
        self.main = parent
        self.root = Toplevel(parent)
        self.root.title('Email Accounts')
        self.root.resizable(False, False)
        self.root.geometry(f'{width}x{height}+300+150')
        self.root['bg'] = '#ccc'

        self.__EmailName = Entry(self.root, bg='#0f0505', fg='#ffffff',
                                 width=20, font='Consolas 12', justify='center')

        self.__backs = Button(self.root, text = 'Назад',
                             bg = '#0f0505', fg = '#ffffff',
                             activebackground = '#ffffff', activeforeground = '#0f0505',
                             width = '15', command = self.__back)

        self.__update_info = Button(self.root, text = 'Записать аккаунт\nкак \"Использован\"',
                                    bg = '#0f0505', fg = '#ffffff',
                                    activebackground = '#ffffff', activeforeground = '#0f0505',
                                    width = '15', command = self.__update_account_info)

        self.__EmailName.bind('<Button-1>', self.deletePlaceHolder)

    def __update_account_info(self):
        self.get_login = self.__EmailName.get()
        if self.get_login:
            if collection.count_documents({'login': self.get_login}) == 0:
                messagebox.showerror('Ошибка', 'Аккаунта с таким логином нету.')
            else:
                info = collection.find_one({'login': self.get_login})['used']
                if info:
                    messagebox.showerror('Ошибка', 'Данный аккаунт\nуже был записан\nкак \"Использован\"')
                else:
                    collection.update_one({'login': self.get_login}, {'$set': {'used': True}})
                    messagebox.showinfo('Успешно', 'Аккаунт записан как \"Использован\" успешно.')
        else:
            messagebox.showerror('Ошибка', 'Вы не ввели данные.')

    def __back(self):
        self.root.destroy()
        self.main.deiconify()

    def deletePlaceHolder(self, event):
        self.__EmailName.delete(0, END)

    def run(self):
        self.draw_window()
        self.__EmailName.insert(0, 'Логин почты')
        self.root.mainloop()

    def draw_window(self):
        self.__EmailName.place(x = width / 5, y = 50)
        self.__backs.place(x = width / 3.5, y = 100)
        self.__update_info.place(x = width / 3.5, y = 150)