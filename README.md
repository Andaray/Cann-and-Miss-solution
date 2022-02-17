# Cann-and-Miss-solution
I wasn't able to fully finish the assignment because I could not figure how to properly represent the individual steering the boat. Additionally, I spent most of the time trying to solve that problem that I couldn't attempt the A8 search.




Representation of the states-

I represented a state as a list of integers where the first 2 integers represent 
the number of missionaries and cannibals on the left side, the middle integer
represents which side the boat is one, and the last 2 integers represent the 
number of missionaries and cannibals on the right side.



How did you encode moves-

I imported the numpy library so that I could adjust the individual integer
in my representation of a state. I made a list of possible moves and incorporated
a loop to go through them and check whether the move is valid according
to the constraints



Question (a)



Question (b)



Pseudo-code for BFS-

Create 2 lists (one for visited nodes and another for unvisited nodes)

Queue the intialized state in the list of unvisited nodes

Create while loop to traverse unvisited nodes
- if the final node matches the desired end state, get the path
- add that node to the visited list and print it's information

- Add copy of node from the returned path to the list of visited nodes
	 	- print the information
- run gen_successors to get the next nodes
- check to see if there are any unvisited nodes and append them to the list



A*



Sample output (my relaxed solution)-

(3, 3, 0, 0, 0)
[2 2 1 1 1]
[1 1 0 2 2]
[0 0 1 3 3]



Acknowledge any help-

I worked on this project with Renan and Spencer. I collaborated with their
team to strategize potential ways of representing the states, nodes, and more.
The program I wrote is my own, but I imagine that our methods are very similar.
Additionaly, there are many functions in my program that were taken from the 
goat, wolf, and cabbage example that was provided to the class.
