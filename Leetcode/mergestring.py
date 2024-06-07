#!/usr/bin/env python                                                                                        
# -*- coding: utf-8 -*-                                                                                      
from __future__ import annotations                                                                           
import itertools                                                                                             
                                                                                                             
__problem_statement__ = """                                                                                  
You are given two strings word1 and word2.                                                                   
Merge the strings by adding letters in alternating order, starting with word1.                               
If a string is longer than the other, append the additional letters onto the end of the merged string.       
                                                                                                             
Return the merged string.                                                                                    
                                                                                                             
                                                                                                             
Example 1:                                                                                                   
                                                                                                             
Input: word1 = "abc", word2 = "pqr"                                                                          
Output: "apbqcr"                                                                                             
                                                                                                             
Explanation: The merged string will be merged as so:                                                         
                                                                                                             
word1:  a   b   c                                                                                            
word2:    p   q   r                                                                                          
merged: a p b q c r                                                                                          
                                                                                                             
Example 3:                                                                                                   
                                                                                                             
Input: word1 = "abcd", word2 = "pq"                                                                          
Output: "apbqcd"                                                                                             
                                                                                                             
Explanation: Notice that as word1 is longer, "cd" is appended to the end.                                    
word1:  a   b   c   d                                                                                        
word2:    p   q                                                                                              
merged: a p b q c   d                                                                                        
"""                                                                                                          
                                                                                                             
                                                                                                             
def merger(word_one: str, word_two: str) -> str:                                                             
    new_word = ""                                                                                            
    counter = 0                                                                                              
                                                                                                             
    if len(word_one) == 0 and len(word_two) == 0:                                                            
        return ""                                                                                            
                                                                                                             
    if len(word_one) == len(word_two):                                                                       
        for i in range(len(word_one)):                                                                       
            new_word += word_one[i]                                                                          
            new_word += word_two[i]                                                                          
                                                                                                             
    if len(word_one) < len(word_two):                                                                        
        for i in range(len(word_one)):                                                                       
            new_word += word_one[i]                                                                          
            new_word += word_two[i]                                                                          
            counter += 1                                                                                     
        new_word += word_two[counter::]                                                                      
                                                                                                             
    if len(word_one) > len(word_two):                                                                        
        for i in range(len(word_two)):                                                                       
            new_word += word_one[i]                                                                          
            new_word += word_two[i]                                                                          
            counter += 1                                                                                     
        new_word += word_one[counter::]                                                                      
                                                                                                             
    return new_word                                                                                          
                                                                                                             
                                                                                                             
def libUse(word1: str, word2: str) -> str:                                                                   
    """Solving using itertools library"""                                                                    
    return "".join(x + b for x, b in itertools.zip_longest(word1, word2, fillvalue=""))    


def naive(word1: str, word2: str) -> str:                                                                    
    # NOTE: Fails on second example                                                                          
    result = ""                                                                                              
    for i, j in zip(word1, word2):                                                                           
        result += i                                                                                          
        result += j                                                                                          
    return result                                                                                            
                                                                                                             

def main() -> None:                                                                                                           
  res = merger("abcd", "pq")                                                                                   
  print(res)                                                                                                   


if __name__ == "__main__":
  main()
