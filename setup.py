from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'


def get_requirements(file_path:str) -> List[str]:

    """
    this function will return the list of requirements
    """

    requirements = []
    with open(file_path) as file_ob:
        requirements = file_ob.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements


setup(
    name='ml-project',
    version='0.0.1',
    author='Rasna Tomar',
    author_email='rasna.tomar@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')



)