#!/usr/bin/python
class Fridge(object):
	"""This class implemetns a fridge where ingredients can be added and removed individually ,or in groups.
	The firdge will retain a count of every ingredient added or removed,and will raise an error if a sufficient
	quantity of an ingredient isn't present."""
	def __init__(self, items = {}):
		"""Optionally pass in an initial dictionary of items"""
		if type(items) != type({}):
			raise TypeError("Fridge need a dictionary but was given %s" %type(items))
		self.items = items
		return

	def __add_muilt(self,food_name,quantity):
		"""__add_muilt(food_name,quantity) -adds more than one of a food item.Returns the number of items added
		This should only be used internally,after the type checking has been done"""
		if (not food_name in self.items):
			self.items[food_name] =0
		self.items[food_name] = self.items[food_name] + quantity


	def add_one(self,food_name):
		if type(food_name) != type(""):
			raise TypeError("add_one need a string but was given %s" % type(food_name))
		else:
			self.__add_muilt(food_name,1)
		return True

	def add_many(self,food_dict):
		if type(food_dict) != type({}):
			raise TypeError("add_many need a dictionary but was given %s" % type(food_dict))
		for item in food_dict.keys():
			self.__add_muilt(item,food_dict[item])
		return True

	def has(self,food_name,quantity=1):
		return self.has_various({food_name:quantity})

	def has_various(self,foods):
		try:
			for food in foods.keys():
				if self.items[food] < foods[food]:
					return False
			return True
		except KeyError:
			return False
	def __get_multi(self,food_name,quantity):
		try:
			if (self.items[food_name] is None):
				return False
			if (quantity > self.items[food_name]):
				return False
			self.items[food_name] = self.items[food_name] - quantity
		except KeyError:
			return False
		return quantity

	def get_one(self,food_name):
		if type(food_name) != type(""):
			raise TypeError("get_one needs a string,given a %s" % type(food_name))
		else:
			result = self.__get_multi(food_name,1)
		return result


	def get_many(self,food_dict):
		if self.has_various(food_dict):
			foods_removed ={}
			for item in food_dict.keys():
				foods_removed[item] = self.__get_multi(item,food_dict[item])
			return foods_removed

	def get_ingredients(self,food):
		try:
			ingredients = self.get_many(food.__ingredients__())
		except AttributeError:
			return False
		if ingredients != False:
			return ingredients

class Omelet(object):
	"""docstring for Omelet"""
	def __init__(self, kind = "cheese"):
		self.set_kind(kind)
		return 

	def __ingredients__(self):
		return self.needed_ingredients

	def get_kind(self):
		return self.kind

	def set_kind(self,kind):
		possible_ingredients = self.__known_kinds(kind)
		if possible_ingredients ==False:
			return False
		else:
			self.kind =kind
			self.needed_ingredients = possible_ingredients

	def set_new_kind(self,name,ingredients):
		self.kind = name
		self.needed_ingredients = ingredients
		return

	def __known_kinds(self,kind):
		if kind =="cheese":
			return  {"eggs":2,"milk":1,"cheese":1}
		elif kind =="mushroom":
			return {"eggs":2,"milk":1,"cheese":1,"mushroom":2}
		elif kind =="onion":
			return {"eggs":2,"milk":1,"cheese":1,"onion":1}
		else:
			return False

	def get_ingredients(self,fridge):
		self.from_fridge = fridge.get_ingredients(self)

	def mix(self):
		for ingredient in self.from_fridge.keys():
			print ("Mixing %d %s for the %s omelet" % (self.from_fridge[ingredient],ingredient,self.kind))
		self.mixed = True

	def make(self):
		if self.mixed == True:
			print ("Cooking the %s omelet!" % self.kind)
			self.cooked = True


		




if __name__ == '__main__':
	f = Fridge({"eggs":6,"milk":4,"cheese":3})
	print f.items
	print f.add_one("grape")
	print f.items
	print f.add_many({"mushroom":5,"tomato":3})
	print f.items

	print "-"*100
	print 'has and has_various fuction'
	f = Fridge({"eggs":6,"milk":4,"cheese":3})
	if f.has("cheese",3):
		print "Year"
	else:
		print "has no "

	print "-"*100
	print "Class omelet"
	o = Omelet("cheese")
	f = Fridge({"cheese":5,"milk":4,"eggs":12})
	o.get_ingredients(f)
	print o.mix()
	print o.make()

	f = Fridge({"cheese":5,"milk":4,"eggs":12,"mushroom":6,"onion":6})
	o = Omelet("cheese")
	e = Omelet("eggs")
	m = Omelet("mushroom")
	c = Omelet("onion")
	c.get_ingredients(f)
	print c.mix()
	m.get_ingredients(f)
	print m.mix()
	c.get_ingredients(f)
	print c.mix()
	print "--"
	#print o.make()
	print m.make()
	print c.make()
	#print e.eggs()


