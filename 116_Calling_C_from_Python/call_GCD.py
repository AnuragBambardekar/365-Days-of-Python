import ctypes
import os

# locating the 'libgcd.so' file in the
# same directory as this file
_file = 'libgcd.so'
_path = os.path.join(*(os.path.split(__file__)[:-1] + (_file, )))
_mod = ctypes.cdll.LoadLibrary(_path)

# int gcd(int, int)
gcd = _mod.gcd
gcd.argtypes = (ctypes.c_int, ctypes.c_int)
gcd.restype = ctypes.c_int

# int divide(int, int, int *)
_divide = _mod.divide
_divide.argtypes = (ctypes.c_int, ctypes.c_int,
                    ctypes.POINTER(ctypes.c_int))
_divide.restype = ctypes.c_int


def divide(x, y):
    rem = ctypes.c_int()
    quot = _divide(x, y, rem)
    print(f"x: {x}, y: {y}, so {x}/{y} = \n")
    print(f"The quotient is {quot}")
    print(f"The remainder is {rem.value}\n")
    return quot, rem.value


# void avg(double *, int n)
# Define a special type for the 'double *' argument
class DoubleArrayType:
    def from_param(self, param):

        typename = type(param).__name__

        if hasattr(self, 'from_' + typename):
            return getattr(self, 'from_' + typename)(param)

        elif isinstance(param, ctypes.Array):
            return param

        else:
            raise TypeError("Can't convert % s" % typename)

    # Cast from array.array objects
    def from_array(self, param):
        if param.typecode != 'd':
            raise TypeError('must be an array of doubles')

        ptr, _ = param.buffer_info()
        return ctypes.cast(ptr, ctypes.POINTER(ctypes.c_double))

    # Cast from lists / tuples
    def from_list(self, param):
        val = ((ctypes.c_double)*len(param))(*param)
        return val

    from_tuple = from_list

    # Cast from a numpy array
    def from_ndarray(self, param):
        return param.ctypes.data_as(ctypes.POINTER(ctypes.c_double))


DoubleArray = DoubleArrayType()
_avg = _mod.avg
_avg.argtypes = (DoubleArray, ctypes.c_int)
_avg.restype = ctypes.c_double


def avg(values):
    result = _avg(values, len(values))
    print(f"The average is {result}")
    return result


# struct Point { }
class Point(ctypes.Structure):
    _fields_ = [('x', ctypes.c_double), ('y', ctypes.c_double)]


# double distance(Point *, Point *)
distance = _mod.distance
distance.argtypes = (ctypes.POINTER(Point), ctypes.POINTER(Point))
distance.restype = ctypes.c_double


# Sample Usage
if __name__ == '__main__':
    print("gcd of 36 and 24 is ", gcd(36, 24),"\n")

    x = 1234
    y = 13
    quotient, remainder = divide(x, y)

    data = [1,2,3,4,5]
    print(f"The input data is {data}\n")

    p1 = Point(1.0, 2.0)
    p2 = Point(4.0, 6.0)
    print(f"The distance between ({p1.x}, {p1.y}) and ({p2.x}, {p2.y}) is {distance(ctypes.byref(p1), ctypes.byref(p2))}")
