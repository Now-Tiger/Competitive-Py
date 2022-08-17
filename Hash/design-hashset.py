#!/use/bin/env/ pypy3
# -*- coding: utf-8 -*-

# 705.
# ------------------------------------------------ Design HashSet ------------------------------------------------
# Design a HashSet without using any built-in hash table libraries.

# Implement MyHashSet class:

# - void add(key) Inserts the value key into the HashSet.
# - bool contains(key) Returns whether the value key exists in the HashSet or not.
# - void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.

# ----------------------------------------------------------------------------------------------------------------

from bisect import insort, bisect_left

class MyHashSet :
    def __init__(self) :
        self.data = []

    def __str__(self) :
        return str(self.data)

    def add(self, key) :
        if not self.data :
            self.data.append(key)
        else :
            if not self.contains(key) :
                insort(self.data, key)

    def remove(self, key) :
        if self.data :
            idx = bisect_left(self.data, key)
            if idx < len(self.data) and self.data[idx] == key :
                self.data.pop(idx)

    def contains(self, key) :
        if not self.data :
            return False
        idx = bisect_left(self.data, key)
        return self.data[idx] == key if idx < len(self.data) else False


def main() :
    hashset = MyHashSet()
    hashset.add(1)
    hashset.add(2)
    hashset.add(5)
    print(f'Is 5 in hashset : {hashset.contains(5)}')
    print(f'Hashset : {str(hashset)}')
    hashset.remove(5)
    print(f'After removing 5 : {str(hashset)}')

if __name__ == '__main__' :
    main()

# $ python design-hashset.py 
# Is 5 in hashset : True
# Hashset : [1, 2, 5]      
# After removing 5 : [1, 2]

# T.C = O(n)
