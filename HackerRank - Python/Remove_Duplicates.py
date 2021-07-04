'''
    problem statement : 
    Given a string S, the task is to remove all the duplicates in the given string. 
'''
def unique(s):
    st = ""
    length = len(s)
    for i in range(length):
        c = s[i]
        '''
        if c is present in the str, it returns the index of c
        else return -1
        ''' 
        if c not in st:
            st += c
    return st

# Driver code :
if __name__ == "__main__":
    s = "needforspeed"
    print(unique(s))

