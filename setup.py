from setuptools import setup, find_packages

setup(name='mockserver',
      version='0.0.1',
      packages=find_packages(),
      entry_points = {
          'console_scripts': ['mockserver=mockserver.__main__:main'],
          }
     )
