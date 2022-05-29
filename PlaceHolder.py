from tkinter import *

__author__ = 'SlavaGolovatskyu'
__version__ = 'V1.1'


"""
При создания класса тоисть
PlaceHold = PlaceHolder(arg1, arg2, arg3) нужно передать все строки тоисть 3 строки и больше.
"""

class PlaceHolder:
	def __init__(self, arg1, arg2 = None, arg3 = None, arg4 = None):

		self.MainDict = {
			1: arg1,  # Строка которую вы хотите впихнуть в первый Entry
			2: arg2,  # Строка которую вы хотите впихнуть во второй Entry и т.д
			3: arg3,
			4: arg4
		}

	""" number это цифра Entry сперва биндите Entry на клик. После чего этой функцие передаете номер Entry
	    Допустим enter.bind('<Button-1>', giveNumber)
	    def giveNumber(event):
	        DeletePlaceHolder(1, 2) 1 аргумент это номер Entry 2 аргумент количество всех Entry's
	        3, 4 аргументы обьязательны это переменые самих Entry's Тоисть создали вы например такую переменую:
	        enter = Entry() в 3 аргумент данной функции передаете эту переменую и следующие
	НА ДАННЫЙ МОМЕНТ ФУНКЦИЯ РАБОТАЕТ НОРМАЛЬНО ВСЕГОЛИШ С 3 АРГУМЕНТАМИ 4 и больше неработают. 
	"""

	def DeletePlaceHolder(self, number, CountEnter, enter, enter_2 = None, enter_3 = None, enter_4 = None):
		# Делаем генератор списка. С проверкой. Если i не равно numb добавляем елемент. В ином случае пропускаем.
		array = [i for i in range(1, CountEnter + 1) if i != number]

		MainEnter = enter if number == 1 else enter_2 if number == 2 else enter_3
		SecondEnter = enter if array[0] == 1 else enter_2

		ThreeEnter = True
		DictForCheck = {}

		if CountEnter == 1:
			MainEnter.delete(0, END)
			return
		# Если Entry 2 шт. Код делает следующее...
		if CountEnter == 2:
			# Добавляем главное число в список которое передали в нашу функцию.
			array.append(number)
			DictForCheck = {
				array[0]: SecondEnter.get(),
				# После того как добавили число в список появился елемент с идексом 1
				array[1]: MainEnter.get()
			}
		else:
			# Как и было сказано раньше если код заходит в проверку. Некоторые переменые меняют свое значение.
			ThreeEnter = enter_2 if array[1] == 2 else enter_3
			DictForCheck = {
				# SecondEnter это найденый второй Entry
				array[0]: SecondEnter.get(),
				# ThreeEnter это найденый третий Entry
				array[1]: ThreeEnter.get()
			}
		# Метод delete удаляет данные. Метод insert записывает данные.
		# Если хотите разобраться в проверках советую просмотреть на словать в def __init__():
		# Так будет проще понять что и как я делал.
		if self.MainDict[array[0]] == DictForCheck[array[0]] and self.MainDict[array[1]] == DictForCheck[array[1]]:
			MainEnter.delete(0, END)
		else:
			if CountEnter == 2:
				if self.MainDict[array[1]] != DictForCheck[array[1]] and not DictForCheck[array[1]]:
					# В главном Entry записываем данные.
					MainEnter.insert(0, self.MainDict[array[1]])
					# Во-втором Entry удаляем все данные
					SecondEnter.delete(0, END)
				if self.MainDict[array[0]] != DictForCheck[array[0]] and not DictForCheck[array[0]]:
					SecondEnter.insert(0, self.MainDict[array[0]])
					MainEnter.delete(0, END)
				MainEnter.delete(0, END)
			else:
				if self.MainDict[array[0]] != DictForCheck[array[0]] and not DictForCheck[array[0]]:
					SecondEnter.insert(0, self.MainDict[array[0]])
					MainEnter.delete(0, END)

				if self.MainDict[array[1]] != DictForCheck[array[1]] and not DictForCheck[array[1]]:
					ThreeEnter.insert(0, self.MainDict[array[1]])
					MainEnter.delete(0, END)
				MainEnter.delete(0, END)
