#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import textwrap

setup(name='pybot_i2c',
      namespace_packages=['pybot'],
      version='1.0',
      description='I2C/SMBus interface',
      license='LGPL',
      long_description=textwrap.dedent("""
            This sub-package contains classes allowing accessing devices
            connected to an I2C or SMBus bus.
      """),
      author='Eric Pascual',
      author_email='eric@pobot.org',
      url='http://www.pobot.org',
      download_url='https://github.com/Pobot/PyBot',
      packages=find_packages("src"),
      package_dir={'': 'src'}
      )
