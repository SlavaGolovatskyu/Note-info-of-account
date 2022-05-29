from pymongo import MongoClient

from helpers.BuildWidget import BuildWidget
from helpers.CustomButton import GenerateCustomButtons
from DeleteAccountFromBD import DeleteAccountFromBD
from Generator import WindowGenerator
from AddNewAccount import AddNewAccounts
from accounts import Accounts
from Update_info import UpdateInfoOfAccount

cluster = MongoClient("YOUR CONNECT TO THE DATABASE (MongoDB)")

db = cluster["testdata"]
collection = db["testcoll"]

width = 300
height = 300

class Program:
    def __init__(self):
        self.root = BuildWidget(title='Email Accounts')

        self.buttons = [
            {
                'text': 'Генератор',
                'bind': self.__turn_on_generator,
            },
            {
                'text': 'Добавление\nНовых аккаунтов',
                'bind': self.__add_new_account,
            },
            {
                'text': 'Не использованные\nаккаунты',
                'bind': self.__unused_account,
            },
            {
                'text': 'Обновить данные\nоб аккаунте',
                'bind': self.__update_info,
            },
            {
                'text': 'Удалить аккаунт',
                'bind': self.__delete_account,
            },
            {
                'text': 'Использованые\nаккаунты',
                'bind': self.__list_used_accounts,
            },
        ]

        self.__turning_on_the_generator,
        self.__add_new_data_of_account,
        self.__window_all_unused_accounts,
        self.__update_info,
        self.__delete_account,
        self.__list_used_accounts = GenerateCustomButtons(self.root, self.buttons)

    def __list_used_accounts(self):
        self.root.withdraw()
        new_window = Accounts(self.root, is_used=True, collection=collection)
        new_window.run()

    def __unused_account(self):
        self.root.withdraw()
        new_window = Accounts(self.root, is_used=False, collection=collection)
        new_window.run()

    def __delete_account(self):
        self.root.withdraw()
        new_window = DeleteAccountFromBD(self.root, collection=collection)
        new_window.run()

    def __update_info(self):
        self.root.withdraw()
        new_window = UpdateInfoOfAccount(self.root, collection=collection)
        new_window.run()

    def __add_new_account(self):
        self.root.withdraw()
        self.new_window = AddNewAccounts(self.root, collection=collection)
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
