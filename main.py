from pymongo import MongoClient
from tkinter import *
from DeleteAccountFromBD import DeleteAccountFromBD
from Generator import WindowGenerator
from AddNewAccount import AddNewAccounts
from unusedaccounts import UnusedAccounts
from Update_info import UpdateInfoOfAccount
from used_accounts import UsedAccounts

cluster = MongoClient("YOUR CONNECT TO THE DATABASE (MongoDB)")

db = cluster["testdata"]
collection = db["testcoll"]

width = 300
height = 300

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
        self.__list_used_accounts = Button(self.root, text='Использованые\nаккаунты',
                                           bg='#0f0505', fg='#ffffff',
                                           activebackground='#ffffff', activeforeground='#0f0505',
                                           width='15', height='2', command=self.__list_used_accounts)

    def __list_used_accounts(self):
        self.root.withdraw()
        new_window = UsedAccounts(self.root)
        new_window.run()

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
        self.__turning_on_the_generator.place(x = width / 3.5, y = 20)
        self.__add_new_data_of_account.place(x = width / 3.5, y = 65)
        self.__window_all_unused_accounts.place(x = width / 3.5, y = 110)
        self.__list_used_accounts.place(x = width / 3.5, y = 155)
        self.__update_info.place(x = width / 3.5, y = 200)
        self.__delete_account.place(x = width / 3.5, y = 245)

if __name__ == '__main__':
    launching = Program()
    launching.run()











#collection.insert_one({'name': 'john', 'password': '5454'})
#collection.update_one({'name': 'john'}, {"$set": {'password': 543654}})
#password = collection.find_one({'name': 'john'})['password']
#collection.delete_one({'name': 'john'})

