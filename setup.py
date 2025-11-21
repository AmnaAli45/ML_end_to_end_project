# Ye file hmare project ko package k tor prr releases krne mein madad kre ga 

from setuptools import find_packages, setup
# setuptools --> Helps in packaging your Python project.
# find_packages --> Automatically finds all folders that contain an __init__.py file. These folders become Python packages.

from typing import List # Used for type hinting.

HYPHON_E_DOT = "-e ."

# Function to Read Requirements

def get_requirements(filepath:str) -> List[str]: # file path is a string .... it will return a list of strings
    requirements = []

    with open(filepath) as file_obj:
        requirements = file_obj.readlines()
        requirements = [i.replace("\n","") for i in requirements]

        if HYPHON_E_DOT in requirements:
            requirements.remove(HYPHON_E_DOT)

# Opens the file requirements.txt
# Reads all lines (each library in a separate line)
# Removes newline characters (\n)
# Removes the line "-e ." if it exists
# Returns the cleaned list of required libraries

setup(
    name = "end_to_end_project", # project name
    description="Machine Learning pipeline project", # small detail about project
    version = 0.01, # version of project
    author= "Amna Ali", # your name
    packages= find_packages(), # automatically finds the packages in your project
    install_requires = get_requirements("requirements.txt") # List of required libraries (taken from requirements.txt).
)
