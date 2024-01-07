# da fokk is sequenca and why do I need alphabeth to use it?
from collections.abc import Sequence

import math

def fibonacci(n: int) -> int:

    # generate fibonacci list for some object oriented reason
    class fibonacci(Sequence):
        def __getitem__(self, index):
            if index < 0:
                return 0

            a = 0
            b = 1
            
            # imagine using for in loop
            for _ in range(index-1):
                a, b = b, a + b

            return a


        def __len__(self):
            return 69

        def __set__(self, index, value):
            print("what the fuck")

    fib = fibonacci()
    
    return fib[n]
    # imagine using return

########
# THERE ENDS FIB FUNCTION
# WHY MUST IT BE INDENTATION BASED
########

# or you can omit types if you feel dangerous today
def factorial(n):
    res = 1
    
    # this is my recursion
    # tail optimization was not implemented
    # for some stupid reason
    while True:
        if n <= 0:
            return res

        res *= n
        n -= 1

def circumference(r):
    return 2 * math.pi * r
# some other guys PI ↑
# do I even trust him?
# he's a python developer after all

def circleSurface(r):
    return math.pi * r**2

def sphereVolume(r):
    return (4/3) * math.pi * r**3
