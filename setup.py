# Llama - list-oriented programming language
# (C) Acapla Studios

# python setup.py build_ext --inplace

from distutils.core import setup
from Cython.Build import cythonize

setup(
    name="LlamaLangCython",
    ext_modules=cythonize("*.pyx")
)
