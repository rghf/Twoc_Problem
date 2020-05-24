def spiral(nform, r, c):
    rowStartIndex, colStartIndex = 0,0
    while (rowStartIndex<r) and (colStartIndex<c):
        
        for i in range(rowStartIndex,c):
            print(nform[rowStartIndex][i],end=" ")
        rowStartIndex+=1

        for i in range(rowStartIndex,r):
            print(nform[i][c-1],end=" ")
        c-=1

        if rowStartIndex<r:
            for i in range(c-1,(colStartIndex-1),-1):
                print(nform[r-1][i],end=" ")
            r-=1

        if colStartIndex<c:
            for i in range(r-1,(rowStartIndex-1),-1):
                print(nform[i][colStartIndex],end=" ")
            colStartIndex+=1


nform = [[1,2,3,4,5],
        [6,7,8,9,10],
        [11,12,13,14,15]]
r = 3
c = 5
spiral(nform, r, c)
