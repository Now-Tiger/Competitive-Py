# METHOD 3 (A Juggling Algorithm)
''' 
1. Instead of moving one by one, divide the array in different sets 
where number of sets is equal to GCD of n and d and move the elements within sets.

2. If GCD is 1 as is for the above example array (n = 7 and d =2), then elements will be moved within one set only, 
we just start with temp = arr[0] and keep moving arr[I+d] to arr[I] and finally store temp at the right place.

3. Here is an example for n =12 and d = 3. GCD is 3 and 

GCD : Greatest common divisors can be computed by determining the prime factorizations of the two numbers and comparing factors.
'''
def new(arr):
    return arr
