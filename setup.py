#!/usr/bin/env python

from setuptools import setup, Extension

clib_name = 'clibrary'
# extension will be placed in mymodule/lib/<clib_name>.<machine>.so
clib = Extension(name='mymodule.lib.{}'.format(clib_name), sources=['{}/a.c'.format(clib_name)])

mod_name = 'mymodule'
setup(name=mod_name,
      packages=[mod_name],
      ext_modules=[clib],
      )
