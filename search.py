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

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """

    # Keep track of which (x, y) positions we've already visited
    visited = []
    # Stack data structure for our DFS implementation
    # Each entry will hold ( (x, y), actionsList), where (x, y) is the current position, 
    # and actionsList is the actions needed to reach the goal) 
    stack = util.Stack()

    # Variables to hold the node we're currently at, as well as a continually-updated list of actions
    currentPos = problem.getStartState()
    actionsList = []

    if (problem.isGoalState(currentPos)):
        # No list of actions to return, we're already at the goal state
        return actionsList
    else:
        stack.push((currentPos, actionsList))
    
    while (not stack.isEmpty()):
        # Get the current pos and the actions it took to get there from our stack
        currentPos, actionsList = stack.pop()

        # If the current position node hasn't been visited, mark it as visited
        if (currentPos not in visited):
            visited.append(currentPos)

            # If this positional node is our goal state, we're done, return the actions list
            if problem.isGoalState(currentPos):
                return actionsList
            else:
                # Update our stack with the successors of our current node
                for nextPos, action, cost in problem.getSuccessors(currentPos):
                    # For each successor, push a tuple consisting of that successor's
                    # (x, y) position, as well as an updated actionsList it will take
                    # to reach that node.
                    stack.push((nextPos, actionsList + [action]))
        
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    # Keep track of which (x, y) positions we've already visited
    visited = []

    # Queue data structure for our BFS implementation
    # Each entry will hold ( (x, y), actionsList), where (x, y) is the current position, 
    # and actionsList is the actions needed to reach the goal) 
    queue = util.Queue()

    # Variables to hold the node we're currently at, as well as a continually-updated list of actions
    currentPos = problem.getStartState()
    actionsList = []

    if (problem.isGoalState(currentPos)):
        # No list of actions to return, we're already at the goal state
        return actionsList
    else:
        queue.push((currentPos, actionsList))

    while (not queue.isEmpty()):
    # Get the current pos and the actions it took to get there from our queue
        currentPos, actionsList = queue.pop()
        # If the current position node hasn't been visited, mark it as visited
        if (currentPos not in visited):
            visited.append(currentPos)

            # If this positional node is our goal state, we're done, return the actions list
            if problem.isGoalState(currentPos):
                return actionsList
            else:
                # Update our queue with the successors of our current node
                for nextPos, action, cost in problem.getSuccessors(currentPos):
                    # For each successor, push a tuple consisting of that successor's
                    # (x, y) position, as well as an updated actionsList it will take
                    # to reach that node.
                    queue.push((nextPos, actionsList + [action]))

    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
