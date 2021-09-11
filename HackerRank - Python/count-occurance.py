
# ---------------------------- Count the occurrences of characters in a string in Python ----------------------------


def countchars(string) :
    # saving into dictionary so we can 
    # fetch value of occurance
    chars = {}
    for char in string :
        if char in chars :
            chars[char] += 1
        else :
            chars[char] = 1
    return chars


def main() :
    string = 'ethernet'
    chars = countchars(string)
    for char, count in countchars('ethernet').items() :
        print(f'{char} : {count}')


if __name__ == '__main__' :
    main()


# $ python count-occurances.py 
# T : 2
# i : 2
# g : 2
# e : 2
# r : 2
# R : 1

# T.C : O(n) 


