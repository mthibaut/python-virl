#!/usr/bin/env python

from distutils.core import setup

setup(name='python-virl',
      version='1.0.0',
      url='https://github.com/mthibaut/python-virl',
      description='Control Cisco VIRL through a python script',
      author='Maarten Thibaut',
      author_email='mthibaut@cisco.com',
      scripts=['scripts/python-virl'],
      install_requires=['requests'],

      classifiers=[
         'Development Status :: 3 - Alpha',
         'Topic :: Utilities',
	 'Intended Audience :: System Administrators',
	 'License :: Public Domain',
      ],
)



