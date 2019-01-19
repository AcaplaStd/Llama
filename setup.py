from distutils.core import setup
from Cython.Build import cythonize

setup(
    name="TimeTest",
    ext_modules=cythonize("*.pyx")
)