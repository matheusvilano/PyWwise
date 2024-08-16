# Copyright 2024 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

def main():
	from setuptools import find_packages, setup
	from pathlib import Path
	readme_path = Path(__file__).parent / "README.md"
	requirements_path = Path(__file__).parent / "requirements.txt"
	long_description = readme_path.read_text()
	setup()


if __name__ == "__main__":
	main()
