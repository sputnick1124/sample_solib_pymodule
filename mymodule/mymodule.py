from ctypes import c_bool, c_int, c_double, Structure, CDLL

class Res(Structure):
    _fields_=[('valid',c_bool),
              ('a',c_double),
              ('b',c_double)]

class Inp(Structure):
    _fields_=[('a',c_double),
              ('b',c_double),
              ('c',c_double)]


class Lib:
    def __init__(self, libpath):
        
        self.lib = CDLL(str(libpath))
        self._quadratic = self.lib.quadratic
        self._quadratic.argtypes = [Inp]
        self._quadratic.restype = Res

    def quadratic(self, a, b, c):
        i = Inp(a, b, c)
        r = self._quadratic(i)
        if r.valid:
            return (r.a, r.b)
        return None
