def bfs(v, g, n):
  v.append(n) # check and append to visited array
  queue.append(n) # append the node to queue array

  while queue:      # looping until the queue is not empty
    m = queue.pop(0) # poping the first element
    print (m, end = " ") # printing the element

    for connection in g[m]: # a for loop to find out the connections or neughbours of the element
      if connection not in v: # checking f the the connection is already visited by the program
        v.append(connection) # marking the connection element as visited if  not already visited
        queue.append(connection) # appending the connection to the queue

g = {
  '5' : ['1','7','3'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : [],
  '1' : ['6'],
  '6' : [],
}  # declaring the graph
v = [] # visited array to note if the nodes are visited are not
queue = [] # queue to contain and perform bfs search
print("Bredth first Search results for the above graph is :")
bfs(v, g, '5') # calling the function

