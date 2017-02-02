"""Project setup file."""
from setuptools import find_packages, setup

setup(name='quick_anno',
      version='0.0.1',
      description='Quick and simple annotations for Python scripts.',
      author='Nitish Reddy Koripalli',
      author_email='nitish.k.reddy@gmail.com',
      url='https://github.com/nitred/quick_anno',
      download_url='https://github.com/nitred/quick_anno/master.tar.gz',
      license='MIT',
      install_requires=['future', 'requests', 'requests-futures'],
      packages=find_packages())
