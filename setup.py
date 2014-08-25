#!/usr/bin/env python

from distutils.core import setup

setup(
    name='cache-stdout',
    version='0.2.0',
    description='Command-line utility to store output and reuse it later',
    author='Sergey Valiev',
    author_email='svaliev@gmail.com',
    url='https://github.com/Valiev/cache',
    scripts=['cache'],
    long_description=open('README.md').read(),
)
