
from __future__ import print_function
from Cython.Shadow import declare
import cython

@cython.cclass
class Shrubbery :
    width : cython.int 
    height : cython.int 

    def __init__(self, w, h) :
        self.width = w 
        self.height = h 
    
    def describe(self) :
        print(f'This shrubbery is {self.width}, by {self.height}, cubits')

if __name__ == '__main__' :
    s = Shrubbery(10, 15)
    s.describe()

# $ python Cython/variables.py 
# This shrubbery is 10, by 15, 
# cubits

@cython.cfunc 
def egs(l : cython.ulong, f: cython.float ) -> cython.int :
    ...