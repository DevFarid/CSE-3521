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
from util import heappush, heappop
from collections import deque
import heapq
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
#
def depthFirstSearch(problem):
    # Implementation: Fringe is a Last-In-First-Out stack.
    fringe = []
    
    # Use set to keep track of visited nodes. All nodes should be unique, no self-node .
    visitedNodes = set()
    fringe.append((problem.getStartState(), []))
    
    # While the fringe is not empty
    while fringe:
        node, actions = fringe.pop()
        if node not in visitedNodes:
            visitedNodes.add(node)
            
            if problem.isGoalState(node):
                return actions
            
            for neighbor, action, cost in problem.getSuccessors(node):
                fringe.append((neighbor, actions + [action]))
    # Otherwise, if fringe is empty or any other unexpected error, return None.
    return None

#
#   Breath First Search
#   Strategy: Expand a shallowest node first.
#
def breadthFirstSearch(problem):
    # Implementation: Fringe is a Last-In-First-Out stack.
    fringe = deque()
    
    # Use set to keep track of visited nodes. All nodes should be unique, no self-node .
    visitedNodes = set()
    fringe.append((problem.getStartState(), []))
    
    # While the queue is not empty
    while fringe:
        node, actions = fringe.popleft()
        if node not in visitedNodes:
            visitedNodes.add(node)
            if problem.isGoalState(node):
                return actions
            
            for neighbor, action, cost in problem.getSuccessors(node):
                fringe.append((neighbor, actions + [action]))
    # Otherwise, if fringe is empty or any other unexpected error, return None.
    return None

#
# Expand the cheapest node first
#
#
def uniformCostSearch(problem):
    # Create a priority queue for UCS
    queue = []
    # Create a set to track visited nodes
    visitedNodes = set()
    # Add the start state to the queue with a cost of 0
    heapq.heappush(queue, (0, problem.getStartState(), []))
    # While the queue is not empty
    while queue:
        # Dequeue a node from the queue
        cost, node, actions = heapq.heappop(queue)
        
        if node not in visitedNodes:
            visitedNodes.add(node)
            
            if problem.isGoalState(node):
                return actions
            
            for neighbor, action, step_cost in problem.getSuccessors(node):
                heapq.heappush(queue, (cost + step_cost, neighbor, actions + [action]))
    # If the search fails to find the goal, return None
    return None

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """
    YOUR CODE HERE
    """
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
