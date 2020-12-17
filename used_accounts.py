from pymongo import MongoClient
from tkinter import *

cluster = MongoClient("mongodb+srv://slavsup15:s9hVixpgjK1gbFM8@cluster0.hgr2y.mongodb.net/testdata?retryWrites=true&w=majority")

db = cluster["testdata"]
collection = db["testcoll"]

width = 300
height = 300

class UsedAccounts:
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
        all_unused_accounts = collection.find({'used': True})
        c = collection.count_documents({'used': True})
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