from .mymodule import Lib as Lib
from . import lib

from distutils.sysconfig import get_config_var

try:
    from importlib.resources import files
except ImportError:
    from importlib_resources import files

_libpath = (files(lib) / 'clibrary').with_suffix(get_config_var('EXT_SUFFIX'))

LIB = Lib(str(_libpath))

def quadratic(a, b, c):
    return LIB.quadratic(a, b, c)

del lib
del _libpath
