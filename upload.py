# Copyright 2024 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from os import system
from sys import argv


def main():
    if "--nobuild" not in argv:
        system("python setup.py sdist")
    system("twine upload dist/*")


if __name__ == "__main__":
    main()
