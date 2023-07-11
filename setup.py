#!/usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import re

version = ''
with open('pyforms/__init__.py', 'r') as fd: version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                                                                 fd.read(), re.MULTILINE).group(1)

if not version: raise RuntimeError('Cannot find version information')

setup(
    name='PyForms',
    version=version,
    description="""Pyforms is a Python framework to develop GUI applications based on pyqt""",
    author='Ricardo Ribeiro',
    author_email='ricardojvr@gmail.com',
    license='MIT',
    url='https://github.com/UmSenhorQualquer/pyforms',
    install_requires=[
        'pyforms-terminal @ git+https://github.com/gamecraftCZ/pyforms-terminal-bazarator.git@v4',
        'pyforms-gui @ git+https://github.com/gamecraftCZ/pyforms-gui-bazarator.git@v4',
        'pyforms-web @ git+https://github.com/gamecraftCZ/pyforms-web-bazarator.git@v4',
    ],
    packages=find_packages()
)
