from pymongo import MongoClient
from tkinter import *
from tkinter import messagebox
from random import choice
from PlaceHolder import PlaceHolder

cluster = MongoClient("YOUR CONNECT TO DATABASE (MongoDB)")

db = cluster["testdata"]
collection = db["testcoll"]

ABC = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
numbers = '1234567890'

lengthNameAndPassword = 15

width = 300
height = 300

class WindowGenerator:
    def __init__(self, parent):
        self.main = parent
        self.root = Toplevel(parent)
        self.root.title('Email Accounts')
        self.root.resizable(False, False)
        self.root.geometry(f'{width}x{height}+300+150')
        self.root['bg'] = '#ccc'

        self.__main_entry = Entry(self.root, bg = '#0f0505', fg = '#ffffff',
							      width = 20, font = 'Consolas 12', justify = 'center')

        self.__back_button = Button(self.root, text = 'Назад',
                                    bg = '#0f0505', fg = '#ffffff',
                                    activebackground = '#ffffff', activeforeground = '#0f0505',
                                    width = '15', command = self.__back)
        self.__generate_info = Button(self.root, text = 'Сгенерировать',
                                      bg = '#0f0505', fg = '#ffffff',
                                      activebackground = '#ffffff', activeforeground = '#0f0505',
                                      width = '15', command = self.insert_info)

    def __generate(self):
        randomName = ""
        for j in range(lengthNameAndPassword):
            randomName += choice(ABC + numbers)
        return randomName

    def insert_info(self):
        self.__main_entry.delete(0, END)
        self.__main_entry.insert(0, self.__generate())

    def __back(self):
        self.root.destroy()
        self.main.deiconify()

    def run(self):
        self.__draw_window()
        self.root.mainloop()

    def __draw_window(self):
        self.__main_entry.place(x = width / 5, y = 50)
        self.__back_button.place(x = width / 3.3, y = 100)
        self.__generate_info.place(x = width / 3.3, y = 150)

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


class UnusedAccounts:
    def __init__(self, parent):
        self.main = parent
        self.root = Toplevel(parent)
        self.root.title('Email Accounts')
        self.root.resizable(False, False)
        self.root.geometry(f'{width}x{height}+300+150')
        self.root['bg'] = '#ccc'
        self.textbox = Text(self.root, bg = '#ffffff', fg = '#0f0505', width = '30', height = '14')
        self.__back_button = Button(self.root, text = 'Назад',
                                    bg = '#0f0505', fg = '#ffffff',
                                    activebackground = '#ffffff', activeforeground = '#0f0505',
                                    width = '15', command = self.__back)

    def __back(self):
        self.root.destroy()
        self.main.deiconify()

    def OptionsScroolBar(self):
        scroll = Scrollbar(self.root)
        scroll.pack(side = 'right', fill = 'y')
        scroll['command'] = self.textbox.yview
        self.textbox['yscrollcommand'] = scroll.set

    def insert_all_unused_accounts(self):
        all_unused_accounts = collection.find({'used': False})
        c = collection.count_documents({'used': False})
        if c == 0:
            self.textbox.insert(1.0, 'Нету')
        else:
            for i in all_unused_accounts:
                self.textbox.insert(1.0, '[' + str(c) + '] Логин: ' + i['login'] + '\nПароль: ' + i['password'] + '\n')
                c -= 1

    def run(self):
        self.draw_window()
        self.OptionsScroolBar()
        self.insert_all_unused_accounts()
        self.root.mainloop()

    def draw_window(self):
        self.textbox.place(x = width / 13, y = 25)
        self.__back_button.place(x = width / 3.5, y = 265)


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

class Program:
    def __init__(self):
        self.root = Tk()
        self.root.title('Email Accounts')
        self.root.resizable(False, False)
        self.root.geometry(f'{width}x{height}+300+150')
        self.root['bg'] = '#ccc'

        self.__turning_on_the_generator = Button(self.root, text = 'Генератор',
                                                 bg = '#0f0505', fg = '#ffffff',
                                                 activebackground = '#ffffff', activeforeground = '#0f0505',
                                                 width = '15', command = self.__turn_on_generator)
        self.__add_new_data_of_account = Button(self.root, text = 'Добавление\nНовых аккаунтов',
                                                bg = '#0f0505', fg = '#ffffff',
                                                activebackground = '#ffffff', activeforeground = '#0f0505',
                                                width = '15', height = '2', command = self.__add_new_account)
        self.__window_all_unused_accounts = Button(self.root, text = 'Не использованные\nаккаунты',
                                                   bg = '#0f0505', fg = '#ffffff',
                                                   activebackground = '#ffffff', activeforeground = '#0f0505',
                                                   width = '15', height = '2', command = self.__unused_account)
        self.__update_info = Button(self.root, text = 'Обновить данные\nоб аккаунте',
                                    bg='#0f0505', fg='#ffffff',
                                    activebackground='#ffffff', activeforeground='#0f0505',
                                    width='15', height='2', command = self.__update_info)
        self.__delete_account = Button(self.root, text = 'Удалить аккаунт',
                                       bg='#0f0505', fg='#ffffff',
                                       activebackground='#ffffff', activeforeground='#0f0505',
                                       width='15', height='2', command = self.__delete_account)

    def __delete_account(self):
        self.root.withdraw()
        new_window = DeleteAccountFromBD(self.root)
        new_window.run()

    def __update_info(self):
        self.root.withdraw()
        new_window = UpdateInfoOfAccount(self.root)
        new_window.run()

    def __unused_account(self):
        self.root.withdraw()
        new_window = UnusedAccounts(self.root)
        new_window.run()

    def __add_new_account(self):
        self.root.withdraw()
        self.new_window = AddNewAccounts(self.root)
        self.new_window.run()

    def __turn_on_generator(self):
        self.root.withdraw()
        self.__generator = WindowGenerator(self.root)
        self.__generator.run()

    def run(self):
        self.__draw_window()
        self.root.mainloop()

    def __draw_window(self):
        self.__turning_on_the_generator.place(x = width / 3.5, y = 30)
        self.__add_new_data_of_account.place(x = width / 3.5, y = 75)
        self.__window_all_unused_accounts.place(x = width / 3.5, y = 125)
        self.__update_info.place(x = width / 3.5, y = 175)
        self.__delete_account.place(x = width / 3.5, y = 225)

if __name__ == '__main__':
    launching = Program()
    launching.run()
