# essential for packging and distributing python projects

from setuptools import find_packages, setup
from typing import List

requirement_lst = []

def get_requirements()-> List[str]:
    """
    This fxn will return list of requirements
    """
    try: 
        with open('requirements.txt', 'r') as file:
            # read lines from the files
            lines = file.readlines()
            # process each line 
            for line in lines:
                requirement=line.strip()
                ## ignoree empty lines and -e.
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)

    except fileNotFoundError:
        print("requirements.txt not found")

    return requirement_lst


setup(
    name = "NetworkSecurity",
    version="0.0.1",
    author="ADITYA",
    author_eamil= "adityamishra76731@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)