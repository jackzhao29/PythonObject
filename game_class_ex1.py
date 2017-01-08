#coding:utf-8
#来自Percal 25号行星的哥顿人
from sys import exit
from random import randint

#场景类
class Scene(object):

	def enter(self):
		print ("This scene is not yet configured. Subclass it and implement enter().")
		exit(1)

#引擎类
class Engine(object):

	def __init__(self,scene_map):
		self.scene_map = scene_map


	def play(self):
		current_scene = self.scene_map.opening_scene()

		while True:
		 	print "\n-------------"
		 	next_scene_name = current_scene.enter()
			if next_scene_name is not None:
				current_scene = self.scene_map.next_scene(next_scene_name)
			else:
				print "No more scenes"



class Death(Scene):

	quips = [
		"You dide. You kinda suck at this.",
		"Your mom would be proud...if she were smarter.",
		"Such a luser.",
		"I have a small puppy that's better at this."
	]

	def enter(self):
		print Death.quips[randint(0, len(self.quips)-1)]


class Centralcorridor(Scene):

	def enter(self):
		print "The gothons of Planet Peercal #25 have invaded your ship and destroyed"
		print "your entire crew. You are the last surviving member and your last"
		print "mission is to get the neutron destruct bomb from the Weapons Armory."
		print "put it in the bridge, and blow the ship up after getting into an"
		print "escape pod."
		print "\n"
		print "You're running down the central corridor to the Weapons Armory when"
		print "a Gothon jumps oout, red scaly skin, dark grimy teeth,and evil clown costume"
		print "flowing around his hate filled body. He's blocking the door to the"
		print "Armory and about to pull a weapon to blast you."

		action = raw_input("> ")

		if action == "shoot!":
			print "Quick on the draw you yank out your blaster and fire it at the Gothon."
			print "His clown costume is flowing and moving around his body, which trhrows"
			print "off your aim. Your laser hits his costume but misses him, which"
			print "you are dead. Then he eats you."
			return 'death'

		elif action == "dodge!":
			print "Like a world class boxer you dodge, weave, slip and slide right"
			print "as the Gothon's blaster cranks a laser past your head."
			print "In the middle of your artful dodge your foot slips and you"
			print "bang your head on the metal wall and pas out."
			print "you wake up shortly after only to die as the Gothon stomps on"
			print "your head and eats you."
			return 'death'

		elif action == "tell a joke":
			print "Lucky for you they made you learn Gpthon insults in the academy."
			print "You tell the one Gothon joke you know:"
			print "Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr."
			print "The Gothon stops, tries not to laugh, then busts out laughing and can't move."
			print "While he's laughing you run up and shoot him square in the head"
			print "putting him down, then jump through the Weapon Armory door."
			return "laser_weapon_armory"

		else:
			print "DOES NOT COMPUTE!"
			return 'central_corridor'


class LaserWeaponArmory(Scene):

	def enter(self):
		pass

class TheBridge(Scene):

	def enter(self):
		print "Your burst onto the Bridge with the netron destruct bomb"
		print "under your arm and surprise 5 Gothons who are trying to"
		print "take control of the ship. Each of them has an even uglier"
		print "clown costume than the last. They haven't pulled their"
		print "weapons out yet, as they seee the active bomb under your"
		print "arm and don't want to se it off."

		action = raw_input("> ")

		if action == "throw the bomb":
			print "In a panic you throw the bomb at the group of Gothons"
			print "and make a leap for the door, Right as you drop it a"
			print "Gothon shoots you right in the back killing you."
			print "As you die you seee another Gothon frantically try to disarm"
			print "the bomb. You die knowing they will probably blow up when"
			print "it goes off."
			return 'death'

		elif action =="slowly place the bomb":
			print "You point your blaster at the bomb under your arm"
			print "and the Gothons put their hands up and start to sweat."
			print "You inchbackward to the door,open it ,and then carefull"
			return 'escape_pod'

		else:
			print "DOES NOT COMPUTE!"
			return "the_bridge"



class EscapePod(Scene):

	def enter(self):
		pass

class Map(object):

	scenes = {
		'central_corridor': Centralcorridor(),
		'laser_weapon_armory': LaserWeaponArmory(),
		'the_bridge': TheBridge(),
		'escape_pod': EscapePod(),
		'death': Death()
	}




	def __init__(self, start_scene):
		self.start_scene = start_scene


	def next_scene(self, scene_name):
		return Map.scenes.get(scene_name)


	def opening_scene(self):
		return self.next_scene(self.start_scene)
		pass


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
