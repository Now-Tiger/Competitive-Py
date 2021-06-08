
# Given example solution : 
# Sample Input : 
1
1
1
2

# Outpute :
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]


# To perform :
# Sample input :
2
2
2
2

# Output :
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2], [1, 0, 0], [1, 0, 2], [1, 1, 1], 
 [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], 
 [2, 2, 0], [2, 2, 1], [2, 2, 2]]

# **************************** Program : **************************************

if __name__ == '__main__':
    x, y, z, n = (int(input()) for _ in range(4))
    print([[a,b,c] for a in range(0, x+1) for b in range(0, y+1) for c in range(0, z+1) if a+b+c != n])
    
    
# ************************* Alternate methode : ******************************

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    final_list =[]
    for i in range(1+x):
        for j in range(y+1):
            for k in range(1+z):
                if i+j+k!=n:
                    temp=[i,j,k]
                    final_list.append(temp)
                else:
                    continue
    print(final_list)
          
          
                  
    
