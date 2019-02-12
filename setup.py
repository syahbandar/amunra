from distutils.core import setup

setup(
    name = 'amunra',
    version = '0.1.0',
    description = 'A web scraping tool for Indonesian news website',
    author = 'Yuka Langbuana',
    author_email = 'langbuana.yuka@hotmail.com',
    url = 'https://github.com/YukaLangbuana/amunra', 
    py_modules=['amunra'],
    install_requires=[
      'bs4', 'requests', 'json'
    ],
)