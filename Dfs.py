def dfs(v, g, n):
  v.append(n) # check and append to visited array
  stack.append(n)  # append the node to stack array

  while stack:       # looping until the stack is not empty
    m = stack.pop()  # poping the top element
    print (m, end = " ") # printing the element

    for connection in g[m]:  # a for loop to find out the connections or neughbours of the element
      if connection not in v: # checking f the the connection is already visited by the program
        v.append(connection)# marking the connection element as visited if  not already visited
        stack.append(connection) # appending the connection to the stack

g = {
  '5' : ['3','7','1'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : [],
  '1' : ['6'],
  '6' : [],
}# declaring the graph

v = [] # visited array to note if the nodes are visited are not
stack = []  # stack to contain and perform dfs search

print("Depth first Search results for the above graph is :")
dfs(v, g, '5') # calling the function
