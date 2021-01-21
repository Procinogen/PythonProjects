class person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

def Main():
	guy = person(input("What is your name? "), input("What is your age? "))
	html = f"<h3>{guy.name}'s credentials:</h3>\n<ul>\n\t<li>Age: {guy.age}</li>\n<ul>"
	print(html)
	return
	
Main()
input("")