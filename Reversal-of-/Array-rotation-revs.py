'''
Write a function rotate(arr[], d, n) that rotates arr[] of size n by d elements. 

Example : 

Input :  arr[] = [1, 2, 3, 4, 5, 6, 7]
         d = 2
Output : arr[] = [3, 4, 5, 6, 7, 1, 2] 
'''
# Function to reverse array[] from index start to end.

def reverseArray(arr, start, end):
	while (start < end):
		temp = arr[start]
		arr[start] = arr[end]
		arr[end] = temp
		start += 1
		end = end-1


# Function to left rotate arr[] of size n by d 
def leftRotate(arr, d):

	if d == 0:
		return
	n = len(arr)
	# in case the rotating factor is
	# greater than array length
	d = d % n
	reverseArray(arr, 0, d-1)
	reverseArray(arr, d, n-1)
	reverseArray(arr, 0, n-1)

# Function to print array :
def printArray(arr):
	for i in range(0, len(arr)):
		print(arr[i]),

# Testing above function by providing an array :
arr = [1, 2, 3, 4, 5, 6, 7]
n = len(arr)
d = 2

leftRotate(arr, d) # Rotate array by 2
printArray(arr)


