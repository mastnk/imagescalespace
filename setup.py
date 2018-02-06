#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
	name= 'imagescalespace', # Application name:
	version= '0.1.1', # Version number

	author= 'Masayuki Tanaka', # Author name
	author_email= 'mastnk@gmail.com', # Author mail	

	url='https://github.com/mastnk/imagescalespace', # Details
	description='A python package for image scale space.', # short description
	long_description='A python package for image scale space.', # long description
	install_requires=[ # Dependent packages (distributions)
		'Pillow', 'numpy', 'scipy'
	],
	
	include_package_data=False, # Include additional files into the package
	packages=find_packages(),

	test_suite = 'tests',

	classifiers=[
		'Programming Language :: Python :: 3.6',
		'License :: OSI Approved :: MIT',
    ]
)

# uninstall
# % python setup.py install --record installed_files
# % cat installed_files | xargs rm -rf
# % rm installed_files

