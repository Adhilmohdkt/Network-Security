from setuptools import find_packages,setup
from typing import List

requirement_lst:List[str]=[]
def get_requirements()->List[str]:

    try:
        with open('requirements.txt','r') as file:
            lines=file.readline()
            for line in lines :
                requirement=line.strip()
                if requirement and requirement!='-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print('the requirement file is not found')
setup(
    name='Networksecurity',
    version='0.0.1',
    author='Adhil mohammed kt',
    author_email='adhil9106@gamil.com',
    packages=find_packages(),
    install_requires=get_requirements()
)

