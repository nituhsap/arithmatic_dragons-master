# coding: utf-8
# license: GPLv3
from gameunit import *
from random import randint, choice

class Healer(Helper):
    pass


def generate_healer():
    AreThereAny = choice(enemy_types)
    enemy = AreThereAny()
    return enemy


def generate_dragon_list(enemy_number):
    enemy_list = [generate_random_enemy() for i in range(enemy_number)]
    return enemy_list


class Drunken_Priest(Healer):
    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer
