# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

if __name__ == '__main__':

    with open('README.rst') as f:
        readme = f.read()

    with open('LICENSE') as f:
        license = f.read()

    setup(
        name='pySatTools',
        version='0.1.0',
        description='Python satellite tools',
        long_description=readme,
        author='Grzegorz Klopotek',
        author_email='grzesko77@wp.pl',
        license=license,
        packages=find_packages(exclude=('src', 'utils', 'docs','aprior'))
    )
