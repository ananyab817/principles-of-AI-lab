def solve_tsp(g,s):
    solution=[0,0,0,0,0]
    s=s-1
    total=max(g[0])+max(g[1])+max(g[2])+max(g[3])
    visited=[0,0,0,0]
    visited[s]=1
    for j in range(4):
            if visited[j]==1:
                continue
            else:
                visited[j]=1
                
                for k in range(4):
                    if visited[k]==1:
                        continue
                    else:
                        visited[k]=1
                        for l in range(4):
                            if visited[l]==1:
                                continue
                            else:
                                sum=g[s][j]+g[j][k]+g[k][l]+g[l][s]
                                pattern=[s,j,k,l,s]
                                if sum<=total:
                                    total=sum
                                    solution=pattern
                            visited[l]=0
                    visited[k]=0
    visited[j]=0

    return total,solution

graph=[[0,2,3,5],[7,0,3,6],[5,1,0,7],[3,1,7,0]]
stating_node=1
print(graph)
total,solution=solve_tsp(graph,stating_node)
print(f"Solution for the problem is of total cost {total} and the solution is:")
i=0
for i in range(4):
    print(f"c{solution[i]+1}",end="->")
print(f"c{solution[4]+1}")
