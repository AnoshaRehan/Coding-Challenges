'''
Acknowldgement: https://github.com/d0ppler1977/coderbyte/blob/master/medium/SeatingStudents.js

The function SeatingStudents(arr) read the array of integers stored in arr which will be in the 
following format: [K, r1, r2, r3, ...] where K represents the number of desks in a classroom, 
and the rest of the integers in the array will be in sorted order and will represent the desks
 that are already occupied. All of the desks will be arranged in 2 columns, 
 where desk #1 is at the top left, desk #2 is at the top right, desk #3 is below #1, desk #4 is below #2, etc. 
 Your program should return the number of ways 2 students can be seated next to each other. 
 This means 1 student is on the left and 1 student on the right, or 1 student is directly above or below the other student.
 
'''


def SeatingStudents(arr):

  K = arr[0]
  occupied = arr[1:]

  rows = int(K/2)

  seats = []
  x = 0
  
  for i in range(rows):
    seats.append([])
    for j in range(2):
      if((x+1) in occupied):
        full_seat = True
      else:
        full_seat = False
      seats[i].append(str(full_seat))
      x+=1

  seating = 0
  for i in range(rows-1):
    if((seats[i][0] == str(False)) and (seats[i][1] == str(False))):
      seating+=1

    if((seats[i][0] == str(False)) and (seats[i+1][0] == str(False))):
      seating+=1

    if((seats[i][1] == str(False)) and (seats[i + 1][1] == str(False))):
      seating+=1
  
  if((seats[rows - 1][0] == str(False)) and (seats[rows - 1][1] == str(False))):
    seating+=1
  return seating

 
print(SeatingStudents([12, 2, 6, 7, 11]))
