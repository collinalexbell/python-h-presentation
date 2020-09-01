# setup.py
from setuptools import setup, Extension
import os


os.environ["CC"] = "gcc"
ext = Extension(
      'dot_prod',
      sources = ['./dot_prod.c'])

setup(name='dot_prod',
       version='1.0',
       description='This is a demo package',
       ext_modules=[ext])
