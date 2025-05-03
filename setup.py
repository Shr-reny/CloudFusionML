from setuptools import find_packages, setup
from typing import List
HYPHEN_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    ''' This function returns requirements as a list'''
    requirements =[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.replace('\n','') for req in requirements]
        
        if HYPHEN_DOT in requirements:
            requirements.remove(HYPHEN_DOT)

    return requirements

setup(
    name = 'CloudFusionML',
    version = '0.0.1',
    author = 'Shruti Swarupa Dhar',
    author_email= 'shrutireny@gmail.com',
    packages= find_packages(),
    install_requires = get_requirements('requirements.txt')
)