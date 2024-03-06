#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : setup.py.py
# @Author: hanyan_news
# @Desc  :


from distutils.core import setup
from setuptools import find_packages

with open("README.rst", "r") as f:
  long_description = f.read()


setup(name='package-tea-one',  # 包名
      version='1.0.0',  # 版本号
      description='small package just example',
      long_description=long_description,
      author='hanyan_news',
      author_email='hanyan0572@gmail.com',
      url='https://github.com/hanyan007/package-tea-one.git',
      install_requires=["package-tea-hanyan==1.0.3", "restful-dnspod-log==1.0.1"],
      project_urls={  # Optional
        "Source": 'https://github.com/hanyan007/package-tea-one.git',
      },
      license='BSD License',
      packages=find_packages(),
      platforms=["all"],
      classifiers=[
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Natural Language :: Chinese (Simplified)',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Topic :: Software Development :: Libraries'
      ],
      )
