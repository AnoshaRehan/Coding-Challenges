'''
Have the function CommandLine(str) take the
str parameter being passed which represents the
parameters given to a command in an old PDP
system. The parameters are alphanumeric tokens
(without spaces) followed by an equal sign and by
their corresponding value. Multiple parameters/value
pairs can be placed on the command line with a single
space between each pair. Parameter tokens and values
cannot contain equal signs but values can contains 
spaces. The purpose of the function is to isolate
the parameters and valyes to return a list of 
parameter and value lengths. It must provide its
result in the same formagt and in the same order
by replacing each entry (tokens and values) by its
corresponding length.

For example, if str is: "SampleNumber=3234 provider=
Dr. M. Welby patient=John Smith priority=High" then
your function should return the string "12=4 8=12 
7=10 8=4" because "SampleNumber" is a 12 character
token with a 4 character value("3234") followed by 
"provider" which is an 8 character token by a 12
character value ("Dr. M. Welby"), etc.

Examples:

Input: "letters=A B Z T numbers=1 2 26 20 combine=true"
Output "7=7 7=9 6=4"

'''

def CommandLine(strParam):
	str_arr = strParam.split("=")
	right_side = []
	solutions = []
	count = 1
	for i in range(len(str_arr)):
		if str_arr[i].count(" ") > 1:
			right_side.append((str_arr[i])[:str_arr[i].rfind(' ')].strip())
			right_side.append((str_arr[i])[str_arr[i].rfind(' '):].strip())
		else:
			right_side.append(str_arr[i])
	for i in range(0, len(right_side), 2):
		sol = str(len(right_side[i])) + "=" + str(len(right_side[count]))
		solutions.append(sol)
		count = count + 2
	return " ".join(solutions)
	
print(CommandLine("letters=A B Z T numbers=1 2 26 20 combine=true"))