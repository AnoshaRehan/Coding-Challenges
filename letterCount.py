'''
Have the function LetterCountI(str) take the str parameter being passed
and return the first word with the greatest number of repeated letters. For 
example: "Today, is the greatest day ever!" should return 'greatest' because
it has 2 e's (and 2 t's) and it comes before 'ever' which also has 2 e's. If
there are no words with repeating letters return -1. Words will be separated
by spaces.


Example:
	Input: "Hello apple pie"
	Output: Hello
	
	Input: "No words"
	Output: -1
'''

def LetterCountI(strParam):
	str_arr = strParam.split()
	count = 0
	greatest_length = '-1'
	
	for i in range(len(str_arr)):
		for j in range(len(str_arr[i])):
			new_count = 0
			for k in range(j+1, len(str_arr[i])):
				if str_arr[i][j] == str_arr[i][k]:
					new_count+=1
			if new_count > count:
				count = new_count
				greatest_length = str_arr[i]
	return greatest_length
	
print(LetterCountI("Hello apple pie"))