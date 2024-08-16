# Copyright 2024 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

if __name__ == "__main__":
    from setuptools import find_packages, setup
    from pathlib import Path

    setup(
        author="Matheus Vilano",
        author_email="",
        classifiers=[
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Developers",
            "Intended Audience :: Education",
            "License :: OSI Approved :: Apache Software License",
            "Operating System :: OS Independent",
            "Programming Language :: Python :: 3",
        ],
        description="A comprehensive Wwise Authoring API wrapper - fully documented, with auto-completion in mind.",
        install_requires=(Path(__file__).parent / "requirements.txt").read_text().splitlines(),
        keywords="audiokinetic wwise waapi game audio sound automation scripting asset pipeline",
        license="MIT",
        long_description=(Path(__file__).parent / "README.md").read_text(),
        long_description_content_type="text/markdown",  # GitHub-flavored Markdown (GFM)
        name="pywwise",
        packages=find_packages("pywwise"),
        package_dir={"": "pywwise"},
        project_urls={
            "Author Website": "https://www.matheusvilano.com/",
            "Git Repository": "https://github.com/matheusvilano/PyWwise.git",
        },
        python_requires=">=3.12",
        url="https://github.com/matheusvilano/PyWwise.git",
        version="0.0.2",
    )
