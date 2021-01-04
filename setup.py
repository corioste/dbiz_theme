# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in dbiz_theme/__init__.py
from dbiz_theme import __version__ as version

setup(
	name='dbiz_theme',
	version=version,
	description='Theme for DBiz',
	author='Clapton Orioste',
	author_email='corioste@bai.ph',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
