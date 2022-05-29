from tkinter import Text, Scrollbar, Toplevel, Tk

from helpers.BuildWidget import BuildWidget
from helpers.CustomButton import CustomButton
from Phrases import Phrases

class Accounts:
    def __init__(self, parent: Tk, is_used: bool, collection):
        self.collection = collection
        self.is_used = is_used
        self.main = parent
        self.width, self.height = 300, 300
        self.root: Toplevel = BuildWidget(parent, title='Email Accounts', width=self.width, height=self.height)

        self.textbox = Text(self.root, bg = '#ffffff', fg = '#0f0505', width = '30', height = '14')
        self.__back_button = CustomButton(
            self.root,
            text=Phrases.back,
            bind=self.__back,
        )

    def __back(self):
        self.root.destroy()
        self.main.deiconify()

    def OptionsScrollBar(self):
        scroll = Scrollbar(self.root)
        scroll.pack(side = 'right', fill = 'y')
        scroll['command'] = self.textbox.yview
        self.textbox['yscrollcommand'] = scroll.set

    def insert_all_accounts(self):
        all_accounts = self.collection.find({'used': self.is_used})
        c = self.collection.count_documents({'used': self.is_used})

        if c == 0:
            self.textbox.insert(1.0, Phrases.not_found)
            return

        for i in all_accounts:
            self.textbox.insert(1.0, '[' + str(c) + '] Логин: ' + i['login'] + '\nПароль: ' + i['password'] + '\n')
            c -= 1

    def run(self):
        self.draw_window()
        self.OptionsScrollBar()
        self.insert_all_accounts()
        self.root.mainloop()

    def draw_window(self):
        self.textbox.place(x = self.width / 13, y = 25)
        self.__back_button.place(x = self.width / 3.5, y = 265)
