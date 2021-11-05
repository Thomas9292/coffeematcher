from setuptools import find_packages, setup

setup(
    name='coffeematcher',
    version='0.0.1',
    url='https://github.com/Thomas9292/coffeematcher.git',
    author='Thomas Wesselink',
    author_email='wesselink.tc@gmail.com',
    description='Coffeematcher is a python library to randomly match participants for coffee meetings.',
    packages=find_packages(),    
    install_requires=[],
    entry_points={
      'console_scripts': [
        'run_coffee = coffeematcher.main:main',
      ],
    }
)