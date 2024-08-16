# Copyright 2024 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from setuptools import find_packages, setup
from pathlib import Path


def main():
	setup(long_description=(Path(__file__).parent / "README.md").read_text(),
	      long_description_content_type="text/markdown")


if __name__ == "__main__":
	main()
