from distutils.core import setup
from Cython.Build import cythonize

setup(
    name="LlamaLangCython",
    ext_modules=cythonize("*.pyx")
)
