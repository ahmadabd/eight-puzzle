# eight-puzzle
This code solves eight puzzle by ASTAR algorithm.<br>
For running this program ,run AStar.py file by python3 interpreter.
## One important thing is:
Final is:[['1','2','3']['8','0','4']['7', '6', '5']]<br> 
so your input values should be same as final values.<br>
and '0' is empty house.

### A* algorithm features:
The A* algorithm combines features of uniform-cost search and pure heuristic search to efficiently compute optimal solutions.<br> 
A* algorithm is a best-first search algorithm in which the cost associated with a node is f(n) = g(n) + h(n), where g(n) is the cost of the path from the initial state to node n and h(n) is the heuristic estimate or the cost or a path from node n to a goal. Thus, f(n) estimates the lowest total cost of any solution path going through node n. At each point a node with lowest f value is chosen for expansion. Ties among nodes of equal f value should be broken in favor of nodes with lower h values. The algorithm terminates when a goal is chosen for expansion.

