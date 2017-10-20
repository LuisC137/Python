"""
	Author: Luis_C-137
	This is a template file
"""

def doSomething():
	""" This is actualy funny because this methos does nothing"""
	pass

def printHelpOfMethod():
	""" This method returns the help for doSomething method"""
	help(doSomething)

def main():
	print("\n\n---------------------")
	print("And so it begins...\n\n\n")
	doSomething()
	printHelpOfMethod()
	

if __name__ == '__main__':
	main()
else:
	print("Importing module {} may not be useful".format(__name__))