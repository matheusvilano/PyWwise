import setuptools
from pathlib import Path

long_description = (Path(__file__).parent/"README.md").read_text()

setuptools.setup(
		author="Matheus Vilano",
		author_email="",
		classifiers=[
			"Development Status :: 2 - Pre-Alpha",
			"Intended Audience :: Developers",
   			"Intended Audience :: Education",
			"License :: OSI Approved :: MIT License",
			"Operating System :: OS Independent",
			"Programming Language :: Python :: 3",
		],
		description="A comprehensive WAAPI wrapper - fully documented, with auto-completion in mind.",
		install_requires=[],
		keywords="audiokinetic wwise waapi game audio",
		license="MIT",
		long_description=long_description,
		long_description_content_type="text/markdown",  # GitHub-flavored Markdown (GFM)
		name="pywwise",
		packages=setuptools.find_packages("pywwise"),
		package_dir={"": "pywwise"},
		project_urls={
			"Author Website": "https://www.matheusvilano.com/",
			"Git Repository": "https://github.com/matheusvilano/PyWwise.git",
		},
		python_requires=">=3.12",
		url="https://github.com/matheusvilano/PyWwise.git",
		version="0.0.1",
)
