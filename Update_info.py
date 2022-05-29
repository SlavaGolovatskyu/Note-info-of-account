from tkinter import Toplevel, Entry, messagebox, END

from Phrases import ButtonKeys, Phrases
from helpers.BuildWidget import BuildWidget
from helpers.CustomButton import GenerateCustomButtons

class UpdateInfoOfAccount:
    def __init__(self, parent, collection):
        self.collection = collection
        self.main = parent
        self.width, self.height = 300, 300
        self.root: Toplevel = BuildWidget(parent, title='Email Accounts', width=self.width, height=self.height)

        self.email = Entry(self.root, bg='#0f0505', fg='#ffffff',
                                 width=20, font='Consolas 12', justify='center')

        self.buttons = [
            {
                'text': Phrases.back,
                'bind': self.__back,
            },
            {
                'text': 'Записать аккаунт\nкак \"Использован\"',
                'bind': self.__update_account_info,
            },
        ]

        self.back,
        self.__update_info = GenerateCustomButtons(self.root, self.buttons)

        self.email.bind(ButtonKeys.LEFT_BUTTON_OF_MOUSE, self.deletePlaceHolder)

    def __update_account_info(self):
        self.get_login = self.email.get()

        if not self.get_login:
            messagebox.showerror(Phrases.error, 'Вы не ввели данные.')
            return
        
        if self.collection.count_documents({'login': self.get_login}) == 0:
            messagebox.showerror(Phrases.error, 'Аккаунта с таким логином нету.')
            return

        info = self.collection.find_one({'login': self.get_login})['used']

        if info:
            messagebox.showerror(Phrases.error, 'Данный аккаунт\nуже был записан\nкак \"Использован\"')
            return

        self.collection.update_one({'login': self.get_login}, {'$set': {'used': True}})
        messagebox.showinfo(Phrases.successfully, 'Аккаунт записан как \"Использован\" успешно.')

    def __back(self):
        self.root.destroy()
        self.main.deiconify()

    def deletePlaceHolder(self, event):
        self.email.delete(0, END)

    def run(self):
        self.draw_window()
        self.email.insert(0, 'Логин почты')
        self.root.mainloop()

    def draw_window(self):
        self.email.place(x = self.width / 5, y = 50)
        self.back.place(x = self.width / 3.5, y = 100)
        self.__update_info.place(x = self.width / 3.5, y = 150)
