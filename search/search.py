# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and Pieter 
# Abbeel in Spring 2013.
# For more info, see http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html

"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
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

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    #util.Stack() = LIFO for DFS
    #travel down path until end of line unlike BFS, backtrack until there is another path

    visited = []

    frontier = util.Stack()
    frontier.push( (problem.getStartState(), []) )  

    while not frontier.isEmpty():
        node,actions = frontier.pop()

        if problem.isGoalState(node):
            return actions

        visited.append(node)

        for coord,direction,cost in problem.getSuccessors(node):
            if not coord in visited:
                frontier.push((coord, actions + [direction]))

    return []

#aima.eecs.berkeley.edu/slides-pdf
 
def breadthFirstSearch(problem):
    # #Queue = FIFO
    # #explore nearest unexpanded node; aka "working on X (current node)"
    # frontier = util.Queue()

    visited = [problem.getStartState()]
    frontier = util.Queue()
    frontier.push( (problem.getStartState(), []) ) 

    while not frontier.isEmpty():
        node,actions = frontier.pop()
        
        if problem.isGoalState(node):
            return actions

        for coord,direction,cost in problem.getSuccessors(node):
            if not coord in visited:
                frontier.push((coord, actions + [direction]))
            visited.append(coord)

    return []





def uniformCostSearch(problem):
    closedset = []
    frontier = util.PriorityQueue()
    frontier.push( (problem.getStartState(), []), 0)
    expanded_nodes = []
    while not frontier.isEmpty():
        node, actions = frontier.pop()

        if problem.isGoalState(node):
            return actions
        closedset.append(node)


        for coord, direction, cost in problem.getSuccessors(node):
            if not coord in closedset:
                if not coord in expanded_nodes:
                    expanded_nodes.append(coord)
                    new_actions = actions + [direction]
                    score = problem.getCostOfActions(new_actions)
                    expanded_nodes.append(score)               
                    frontier.push( (coord, new_actions), score)
                elif coord in expanded_nodes:
                    new_actions = actions + [direction]
                    score = problem.getCostOfActions(new_actions)
                    if expanded_nodes[expanded_nodes.index(coord)+1] > score:
                        frontier.push((coord, new_actions),score)




    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    closedset = []
    frontier = util.PriorityQueue()
    frontier.push( (problem.getStartState(), []), heuristic(problem.getStartState(), problem))
    expanded_nodes = []
    while not frontier.isEmpty():
        node, actions = frontier.pop()

        if problem.isGoalState(node):
            return actions
        closedset.append(node)


        for coord, direction, cost in problem.getSuccessors(node):
            if not coord in closedset:
                if not coord in expanded_nodes:
                    expanded_nodes.append(coord)
                    new_actions = actions + [direction]
                    score = problem.getCostOfActions(new_actions) + heuristic(coord, problem) 
                    expanded_nodes.append(score)               
                    frontier.push( (coord, new_actions), score)
                elif coord in expanded_nodes:
                    new_actions = actions + [direction]
                    score = problem.getCostOfActions(new_actions) + heuristic(coord, problem) 
                    if expanded_nodes[expanded_nodes.index(coord)+1] > score:
                        frontier.push((coord, new_actions),score)




    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

"""
#******************* WRITTEN QUESTIONS PORTION *******************#


1. In terms of a depth first search, yes; for example, instead of immediately turning
left ("down") which takes a shorter path, pacman takes the long way around the maze. 
This makes sense in terms of DFS because this search takes each initial path as far as 
it can go as opposed to the BFS "check on all neighbors" method.  Therefore pacman
explores a path which is less efficient but takes him to a goal state in the end.

2.  No; these algorithms are designed to traverse all paths, UNLESS we hit a goal 
state.  Once pacman finds this the maze is done.  

3.  Not necessarily; as I said in question one, the way DFS is designed leads pacman 
(for example in medium maze) down a straight path that eventually leads him to a 
goal state.  He ends up finding it, so the game ends, but there are shorter paths 
that DFS doesn't find because of its design.

4.  Open Maze: DFS
    Open Maze is bad news for DFS pacman.  He is designed to take each path as far as 
    he can to its conclusion, which means that he traverses the maze left to right 
    seeking the goal state: he goes all the way left, down one, then back to the right.
    score:212  nodes expanded: 806

    BFS:
    BFS solves the maze relatively quickly; his strategy to check all neighbors results
    in a wide swath of explored nodes (as indicated by the color), but leads his to the
    actual goal in shorter time.
    score:456  nodes expanded: 682

    UCS: 
    UCS goes down, left, down, left in big straight lines.  It is checking the score to
    take the minimum path first. 
    score:456  nodes expanded: 682

    aStar:
    When combining the heuristic with a search we see astar get the optimal path to the goal,
    which is the same as UCS.  This is because it combines the heuristic with the cost score
    to prevent it going down incorrect paths.
    score:456  nodes expanded: 682

"""

