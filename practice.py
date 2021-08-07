"""
Generates HTML from markdown
"""
#!/usr/bin/python3

from docopt import docopt
from os.path import join, dirname, isdir
from os import makedirs, listdir
from jinja2 import Environment
from jinja2 import PackageLoader
from jinja2 import Template

def generator(lines):
	"""
	>>> lines = ['Question: 1', 'Option: 1', 'Question: 2', 'Option: 3', "Question: 3", "Option: 4"]
	>>> questions = list(generator(lines))
	>>> len(questions)
	3
	>>> len(questions[0])
	2
	>>> len(questions[1])
	2
	"""
	lst = list()
	for line in lines:
		if line.startswith("Question:"):
			if lst: yield lst
			lst = [line.replace("Question:", '', 1)]
		elif line.strip():
			lst.append(line.replace("Option:", '', 1))
	if lst: yield lst

def converter(path, template):
	with open(path) as file_pointer:
		questions = generator(file_pointer.readlines())
	outpath = join("outputs", path).replace(".md", ".html")
	makedirs(dirname(outpath), exist_ok = True)
	with open(outpath, 'w') as file_pointer:
		file_pointer.write(template.render(questions = questions))
	print(f" * File outputted at {outpath}")

def main():
	arguments = docopt(__doc__, version = "Practice 1.0")
	env = Environment(loader=PackageLoader("practice", "templates"))
	template = env.get_template("index.html")
	path = arguments["<filepath>"]
	if isdir(path):
		for filename in listdir(path):
			if filename.endswith(".md"):
				converter(join(path, filename), template)
	else:
		converter(path, template)

if __name__ == "__main__":
	main()
