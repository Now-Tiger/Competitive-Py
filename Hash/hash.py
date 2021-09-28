
# -------------------------------------------- Simple hash function --------------------------------------------

def hash(data) :
    counter = 1
    sum = 0
    for d in data :
        sum += counter * ord(d)
    return sum % 256

if __name__ == '__main__' :
    items = ['linux', 'harvard', 'bim', 'solar', 'tubes' , 'softmax']
    for i in items : 
        print (f'{i, hash(i)}')


# $ python hash.py 
# ('linux', 48)
# ('harvard', 232)
# ('bim', 56)     
# ('solar', 33)   
# ('tubes', 35)
# ('softmax', 2)