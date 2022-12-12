from setuptools import setup, find_packages

setup(name='generic-server',
      version='0.0.1',
      packages=find_packages(),
      entry_points = {
          'console_scripts': ['genericserver=genericserver.__main__:main'],
          }
     )
