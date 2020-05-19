from distutils.core import setup, Extension

module = Extension("kvadratas", sources = ["kvadratas.c"])

setup(name="kvadratas",
		ext_modules = [module])