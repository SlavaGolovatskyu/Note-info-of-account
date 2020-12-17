from pymongo import MongoClient
from tkinter import *
from tkinter import messagebox
from PlaceHolder import PlaceHolder


cluster = MongoClient("mongodb+srv://slavsup15:s9hVixpgjK1gbFM8@cluster0.hgr2y.mongodb.net/testdata?retryWrites=true&w=majority")

db = cluster["testdata"]
collection = db["testcoll"]

width = 300
height = 300

class AddNewAccounts:
    def __init__(self, parent):
        self.main = parent
        self.root = Toplevel(parent)
        self.root.title('Email Accounts')
        self.root.resizable(False, False)
        self.root.geometry(f'{width}x{height}+300+150')
        self.root['bg'] = '#ccc'

        self.main_place = PlaceHolder('Login', 'Password')

        self.__name_account_entry = Entry(self.root, bg = '#0f0505', fg = '#ffffff',
							              width = 20, font = 'Consolas 12', justify = 'center')

        self.__password_account_entry = Entry(self.root, bg = '#0f0505', fg = '#ffffff',
							                  width = 20, font = 'Consolas 12', justify = 'center')

        self.__button_for_back = Button(self.root, text = 'Назад',
                                        bg = '#0f0505', fg = '#ffffff',
                                        activebackground = '#ffffff', activeforeground = '#0f0505',
                                        width = '15', height = '2', command = self.__back)

        self.__write_data = Button(self.root, text = 'Записать данные',
                                   bg = '#0f0505', fg = '#ffffff',
                                   activebackground = '#ffffff', activeforeground = '#0f0505',
                                   width = '15', height = '2', command = self.__add_new_account_in_bd)

        self.__name_account_entry.bind('<Button-1>', self.LaunchPlaceHolder1)
        self.__password_account_entry.bind('<Button-1>', self.LaunchPlaceHolder2)

    def LaunchPlaceHolder1(self, event):
        self.main_place.DeletePlaceHolder(1, 2, self.__name_account_entry, self.__password_account_entry)

    def LaunchPlaceHolder2(self, event):
        self.main_place.DeletePlaceHolder(2, 2, self.__name_account_entry, self.__password_account_entry)

    def __back(self):
        self.root.destroy()
        self.main.deiconify()

    def __add_new_account_in_bd(self):
        EmailName = self.__name_account_entry.get()
        Password = self.__password_account_entry.get()
        if EmailName and Password:
            if collection.count_documents({'login': EmailName}) == 0:
                collection.insert_one({'login': EmailName, 'password': Password, 'used': False})
                messagebox.showinfo('Успешно', 'Данные успешно записаны.')
            else:
                messagebox.showerror('Ошибка', 'Данный аккаунт уже записан в базе данных.')
        else:
            messagebox.showerror('Ошибка', 'Введите все данные.')

    def insert_info(self):
        self.__name_account_entry.insert(0, 'Login')
        self.__password_account_entry.insert(0, 'Password')

    def run(self):
        self.draw_window()
        self.insert_info()
        self.root.mainloop()

    def draw_window(self):
        self.__name_account_entry.place(x = width / 5, y = 50)
        self.__password_account_entry.place(x = width / 5, y = 100)
        self.__button_for_back.place(x = width / 3.3, y = 150)
        self.__write_data.place(x = width / 3.3, y = 200)