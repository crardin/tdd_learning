try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description' : 'tdd learning',
    'author': 'Clay Rardin',
    'url': '',
    'download_url': '',
    'author_email:': 'clayton.rardin@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': [],
    'scripts': [],
    'name': 'binary'
}

setup(**config)