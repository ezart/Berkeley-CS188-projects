2# search.py
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

class Node:
    def __init__(self, state,path=[],cost = 0):
        self.state = state
        self.path = path
        self.cost = cost
    


        

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

    def expand(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (child,
        action, stepCost), where 'child' is a child to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that child.
        """
        util.raiseNotDefined()

    def getActions(self, state):
        """
          state: Search state

        For a given state, this should return a list of possible actions.
        """
        util.raiseNotDefined()

    def getActionCost(self, state, action, next_state):
        """
          state: Search state
          action: action taken at state.
          next_state: next Search state after taking action.

        For a given state, this should return the cost of the (s, a, s') transition.
        """
        util.raiseNotDefined()

    def getNextState(self, state, action):
        """
          state: Search state
          action: action taken at state

        For a given state, this should return the next state after taking action from state.
        """
        util.raiseNotDefined()

    def getCostOfActionSequence(self, actions):
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
    """
    "*** YOUR CODE HERE ***"

    fringe = util.Stack()
    start = (problem.getStartState(),[])
    fringe.push(start)
    explored = set()
    while not fringe.isEmpty():
        state,path = fringe.pop()
        if problem.isGoalState(state):
            return path
        if not state in explored:
            explored.add(state)
            for child,action,stepCost in problem.expand(state):
                n_path = path.copy()
                n_path.append(action)
                fringe.push((child,n_path))
    else:
        return None

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    fringe = util.Queue()
    start = (problem.getStartState(),[])
    fringe.push(start)
    explored = set()
    while not fringe.isEmpty():
        state,path = fringe.pop()
        if problem.isGoalState(state):
            return path
        if not state in explored:
            explored.add(state)
            for child,action,stepCost in problem.expand(state):
                n_path = path.copy()
                n_path.append(action)
                fringe.push((child,n_path))
    else:
        return None

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    fringe = util.PriorityQueue()
    state = problem.getStartState()
    start = (state,[],0)
    h = heuristic(state,problem)
    fringe.push(start,h)
    explored = set()

    while not fringe.isEmpty():
        # import pdb; pdb.set_trace()
        state,path,backwardCost = fringe.pop()
        if problem.isGoalState(state):
            return path
        if state not in explored:
            explored.add(state)
            # expand node
            for child,action, stepCost in  problem.expand(state):
                actualCost = stepCost + backwardCost
                # f = g + h
                f = actualCost + heuristic(child,problem)
                # Note: make a shallow copy of path otherwise everychange you make to path will be reflected on the next
                # iteration leading to very undesirable effects
                thisPath = path.copy()
                thisPath.append(action)
                fringe.push((child,thisPath,actualCost),f)
        

    



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
