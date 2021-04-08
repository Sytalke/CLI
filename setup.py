from setuptools import setup, find_packages


def read_requirements():
    with open('requirements.txt') as requirements:
        content = requirements.read()
        req=content.split()
    return req
setup(
    name='vlcli',
    version='0.1.0', 
    packages=find_packages(),
    include_package_data=True,
    install_requires=read_requirements(),
    entry_points='''
        [console_scripts]
        vlcli=vlcli.cli:cli
    '''    
)