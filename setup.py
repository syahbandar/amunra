from distutils.core import setup
import setuptools

with open('README.md') as f:
    long_description = f.read()

setup(
    name = 'amunra',
    version = '0.2.0',
    description = 'A news portal scraping tool',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author = 'Yuka Langbuana',
    author_email = 'langbuana.yuka@hotmail.com',
    url = 'https://github.com/syahbandar/amunra', 
    py_modules=['amunra'],
    install_requires=[
      'bs4', 'requests'
    ],
)