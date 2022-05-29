import random

from tkinter import Toplevel, Entry, END

from Phrases import Phrases
from helpers.BuildWidget import BuildWidget
from helpers.CustomButton import GenerateCustomButtons

ABC = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
numbers = '1234567890'

lengthNameAndPassword = 15

class WindowGenerator:
    def __init__(self, parent):
        self.main = parent
        self.width, self.height = 300, 300
        self.root: Toplevel = BuildWidget(parent, title='Email Accounts', width=self.width, height=self.height)

        self.__main_entry = Entry(self.root, bg = '#0f0505', fg = '#ffffff',
							      width = 20, font = 'Consolas 12', justify = 'center')

        self.buttons = [
            {
                'text': Phrases.back,
                'bind': self.__back,
            },
            {
                'text': 'Сгенерировать',
                'bind': self.insert_info,
            },
        ]

        self.__back_button,
        self.__generate_info = GenerateCustomButtons(self.root, self.buttons)

    def __generate(self):
        return "".join(random.sample(ABC + numbers, lengthNameAndPassword))

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
        self.__main_entry.place(x = self.width / 5, y = 50)
        self.__back_button.place(x = self.width / 3.3, y = 100)
        self.__generate_info.place(x = self.width / 3.3, y = 150)
