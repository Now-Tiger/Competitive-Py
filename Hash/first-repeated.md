### Problem :
Give an algorithm for printing the __first__ repeated character if there are duplicated elements in it.

### Solution :
``` python
def repeated(str) :
    size = len(str)
    count = [0] * (256)
    for i in range(size) :
        if count[ord(str[i])] == 1 :
            print(str[i])
            break
        else :
            count[ord(str[i])] += 1 
    if i == size :
        print('No repeated characters')
    return 0


if __name__ == '__main__' :
    A = ['C', 'a', 'r', 'e', 'e', 'r', 'm', 'o', 'n', 'k']
    repeated(A)


# $ python first-repeated.py
# e
```
