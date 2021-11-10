# coding: utf-8
# license: GPLv3

from abc import ABC, abstractmethod

class Mobile(ABC):
	pass


class Attacker(Mobile):
	_health = None
	_attack = None
        
	def is_alive(self):
		return self._health > 0

	def attack(self, target):
		target._health -= self._attack   
        
class Helper(Mobile):
	_heal = None
	
	def heal(self, target):
		if target._health < 100:
			target._health += self._heal
