from distutils.core import setup, Extension

module = Extension("stringReverse", sources = ["stringReverse.c"])

setup(name="stringReverse",
		ext_modules = [module])