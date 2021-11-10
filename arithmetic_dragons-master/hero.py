# coding: utf-8
# license: GPLv3
from gameunit import *

class Hero(Attacker):
	def __init__(self):
		self._health = 100
		self._attack = 50
		self._exp = 0
		

#FIXME:
"""В этом файле должен быть описан класс героя, унаследованный от Attacker
Герой должен иметь имя, задаваемое в конструкторе
Метод attack должен получать атрибут target и уменьшать его здоровье на величину атаки.

"""
