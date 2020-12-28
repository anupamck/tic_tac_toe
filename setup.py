try:
    from setuptools import setup
except ImportError:
    from distutils.core. import setuptools

config = {
    'description': 'My Project',
    'author': 'Anupam Krishnamurthy',
    'url': '<Project URL>',
    'download_url': '<Download URL>',
    'author_email': 'anupam.ck@gmail.com',
    'version': '0.1',
    'install_requires': ['pytest'],
    'packages': ['NAME'],
    'scripts': [],
    'name:' 'projectname'
}

setup(**config)
