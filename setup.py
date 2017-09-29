"""Project setup file."""
from setuptools import find_packages, setup

setup(name='decoratory',
      version='0.1.0',
      description='Quick and simple annotations for Python scripts.',
      author='Nitish Reddy Koripalli',
      author_email='nitish.k.reddy@gmail.com',
      url='https://github.com/nitred/decoratory',
      download_url='https://github.com/nitred/decoratory/master.tar.gz',
      license='MIT',
      install_requires=['future'],
      packages=find_packages())
