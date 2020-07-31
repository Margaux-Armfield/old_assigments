# search_algs.py
# Margaux Armfield
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
In search_algs.py, I implemented generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.
    
    """

    start = (problem.getStartState(),[])
    goal_test = problem.isGoalState(problem.getStartState())

    # nodes have coordinates and directions
    coords = 0
    directions = 1

    current_node = start
    path = start[directions]

    # create list of visited states
    already_visited = []
    
    # create queue for fringe
    fringe = util.Stack() #LIFO for DPS

    # add start state to fringe
    fringe.push(start)

    # loop
    while not fringe.isEmpty(): # as long as there is fringe and goal test is not met
        
        #get top node from fringe
        current_node = fringe.pop()
        path = current_node[directions]
        place = current_node[coords]

        # check if current state is = to goal state
        goal_test = problem.isGoalState(place)
        if goal_test:
            return path

        #if node has not been visisted before, add node to already_visited and expand
        if place not in already_visited:
            # add current node's coordinates to already visited list
            already_visited += [place]

            #expand children
            children =  problem.getSuccessors(place)
            for child in children:
                if child[coords] not in already_visited:
                    # for each child, overwrite their directions to be previous path + child directions
                    new_path = path + [child[directions]]
                    fringe.push((child[coords], new_path))

    return path     
    

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    start = (problem.getStartState(),[])
    goal_test = problem.isGoalState(problem.getStartState())

    # nodes have coordinates and directions
    coords = 0
    directions = 1

    current_node = start
    path = start[directions]

    # create list of visited states
    already_visited = []
    
    # create queue for fringe
    fringe = util.Queue() #FIFO for BFS

    # add start state to fringe
    fringe.push(start)

    # loop
    while not fringe.isEmpty(): # as long as there is fringe and goal test is not met
        
        #get top node from fringe
        current_node = fringe.pop()
        path = current_node[directions]
        place = current_node[coords]

        # check if current state is = to goal state
        goal_test = problem.isGoalState(place)
        if goal_test:
            return path

        #if node has not been visisted before, add node to already_visited and expand
        if place not in already_visited:
            # add current node's coordinates to already visited list
            already_visited += [place]

            #expand children
            children =  problem.getSuccessors(place)
            for child in children:
                if child[coords] not in already_visited:
                    # for each child, overwrite their directions to be previous path + child directions
                    new_path = path + [child[directions]]
                    fringe.push((child[coords], new_path))

    return path

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    start = (problem.getStartState(),[])
    goal_test = problem.isGoalState(problem.getStartState())
    
    # nodes have coordinates and directions
    coords = 0
    directions = 1


    path = start[directions]
    cost = problem.getCostOfActions(path)

    # create list of visited states
    already_visited = []
    
    # create queue for fringe
    fringe = util.PriorityQueue() #FIFO for BFS

    # add start state to fringe
    fringe.push(start, cost)

    # loop
    while not fringe.isEmpty(): # as long as there is fringe and goal test is not met
        
        #get top node from fringe
        current_node = fringe.pop()
        path = current_node[directions]
        place = current_node[coords]
        cost = problem.getCostOfActions(path)

        #check if current state is = to goal state
        goal_test = problem.isGoalState(place)
        if goal_test:
            return path
        count = util.Counter()
        #if node has not been visisted before, add node to already_visited and expand
        if place not in already_visited:
            # add current node's coordinates to already visited list
            already_visited += [place]

            #expand children
            children =  problem.getSuccessors(place)
            for child in children:
                if child[coords] not in already_visited:
                    # for each child, overwrite their directions to be previous path + child directions
                    new_path = path + [child[directions]]
                    new_cost = problem.getCostOfActions(new_path)
                    fringe.push((child[coords], new_path), new_cost)

    return path

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    start = (problem.getStartState(),[])
    goal_test = problem.isGoalState(problem.getStartState())
    
    # nodes have coordinates and directions
    coords = 0
    directions = 1


    path = start[directions]
    cost = problem.getCostOfActions(path) + 0 # heuristic of start node is trivial

    # create list of visited states
    already_visited = []
    
    # create queue for fringe
    fringe = util.PriorityQueue() #FIFO for BFS

    # add start state to fringe
    fringe.push(start, cost)

    # loop
    while not fringe.isEmpty(): # as long as there is fringe and goal test is not met
        
        #get top node from fringe
        current_node = fringe.pop()
        path = current_node[directions]
        place = current_node[coords]
        cost = problem.getCostOfActions(path) + heuristic(place, problem)

        #check if current state is = to goal state
        goal_test = problem.isGoalState(place)
        if goal_test:
            return path
      
        #if node has not been visisted before, add node to already_visited and expand
        if place not in already_visited:
            # add current node's coordinates to already visited list
            already_visited += [place]

            #expand children
            children =  problem.getSuccessors(place)
            for child in children:
                if child[coords] not in already_visited:
                    # for each child, overwrite their directions to be previous path + child directions
                    new_path = path + [child[directions]]
                    # new_distance = util.manhattanDistance(current_node[coords], child[coords])
                    new_cost = problem.getCostOfActions(new_path) + heuristic(child[coords], problem)
                    fringe.push((child[coords], new_path), new_cost)

    return path


