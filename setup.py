from setuptools import find_packages
from distutils.core import setup

setup(
    name='skipper',
    version='0.0.1',
    url='http://github.com/Stratoscale/skipper',
    author='Adir Gabai',
    author_mail='adir@stratoscale.com',
    packages=find_packages(include=['skipper*']),
    entry_points={
          'console_scripts': [
              'skipper = skipper.main:main',
          ],
      },
    install_requires=[
            'PyYAML>=3.11',
            'click>=6.6',
            'docker-py>=1.8.1',
            'requests>=2.10.0',
            'tabulate>=0.7.5',
        ]
)
