# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"

    """
    -Using the (stack) data structure from util.py, assign with the array list for
    ( (x,y)position , path , cost ) and put those into the stack
    (#push starting position to frontier).
    -checking the stack is empty , poping out the current_node if emptyself.
    (#current node is now on the top of frontier in the stack)
    -initializing with current position especially focus on the zero index for (x,y)positions
    (#currnet position pop off from the frontier in the stack)
    -checking the current position is not in the explore notes, we have to add current position into explore nodesself.
    (#update the current position to the explore notes)
    - And we try to check passing the problem.getSuccessors as a successorNodes
     (#expand the current position and explored_nodes)
    - check lastly if that successNode index of 0 (x,y position)
     (#push tempTuple of successor to the frontier in the stack )
    """
    DFS_stack = util.Stack()
    explored_nodes = set()
    starting_position = problem.getStartState()
    NodeTuple = (starting_position, [], 0)
    DFS_stack.push(NodeTuple)

    while not DFS_stack.isEmpty():
        current_node = DFS_stack.pop()
        current_position = current_node[0]
        if problem.isGoalState(current_position):
            return path
        if current_position not in explored_nodes:
            explored_nodes.add(current_position)
            print "current Position", current_position
            print "explored_nodes" , explored_nodes
            for successorNodes in problem.getSuccessors(current_position):
                print "successorNodes", successorNodes
                if successorNodes[0] not in explored_nodes:
                    path = current_node[1]
                    path = path + [successorNodes[1]]
                    tempTuple = (successorNodes[0], path, 0)
                    DFS_stack.push(tempTuple)

    util.raiseNotDefined()


"""
Similarity with stack, use queue data structure.

-Using the (queue) data structure from util.py, assign with the array list for
( (x,y)position , path , cost ) and put those into the queue
(#push starting position to frontier).
-checking the queue is empty , poping out the current_node if emptyself.
(#current node is now on the top of frontier in the queue)
-initializing with current position especially focus on the "zero" index for (x,y)positions
(#currnet position pop off from the frontier in the queue)
-checking the current position is not in the explore notes, we have to add current position into explore nodesself.
(#update the current position to the explore notes)
- And we try to check passing the problem.getSuccessors as a successorNodes
 (#expand the current position and explored_nodes)
- check lastly if that successNode index of 0 (x,y position)
 (#push tempTuple of successor to the frontier in the queue )
"""
def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    BFS_queue = util.Queue()
    explored_nodes = set()
    starting_position = problem.getStartState()
    NodeTuple = (starting_position, [], 0)
    BFS_queue.push(NodeTuple)

    while not BFS_queue.isEmpty():
        current_node = BFS_queue.pop()
        current_position = current_node[0]
        if problem.isGoalState(current_position):
            return current_node[1]
        if current_position not in explored_nodes:
            explored_nodes.add(current_position)
            print "current Position", current_position
            print "explored_nodes" , explored_nodes
            for successorNodes in problem.getSuccessors(current_position):
                print "successorNodes", successorNodes
                if successorNodes[0] not in explored_nodes:
                    path = current_node[1]
                    path = path + [successorNodes[1]]
                    tempTuple = (successorNodes[0], path, 0)
                    BFS_queue.push(tempTuple)

    util.raiseNotDefined()

    """
    Similarity with queue, use priority queue data structure.

    -Using the (priority queue) data structure from util.py, assign with the array list for
    ( (x,y)position , path , cost ) and put those into the queue
    (#push starting position to frontier).
    -checking the stack is empty , poping out the current_node if emptyself.
    (#current node is now on the top of frontier in the priority queue)
    -initializing with current position especially focus on the "first" index for "path"
    (#currnet position pop off from the frontier in the priority queue)
    -checking the current position is not in the explore notes, we have to add current position into explore nodesself.
    (#update the current position to the explore notes)
    - And we try to check passing the problem.getSuccessors as a successorNodes
     (#expand the current position and explored_nodes)
    - check lastly if that successNode "first" index of 0 "path" along with the getCostOfActions of path function
     (#push tempTuple of successor to the frontier in the priority queue with problem.getCostOfActions )
    """

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    Uniform_Search = util.PriorityQueue()
    explored_nodes = set()
    starting_position = problem.getStartState()
    NodeTuple = (starting_position, [], 0)
    Uniform_Search.push(NodeTuple, NodeTuple[2])

    while not Uniform_Search.isEmpty():
        current_node = Uniform_Search.pop()
        current_position = current_node[0]
        if problem.isGoalState(current_position):
            return current_node[1]
        if current_position not in explored_nodes:
            explored_nodes.add(current_position)
            print "current Position", current_position
            print "explored_nodes" , explored_nodes
            for successorNodes in problem.getSuccessors(current_position):
                print "successorNodes", successorNodes
                if successorNodes[0] not in explored_nodes:
                    path = current_node[1]
                    path = path + [successorNodes[1]]
                    tempTuple = (successorNodes[0], path, problem.getCostOfActions(path))
                    Uniform_Search.push(tempTuple, problem.getCostOfActions(path))

    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

"""

    -Using the (priority queue) data structure from util.py, assign with the array list for
    ( (x,y)position , path , cost ) and put those into the queue
    (#push starting position to frontier).
    -checking the stack is empty , poping out the current_node if emptyself.
    (#current node is now on the top of frontier in the priority queue)
    -initializing with current position especially focus on the "first" index for "path"
    In astar search, two arguments is taken heuristic the search problem and main arg
    (#currnet position pop off from the frontier in the priority queue)
    -checking the current position is not in the explore notes, we have to add current position into explore nodesself.
    (#update the current position to the explore notes)
    - And we try to check passing the problem.getSuccessors as a successorNodes
     (#expand the current position and explored_nodes)
    - check lastly if that successNode "first" index of 0 "path" along with the getCostOfActions of path function
     (#push tempTuple of successor to the frontier in the priority queue with problem.getCostOfActions )
"""

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    Astar_Search = util.PriorityQueue()
    explored_nodes = set()
    starting_position = problem.getStartState()
    NodeTuple = (starting_position, [], 0)
    H_value = heuristic(starting_position,problem)
    Astar_Search.push(NodeTuple, H_value)

    while not Astar_Search.isEmpty():
        current_node = Astar_Search.pop()
        current_position = current_node[0]

        if problem.isGoalState(current_position):
            return current_node[1]
        if current_position not in explored_nodes:
            explored_nodes.add(current_position)
            print "current Position", current_position
            print "explored_nodes" , explored_nodes
            for successorNodes in problem.getSuccessors(current_position):
                print "successorNodes", successorNodes
                if successorNodes[0] not in explored_nodes:
                    path = current_node[1] + [successorNodes[1]]
                    total_cost = H_value + problem.getCostOfActions(path)
                    tempTuple = (successorNodes[0], path, total_cost)
                    Astar_Search.push(tempTuple, total_cost)
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
