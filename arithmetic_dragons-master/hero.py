# coding: utf-8
# license: GPLv3
from gameunit import *

class Hero(Attacker):
    _experience = None
    def __init__(self, name):
        self._health = 100
        self._attack = 50
        self._experience = 0
        self._name = name
		

#FIXME:
"""В этом файле должен быть описан класс героя, унаследованный от Attacker
Герой должен иметь имя, задаваемое в конструкторе
Метод attack должен получать атрибут target и уменьшать его здоровье на величину атаки.

"""
