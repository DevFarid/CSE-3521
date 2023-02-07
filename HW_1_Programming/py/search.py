# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util
from util import heappush, heappop, Stack, Queue

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
      """
      Returns the start state for the search problem
      """
      util.raiseNotDefined()

    def isGoalState(self, state):
      """
      state: Search state

      Returns True if and only if the state is a valid goal state
      """
      util.raiseNotDefined()

    def getSuccessors(self, state):
      """
      state: Search state

      For a given state, this should return a list of triples,
      (successor, action, stepCost), where 'successor' is a
      successor to the current state, 'action' is the action
      required to get there, and 'stepCost' is the incremental
      cost of expanding to that successor
      """
      util.raiseNotDefined()

    def getCostOfActions(self, actions):
      """
      actions: A list of actions to take

      This method returns the total cost of a particular sequence of actions.  The sequence must
      be composed of legal moves
      """
      util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s,s,w,s,w,w,s,w]

#
#   Depth First Search
#   Strategy: Expand a deepest node first.
#   Implementation: Fringe is a Last-In-First-Out stack.
#
def depthFirstSearch(problem):
    fringe = Stack()
    
    # Use set to keep track of visited nodes. All nodes should be unique & visited once, no self-node.
    visitedNodes = set()
    fringe.push( ( problem.getStartState(), [] ) ) # FORMATTED AS ((Node.x, Node.y), [LIST OF PREVIOUS ACTION THAT TOOK US TO THIS NODE.])
    
    # While the fringe is not empty
    while fringe:
        node, actions = fringe.pop() # node is (x,y), action is EMPTY on first iteration.
        # If we haven't visited this current node then:
        if node not in visitedNodes:
            visitedNodes.add(node)
            
            # If we happen to arrive at the goal, stop execution and return our current path traversed.
            if problem.isGoalState(node):
                return actions
            
            # Otherwise, let's keep searching through our successor function.
            for neighbor, action, cost in problem.getSuccessors(node):
                fringe.push((neighbor, actions + [action])) #
    # Otherwise, if fringe is empty, return None.
    return None

#
#   Breath First Search
#   Strategy: Expand a shallowest node first.
#   Implementation: Fringe is a Last-In-First-Out stack.
#   Pretty much same as DFS, except our data structure is what makes it different due to the pop() algorithm.
#
def breadthFirstSearch(problem):
    fringe = Queue() # Our fringe will be a list of tuples. Where the tuple is ((Node Coordinate), [DIRECTON/ACTION])
    
    # Use set to keep track of visited nodes. All nodes should be unique, no self-node.
    visitedNodes = set()
    fringe.push( ( problem.getStartState(), [] ) ) # FORMATTED AS ((Node.x, Node.y), [LIST OF PREVIOUS ACTION THAT TOOK US TO THIS NODE.])
    
    # While the fringe is not empty
    while fringe:
        node, actions = fringe.pop()
        # If we haven't visited this current node then:
        if node not in visitedNodes:
            visitedNodes.add(node)
            
            # If we happen to arrive at the goal, stop execution and return our current path traversed.
            if problem.isGoalState(node):
                return actions
            
            # Otherwise, let's keep searching through our successor function.
            for neighbor, action, cost in problem.getSuccessors(node):
                fringe.push( (neighbor, actions + [action]) )
    # Otherwise, if fringe is empty, return None.
    return None

#
#   Uniform Cost Search
#   Strategy: Expand the cheapest node first
#   Implementation: Fringe is a priority queue (priority based on cumulative cost)
#
def uniformCostSearch(problem):
    fringe = []
    # Use set to keep track of visited nodes. All nodes should be unique, no self-node.
    visited = set()
    heappush(fringe, ( 0, problem.getStartState(), [] ) ) # FORMATTED AS A TUPLE S.T. ( PRIORITY=COST, (Node.x, Node.y), [PREVIOUS ACTIONS])
    
    # While the fringe is not empty
    while fringe:
        cost, node, path = heappop(fringe)

        # Ignore if already visited.
        if node in visited:
            continue
        
        # If here, then probably have not visited this node.
        visited.add(node)

        # If this is the goal state, return the path.
        if problem.isGoalState(node):
            return path
        
        # Otherwise, keep traversing the short path costs until goal is found.
        for nextState, action, newCost in problem.getSuccessors(node):
            if nextState not in visited:
                # Add the previous costs, and this new cost because we want to find the best path.
                heappush(fringe, (cost + newCost, nextState, path + [action]))
                
    # Otherwise, if fringe is empty, return None.
    return None

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0
#
#   Uniform Cost Search
#   Strategy: UCS + Greedy
#   Implementation: Fringe is a priority queue (priority based on heuristic + cumulative cost). 
#
def aStarSearch(problem, heuristic=nullHeuristic):
#    h_start = heuristic(problem.getStartState(), problem)
    fringe = []
    visited = set()
    heappush( fringe, ( 0, problem.getStartState(), [] ) )
    
    # While the fringe is not empty
    while fringe:
        hOfX, node, path = heappop(fringe)

        # print("\n----\n", "h(x)=", hOfX, "\n", "NODE:",node, "\n", "PATH TRAVERSED",path, "\n","\nSUCCESSORS(",node,")=", problem.getSuccessors(node),"\n" ,"problem.getCostOfActions(",path,")",problem.getCostOfActions(path), "\n----\n")

        # Ignore if already visited.
        if node in visited:
            continue
        
        # If here, then probably have not visited this node.
        visited.add(node)

        # If this is the goal state, return the path.
        if problem.isGoalState(node):
            return path
        
        # Otherwise, keep traversing the short path costs until goal is found.
        for nextState, action, newCost in problem.getSuccessors(node):
            if nextState not in visited:
                heappush(fringe, ( problem.getCostOfActions(path + [action]) + heuristic(nextState, problem), nextState, path + [action]))
                # Computationally expensive, but we sort the heuristic + cost of actions, so that we pick the best possible node.
                fringe.sort(key=lambda x: x[0])
    # Otherwise, if fringe is empty, return None.
    return None


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
