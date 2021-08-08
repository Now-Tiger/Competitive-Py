# ----------------------------- Duplicates in a string -------------------------------- 
# Write an efficient program to print all the duplicates and their counts in the input string .

No_of_chars = 256

def fillCharCounts(string, count) :
    for i in string :
        count[ord(i)] += 1
    return count 

def printDups(string) :
    count = [0] * No_of_chars
    count = fillCharCounts(string, count)
    k = 0
    for i in count :
        if int(i) > 1 :
            print(chr(k) + ", count = " + str(i))
        k += 1

string = "TigerTigeR"
print(printDups(string))


