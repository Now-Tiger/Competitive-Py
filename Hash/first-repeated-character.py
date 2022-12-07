#!/usr/bin/ python3
# -*- coding: uf-8 -*-
# Problem : Give an algorithm for printing the first repeated character if there are duplicated elements in it.


class solution(object):
    def brut_force(self, string: str) -> None:
        """ Time Complexity: O(N^2) 
            Space Complexity: O(1)
        """
        string = string.lower().replace(" ", "")
        
        counter: int = 0
        size: int = len(string)
        
        for i in range(size):
            if counter == 1:
                break
            for j in range(i+1, size):
                if string[i] == string[j]:
                    print(string[i])
                    counter = 1
                    break       
        if counter == 0:
            print(-1)
            return 

    def hash_table(self, string: str) -> None: 
        """ Time Complexity: O(N) 
            Space Complexity: O(N)
        """
        string = string.lower().replace(" ", "")

        table: dict = {}
        size: int = len(string)

        for i in range(size):
            if string[i] in table:
                table[string[i]] += 1
            else:
                table[string[i]] = 1

        count: int = 0
        for i in range(size):
            if table[string[i]] >1:
                print(string[i])
                count = 1
                break
        if count == 0:
            print(-1)


    def efficient_hashing(self, string: str) -> None:
        """ Time Complexity: O(N) 
            Space Complexity: O(N)
        """
        string = string.lower().replace(" ", "")

        table: dict = {}
        size: int = len(string)
        ans: int = size + 1
        
        for i in range(size):
            if string[i] in table:
                ans = min(ans, table[string[i]]) 
            else:
                table[string[i]] = i

        if ans == size + 1:
            print(-1)
        else:
            print(string[ans])


def main() -> None:
    instance = solution()
    letters = "HEe lLo"
    solution.brut_force(instance, letters)
    solution.hash_table(instance, letters)
    solution.efficient_hashing(instance, letters)
    return
    

if __name__ == "__main__":
    main() 


# $ python first-repeated-character.py
# e
# e
# e
