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
    arr = arr[:-1]
    total = 0
    
    def check_combination(subarr, target):
        if target == 0:
            return True
        if not subarr:
            return False
        
        include_last = check_combination(subarr[:-1], target - subarr[-1]) # Try including the last element
        exclude_last = check_combination(subarr[:-1], target) # Try excluding the last element
        
        return include_last or exclude_last

    if check_combination(arr, maximum):
        return 'true'
    else:
        return 'false'

print(ArrayAdditionI([3, 5, -1, 8, 12]))
