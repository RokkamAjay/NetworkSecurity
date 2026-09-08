'''
The setup.py file is as esstential part of packaging and distibution of  python projects. It is Used by Setup tools (or Distutiles in order 
python versions.) to define the Configuration of the project, Such as its Metadata ,Dependencys and More.
'''

from setuptools import find_packages,setup
from typing import List


def get_requirements()->List[str]:
    """
    This function will return list of requirements
    """
    requirement_lst:List[str] = []
    try:
        with open('requirements.txt','r') as file:
            ## Read lines from file
            lines = file.readlines()
            ## Process Each Line
            for line in lines:
                requirement = line.strip()
                ## Ignore empty lines and -e.
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirement.txt file is Not Found! ")

    return requirement_lst

setup(
    name='NetworkSecurity',
    version= '0.0.0.1',
    author='RokkamAjay',
    author_email='ajayrokkam38@gmail.com',
    packages = find_packages(),
    install_requires=get_requirements()

)