from tkinter import Toplevel, Entry, messagebox, END

from Phrases import Phrases
from helpers.BuildWidget import BuildWidget
from helpers.CustomButton import GenerateCustomButtons

class DeleteAccountFromBD:
    def __init__(self, parent, collection):
        self.collection = collection
        self.main = parent
        self.width, self.height = 300, 300
        self.root: Toplevel = BuildWidget(parent, title='Email Accounts', width=self.width, height=self.height)

        self.__EmailName = Entry(self.root, bg='#0f0505', fg='#ffffff',
                                 width=20, font='Consolas 12', justify='center')

        self.buttons = [
            {
                'text': Phrases.back,
                'bind': self.__back,
            },
            {
                'text': 'Удалить аккаунт\nиз базы данных.',
                'bind': self.__delete_account_info,
            },
        ]

        self.back,
        self.__delete_info = GenerateCustomButtons(self.root, self.buttons)

        self.__EmailName.bind('<Button-1>', self.deletePlaceHolder)

    def deletePlaceHolder(self, event):
        self.__EmailName.delete(0, END)

    def __delete_account_info(self):
        self.get_login = self.__EmailName.get()

        if not self.get_login:
            messagebox.showerror(Phrases.error, 'Вы не ввели данные.')
            return
        
        if self.collection.count_documents({'login': self.get_login}) == 0:
            messagebox.showerror(Phrases.error, 'Аккаунта с таким логином нету.')
            return

        self.collection.delete_one({'login': self.get_login})
        messagebox.showinfo(Phrases.successfully, 'Аккаунт удален из базы данных.')

    def __back(self):
        self.root.destroy()
        self.main.deiconify()

    def run(self):
        self.draw_window()
        self.__EmailName.insert(0, 'Логин аккаунта')
        self.root.mainloop()

    def draw_window(self):
        self.__EmailName.place(x=self.width / 5, y=50)
        self.back.place(x=self.width / 3.5, y=100)
        self.__delete_info.place(x=self.width / 3.5, y=150)
