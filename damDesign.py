mud = 0    
for i in range(len(wallPositions)-1):
        if(wallPositions[i] < wallPositions[i+1]-1):
            height = abs(wallHeights[i+1]-wallHeights[i])
            gap = wallPositions[i+1] - wallPositions[i]-1
            temp = 0
            if gap > height:
                count = max(wallHeights[i+1], wallHeights[i])+1
                gap_left = gap - height -1
                temp = count + gap_left/2
            else:
                temp = min(wallHeights[i+1], wallHeights[i])+gap
            mud = max(mud, temp)    
return int(mud)