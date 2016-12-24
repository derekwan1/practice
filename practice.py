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
	lst = []
	for line in lines:
		if line.startswith('Question:'):
			if lst:
				yield lst
			lst = [line.replace('Question:', '', 1)]
		elif line.strip():
			lst.append(line.replace('Option:', '', 1))
	if lst:
		yield lst


def main():
	questions = generator(open('questions.md').readlines())
	
	env = Environment(loader=PackageLoader('practice', 'templates'))	
	template = env.get_template('index.html')

	f = open('outputs/output.html', 'w')
	f.write(template.render(questions = questions))
	f.close()

if __name__ == '__main__':
	main()