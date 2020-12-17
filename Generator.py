from pymongo import MongoClient
from tkinter import *
from random import choice

cluster = MongoClient("YOUR CONNECT TO THE DATABASE (MongoDB)")

db = cluster["testdata"]
collection = db["testcoll"]

width = 300
height = 300

ABC = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
numbers = '1234567890'

lengthNameAndPassword = 15

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
