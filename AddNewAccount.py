from tkinter import Toplevel, Tk, Entry, messagebox

from helpers.BuildWidget import BuildWidget
from helpers.CustomButton import GenerateCustomButtons
from Phrases import ButtonKeys, Phrases
from PlaceHolder import PlaceHolder

class AddNewAccounts:
    def __init__(self, parent: Tk, collection):
        self.collection = collection
        self.main = parent
        self.width, self.height = 300, 300
        self.root: Toplevel = BuildWidget(parent, title='Email Accounts', width=self.width, height=self.height)

        self.ph = PlaceHolder('Login', 'Password')

        self.__name_account_entry = Entry(self.root, bg = '#0f0505', fg = '#ffffff',
							              width = 20, font = 'Consolas 12', justify = 'center')

        self.__password_account_entry = Entry(self.root, bg = '#0f0505', fg = '#ffffff',
							                  width = 20, font = 'Consolas 12', justify = 'center')
        
        self.buttons = [
            {
                'text': Phrases.back,
                'bind': self.__back,
            },
            {
                'text': 'Записать данные',
                'bind': self.__add_new_account_in_bd,
            },
        ]

        self.__button_for_back,
        self.__write_data = GenerateCustomButtons(self.root, self.buttons)

        self.__name_account_entry.bind(
            ButtonKeys.LEFT_BUTTON_OF_MOUSE,
            self.LaunchPlaceHolder1,
        )

        self.__password_account_entry.bind(
            ButtonKeys.LEFT_BUTTON_OF_MOUSE,
            self.LaunchPlaceHolder2,
        )

    def LaunchPlaceHolder1(self, event):
        self.ph.DeletePlaceHolder(1, 2, self.__name_account_entry, self.__password_account_entry)

    def LaunchPlaceHolder2(self, event):
        self.ph.DeletePlaceHolder(2, 2, self.__name_account_entry, self.__password_account_entry)

    def __back(self):
        self.root.destroy()
        self.main.deiconify()

    def __add_new_account_in_bd(self):
        EmailName = self.__name_account_entry.get()
        Password = self.__password_account_entry.get()

        if not EmailName or not Password:
            messagebox.showerror('Ошибка', 'Введите все данные.')
            return

        if self.collection.count_documents({'login': EmailName}) != 0:
            messagebox.showerror('Ошибка', 'Данный аккаунт уже записан в базе данных.')
            return

        self.collection.insert_one({'login': EmailName, 'password': Password, 'used': False})
        messagebox.showinfo('Успешно', 'Данные успешно записаны.')

    def insert_info(self):
        self.__name_account_entry.insert(0, 'Login')
        self.__password_account_entry.insert(0, 'Password')

    def run(self):
        self.draw_window()
        self.insert_info()
        self.root.mainloop()

    def draw_window(self):
        self.__name_account_entry.place(x = self.width / 5, y = 50)
        self.__password_account_entry.place(x = self.width / 5, y = 100)
        self.__button_for_back.place(x = self.width / 3.3, y = 150)
        self.__write_data.place(x = self.width / 3.3, y = 200)
