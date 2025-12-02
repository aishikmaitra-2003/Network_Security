from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    This func returns list of requirements

    """
    req_list:List[str]=[]
    try:
        with open("requirements.txt","r") as file:
            lines=file.readlines()
            for line in lines:
                requirement=line.strip()
                if requirement and requirement!="-e .":
                    req_list.append(requirement)
    except FileNotFoundError:
        print("Requirements.txt is unavailable")
    return req_list
print(get_requirements())
setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Aishik Maitra",
    author_email="aishikmaitra2003@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)