# Ye file hmare project ko package k tor prr releases krne mein madad kre ga 

from setuptools import find_packages, setup
from typing import List

HYPHON_E_DOT = "-e ."

def get_requirements(filepath:str) -> List[str]:
    requirements = []

    with open(filepath) as file_obj:
        requirements = file_obj.readlines()
        requirements = [i.replace("/n","") for i in requirements]

        if HYPHON_E_DOT in requirements:
            requirements.remove(HYPHON_E_DOT)

setup(
    name = "end_to_end_project",
    description="Machine Learning pipeline project",
    version = 0.01,
    author= "Amna Ali",
    packages= find_packages(),
    install_requires = get_requirements("requirements.txt")
)