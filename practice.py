from TexSoup import TexSoup
from jinja2 import Environment
from jinja2 import PackageLoader
from jinja2 import Template

def main():
	soup = TexSoup(open("quiz06.tex"))
	questions = soup.find_all('item')
	
	env = Environment(loader=PackageLoader('practice', 'templates'))	
	template = env.get_template('index.html')

	f = open('index.html', 'w')
	f.write(template.render(questions = questions))
	f.close()
if __name__ == '__main__':
	main()