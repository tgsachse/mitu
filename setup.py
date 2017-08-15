#! /usr/bin/env python3
"""
"""
from setuptools import setup

def load_description():
    with open('docs/README.md', 'r') as f:
        long_description = f.read()
        return long_description

setup(
    name='mitu',
    version='1.0.0',
    author='Tiger Sachse',
    author_email='tgsachse@gmail.com',
    description=('A collection of methods that may be useful when building ' +
                 'interactive terminal elements in programs.'),
    long_description=load_description(),
    url='https://github.com/tgsachse/mitu',
    license='GPLv3',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: Libraries:: Python Modules',
        'Topic :: Terminals'],
    keywords='mitu terminal termcolor interactive CLI color print output',
    packages=['mitu'],
    install_requires=['termcolor'],
    python_requires='>=3',
    data_files=[('share/doc/mitu', ['docs/LICENSE.txt', 'docs/README.md'])]
    )

