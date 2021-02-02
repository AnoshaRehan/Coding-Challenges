'''
Minimum Difference Sum

Given an array od n integers, rearrange them so that
the sum of the absolute differences of all adjacent
elements is minimized. Then, compute the sum of
those absolute differences.

Example
n = 5
arr = [1, 3, 3, 2, 4]

If the list is rearranged as arr'=[1, 2, 3, 3, 4], the
absolute differences are |1 - 2| = 1, |2 - 3| = 1, |3 -
3| = 0, |3 - 4| = 1. The sum of those differences is 1
+ 1 + 0 + 1 = 3.
'''


# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.


def minDifference(arr):
	abs_sum = 0
	sorted_arr = sorted(arr)
	for i in range(len(sorted_arr)-1):
		abs_sum = abs_sum + abs(sorted_arr[i]-sorted_arr[i+1])
	return abs_sum