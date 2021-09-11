
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
# e : 3
# t : 2
# h : 1
# r : 1
# n : 1


# T.C : O(n) 


