from setuptools import find_packages, setup

with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name="ezo",
    version="0.1",
    description="Python package that acts as a wrapper for the EZOffice API.",
    author="Jordan Maynor",
    author_email="jmaynor@pepsimidamerica.com",
    packages=find_packages(),
    python_requires=">=3.12",
    install_requires=required,
)
