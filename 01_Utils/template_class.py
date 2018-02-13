"""
	Author: Luis_C-137
	Class template file
"""

class User:
	"""
	Here goes the docstring documentation
	This text is displayed with the help function
	"""
	def __init__(self,name,age):
		self.name = name
		self.age = age

	def print_name():
		"""This method printd the name of the user"""
		print(self.name)

def main():
	help(User)

if __name__ == '__main__':
	print("This file contains a class, by accesing it this way it will run the help method for the class")
	main()
else:
	print("Importing module {}".format(__name__))