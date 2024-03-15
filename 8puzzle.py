def puzzlesorting(node,goal,pos):
    final=0
    f_pos=0
    x=pos[0]
    y=pos[1]
    move=[[x,y-1],[x,y+1],[x-1,y],[x+1,y]]
    for i in range(3):
        for j in range(3):
            if node[i][j]!=goal[i][j]:
                final+=1
            else:
                f_pos+=1
    if final==0:
        return 1
    for i in range(4):
        if move[i][0]>=0 and  move[i][0]<3 and  move[i][1]>=0 and  move[i][1]<3:
            newnode=node
            temp=newnode[x][y]
            newnode[x][y]=newnode[move[i][0]][move[i][1]]
            newnode[move[i][0]][move[i][1]]=temp

            output=puzzlesorting(newnode,goal,move[i])
    

def puzzle8problem(start,goal):
    blank_pos=[0,0]
    x=0
    onpos=0
    print("The computer the cureently solving the 8 puzzle problem using huerisitics methods")
    for i in range(3):
        for j in range(3):
            if start[i][j]=='_':
                blank_pos[0]=i
                blank_pos[1]=j
            x=puzzlesorting(start,goal,blank_pos)
    if x==0:
        print("Goal position cannot be achived")
    return
        
start=[[1,4,3],[2,5,'_'],[6,7,8]]
goal=[[1,2,3],[4,5,6],[7,8,'_']]

puzzle8problem(start,goal)
