#!/usr/bin/env cython

# --------- C variable declarations ---------- 
from __future__ import print_function
from Cython.Shadow import declare
import cython

globalVariable = declare(cython.int)

def func() :
    i : cython.int 
    j : cython.int 
    k : cython.int
    f : cython.float 
    g : cython.int[42]
    h : cython.p_float 

# Moreover, C struct, union and enum are supported :

Grail = cython.struct(
    age = cython.int, 
    volume = cython.float 
    )

Food = cython.union(
    spam = cython.p_char, 
    eggs = cython.p_float
    ) 

# -------------------------------------------------------------------

# Cython typedef 

p_char = cython.typedef(cython.p_char)
p_float = cython.typedef(cython.p_float)

print(f'p_char : {p_char}, \n'
     f'p_float : {p_float} ')

# $ python Cython/variables.py 
# p_char : <class 'Cython.Shadow.pointer.<locals>.PointerInstance'>,
# p_float : <class 'Cython.Shadow.pointer.<locals>.PointerInstance'>

# -------------------------------------------------------------------
