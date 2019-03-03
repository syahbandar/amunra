from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name = 'amunra',
  version = '0.3.1',
  description = 'A news portal scraping tool',
  long_description=long_description,
  long_description_content_type="text/markdown",
  author = 'Yuka Langbuana',
  author_email = 'langbuana.yuka@gmail.com',
  url = 'https://github.com/syahbandar/amunra', 
  py_modules=['amunra'],
  install_requires=[
    'bs4', 'requests'
  ],
)