
"""
Harry 37.21
Berry 37.21
Tina 37.2
Akriti 41
Harsh 39

1. The lowest score is of Tina i.e 37.2
2. Scond lowest score is of these twos : Harry and Berry

3. We have to put second rankers in the alphabatical manner on the stage let say.
4. i.e Berry first then Harry 
5. Since B comes first compared to H.  

""" 
#********************************************************************************************************************************

import sys
sys.stdin = open('Compitetive/input.txt','r')
sys.stdout = open('Compitetive/output.txt', 'w')

if __name__ == '__main__':
    marksheet = []
for _ in range(0,int(input())):
    marksheet.append([input(), float(input())])

second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))



