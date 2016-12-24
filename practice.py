from jinja2 import Environment
from jinja2 import PackageLoader
from jinja2 import Template

def generator(lines):
	"""
	>>> lines = ['Question: 1', 'Option: 1', 'Question: 2', 'Option: 3']
	>>> questions = list(generator(lines))
	>>> len(questions)
	2
	>>> len(questions[0])
	2
	>>> len(questions[1])
	2
	"""
	lst, seen = [], 0
	for line in lines:
		if line.startswith('Question:') and seen == 0:
			lst.append(line)
			seen += 1
		elif line.startswith('Question:') and seen == 1:
			val = lst
			lst = []
			lst.append(line)
			yield val
		elif line.strip():
			lst.append(line)
	yield lst


def main():
	questions = generator(open('questions.md').readlines())
	
	env = Environment(loader=PackageLoader('practice', 'templates'))	
	template = env.get_template('index.html')

	f = open('output.html', 'w')
	f.write(template.render(questions = questions))
	f.close()

if __name__ == '__main__':
	main()