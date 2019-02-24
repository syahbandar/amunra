from distutils.core import setup
import setuptools

with open('README.md') as f:
    long_description = f.read()

setup(
    name = 'rampok',
    version = '0.1.1',
    description = 'A news portal scraping tool',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author = 'Yuka Langbuana',
    author_email = 'langbuana.yuka@hotmail.com',
    url = 'https://github.com/syahbandar/rampok', 
    py_modules=['rampok'],
    install_requires=[
      'bs4', 'requests'
    ],
)