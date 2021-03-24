''''

Have the function ArrayAdditionI(arr) take the array of numbers stored in arr 
and return the string true if any combination of numbers in the array can be 
added up to equal the largest number in the array, otherwise return the string 
false. For example: if arr contains [4, 6, 23, 10, 1, 3] the output should 
return true because 4 + 6 + 10 + 3 = 23. The array will not be empty, will not 
contain all the same elements, and may contain negative numbers.

Examples:

Input: [5, 7, 16, 1, 2]
Output: false

Input: [3, 5, -1, 8, 12]
Output: true

''''

def ArrayAdditionI(arr):
	arr = sorted(arr)
	maximum = arr[-1]
	arr = arr[:1]
	total = 0
	
	for i in range(len(arr)):
	
		total = total + arr[i]
		if total == maximum:
			return 'true'
		
		for j in range(len(arr)):
			if j != i:
				total = total + arr[j]
				if total == maximum:
					return 'true'
		
		for k in range(len(arr)):
			if k != i:
				total = total + arr[k]
				if total == maximum:
					return 'true'
		
		return 'false'
		
print(ArrayAdditionI([3, 5, -1, 8, 12]))