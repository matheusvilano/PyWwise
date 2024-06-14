from sys import argv
from os import system


def main():
	if "--nobuild" not in argv:
		system("python setup.py sdist")
	system("twine upload dist/*")


if __name__ == "__main__":
	main()
