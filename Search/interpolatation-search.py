'''
Given a sorted array of n uniformly distributed values arr[], 
write a function to search for a particular element x in the array. 

intuatuion : The Interpolation Search is an improvement over Binary Search for instances, where the values 
             in a sorted array are uniformly distributed 

workflow :  interpolation search may go to different locations according to the value of the key being searched. 
            For example, if the value of the key is closer to the last element, interpolation search is likely 
            to start search toward the end side.

formula : pos = lo + [ (x-arr[lo])*(hi-lo) / (arr[hi]-arr[Lo]) ]
'''

def interplotationSearch(arr, lo, hi, x):
    if(lo <= hi and x >= arr[lo] and x <= arr[hi]):
        pos = lo + ((hi - lo) // (arr[hi] - arr[lo])*(x - arr[lo]))
        if arr[pos] == x :
            return pos
        if arr[pos] < x :
            return interplotationSearch(arr, pos+1, hi, x)
        if arr[pos] > x :
            return interplotationSearch(arr, lo, pos-1, x)
    return -1

# Driver code to check : 
arr = [10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
n = len(arr)
x = 22
index = interplotationSearch(arr, 0, n-1, x)

if index != -1 :
    print('Element found at index ', index)
else :
    print('Element does not exist')


