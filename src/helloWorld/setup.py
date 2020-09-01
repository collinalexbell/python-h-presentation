from distutils.core import setup, Extension

module1 = Extension('hello', sources = ['helloworld.c'])

setup (name = 'Hello World',
       version = '1.0',
       description = '',
       ext_modules = [module1])
