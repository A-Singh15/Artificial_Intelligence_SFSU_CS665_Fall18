# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        #return successorGameState.getScore()
        """
        print("SuccessorGameState: ", successorGameState)
        print("newPos: ", newPos)
        print("newFood: ", newFood)
        print("newGhostStates: ", newGhostStates)
        print("newScaredTimes: ", newScaredTimes)
        """

        val = successorGameState.getScore() #get score as values

        dis_To_Ghost = []
        for ghosts in newGhostStates: # get distance function called manhattanDistance(newPos,ghosts position)
            dis_To_Ghost.append(manhattanDistance(newPos,ghosts.getPosition()))
        minDistToGhost = min(dis_To_Ghost)
        if minDistToGhost > 0:
            val -= 2.0 / minDistToGhost

        dist_To_Food = []
        for food in newFood.asList():
            dist_To_Food.append(manhattanDistance(newPos, food)) # get distance function called manhattanDistance(newPos, food position)
        minDistToFood = float('inf')
        if len(dist_To_Food):
            minDistToFood = min(dist_To_Food)
        if minDistToFood > 0:
            val += 1.0 / minDistToFood

        return val
        """
        minDistToGhost = 999999999
        for ghostState in newGhostStates:
            distGhost = manhattanDistance(newPos, ghostState.getPosition()) #give postion to the ghost from pacman
            if distGhost < minDistToGhost and distGhost > 0:
                minDistToGhost = distGhost # the new distance of ghost from pacman
        print minDistToGhost

        minDistToFood = 999999999
        distancesToFood = [manhattanDistance(newPos, x) for x in newFood.asList()]
        if len(distancesToFood):
            minDistToFood = min(distancesToFood)

        reci_val = (1.0 / minDistToFood) - (2.0 / minDistToGhost)
        eval = successorGameState.getScore() + reci_val
        return eval
        """



def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
        """
        "*** YOUR CODE HERE ***"
        # Pacman turn initially
        # return argmax pac's action index1
        self.countAgents = gameState.getNumAgents()
        pacman_Action=self.Max_Value(gameState, 0,0)
        return pacman_Action[1]


  # get_value(gameState) func
  # check 3 states: 1. if terminal state -> return state Utility
  #                 2. if next agent is maximum -> return max_val of gamestate
  #                 3. if next agent is minimum -> return min_val of gamestate

    def get_Value(self,gameState,agentIndex,current_Depth):
        "Terminal Test"
        if current_Depth>=self.countAgents*self.depth or gameState.isWin() or gameState.isLose():
            return self.evaluationFunction(gameState)
        elif agentIndex==0:    ## agentindex==0 is pacman
            return self.Max_Value(gameState, agentIndex, current_Depth)[0]   ## [0] is bestValue,[1] is bestAction
        else:
            return self.Min_Value(gameState, agentIndex, current_Depth)


  #  For Max_Value func, pass values(self,gameState,agentIndex,current_Depth) into the func
  #  method call legalActions of the Agentindex=0
  #  initialize best_max_val as negative infinity
  #  Use for loop to check each successorstate of the gamestate
  #  Pass by best_max_val=max(getValue(succesosr)) to return value
  #  best_Action return getAction

    def Max_Value(self,gameState,agentIndex,current_Depth):
        legalActions=gameState.getLegalActions(agentIndex)
        best_Max_Value=float('-inf')
        bestAction='Stop'
        for action in legalActions:
            successorState=gameState.generateSuccessor(agentIndex,action)
            successorDepth=current_Depth+1
            depth_index = successorDepth % self.countAgents # iterate to the agent according to depthIndex (if agent is 2 % 3 which is remainder 2)
            value=self.get_Value(successorState, depth_index, successorDepth)
            if value>best_Max_Value:
                best_Max_Value=value
                best_Action=action
        return [best_Max_Value,best_Action]


  #  For Min_Value func, pass values(self,gameState,agentIndex,current_Depth) into the func
  #  method call legalActions of the Agentindex=0
  #  initialize best_min_val as positive infinity
  #  Use for loop to check each successorstate of the gamestate
  #  Pass by best_min_val=max(getValue(succesosr)) to return value

    def Min_Value(self,gameState,agentIndex,current_Depth):
        legalActions=gameState.getLegalActions(agentIndex)
        best_Min_Value=float("inf")
        for action in legalActions:
            successorState=gameState.generateSuccessor(agentIndex,action)
            successorDepth=current_Depth+1
            depth_index = successorDepth % self.countAgents# iterate to the agent according to depthIndex (if agent is 2 % 3 which is remainder 2)
            value=self.get_Value(successorState, depth_index, successorDepth)
            if value<best_Min_Value:
                best_Min_Value=value
        return best_Min_Value


class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        # Pacman turn initially, initilize alpha, beta
        # return argmax pac's action index1
        alpha=float('-inf')
        beta=float('inf')
        self.countAgents = gameState.getNumAgents()
        pacmanAction=self.Max_Value(gameState, 0,0,alpha,beta)
        return pacmanAction[1]

  # get_value(self,gameState,agentIndex,currentDepth,alpha,beta) func
  # check 3 states: 1. if terminal state -> return state Utility
  #                 2. if next agent is maximum -> return max_val of gamestate->alpha,beta
  #                 3. if next agent is minimum -> return min_val of gamestate->alpha,beta

    def getValue(self,gameState,agentIndex,currentDepth,alpha,beta):
        self.countAgents = gameState.getNumAgents()
        "Terminal Test"
        if currentDepth>=self.countAgents*self.depth or gameState.isWin() or gameState.isLose():
            return self.evaluationFunction(gameState)
        elif agentIndex==0:
            return self.Max_Value(gameState,agentIndex,currentDepth,alpha,beta)[0]   ## [0] is bestValue,[1] is bestAction
        else:
            return self.Min_Value(gameState,agentIndex,currentDepth,alpha,beta)[0]

  #  For Max_Value func, pass values(self,gameState,agentIndex,current_Depth,alpha,beta) into the func
  #  method call legalActions of the Agentindex=0
  #  initialize best_max_val as negative infinity
  #  Use for loop to check each successorstate of the gamestate
  #  Pass by best_max_val=max(getValue(succesosr)) to return value
  #  check if best_max_val>beta: return best_max_val
  #  best_Action return getAction

    def Max_Value(self,gameState,agentIndex,currentDepth,alpha,beta):
        legalActions=gameState.getLegalActions(agentIndex)
        best_Max_Value=float('-inf')
        bestAction='Stop'
        for action in legalActions:
            successorState=gameState.generateSuccessor(agentIndex,action)
            successorDepth=currentDepth+1
            depth_index = successorDepth % self.countAgents # iterate to the agent according to depthIndex (if agent is 2 % 3 which is remainder 2)
            value=self.getValue(successorState,depth_index, successorDepth,alpha,beta)
            if value>best_Max_Value:
                best_Max_Value=value
                bestAction=action
                if best_Max_Value>beta:
                    return [best_Max_Value,bestAction]
                alpha=max(alpha, best_Max_Value)
        return [best_Max_Value,bestAction]


  #  For Min_Value func, pass values(self,gameState,agentIndex,current_Depth,alpha,beta) into the func
  #  method call legalActions of the Agentindex=0
  #  initialize best_min_val as positive infinity
  #  Use for loop to check each successorstate of the gamestate
  #  check if best_min_val>alpha: return best_min_val-> min(beta,best_min_val)
  #  Pass by best_min_val=max(getValue(succesosr)) to return value

    def Min_Value(self,gameState,agentIndex,currentDepth,alpha,beta):
        legalActions=gameState.getLegalActions(agentIndex)
        best_Min_Value=float("inf")
        for action in legalActions:
            successorState=gameState.generateSuccessor(agentIndex,action)
            successorDepth=currentDepth+1
            depth_index = successorDepth % self.countAgents # iterate to the agent according to depthIndex (if agent is 2 % 3 which is remainder 2)
            value=self.getValue(successorState,depth_index,successorDepth,alpha,beta)
            if value<best_Min_Value:
                best_Min_Value=value
                if best_Min_Value<alpha:
                    return [best_Min_Value]
                beta=min(beta,best_Min_Value)
        return [best_Min_Value]


class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
        # Pacman go first
        self.countAgents = gameState.getNumAgents()
        pacmanAction=self.Max_Value(gameState, 0,0)
        return pacmanAction[1]

  # get_value(gameState) func
  # check 3 states: 1. if terminal state -> return state Utility
  #                 2. if next agent is maximum -> return max_val of gamestate
  #                 3. if next agent is Expected_Value -> return expectedValue of gamestate

    def getValue(self,gameState,agentIndex,currentDepth):
        self.countAgents = gameState.getNumAgents()
        "Terminal Test"
        if currentDepth>=self.countAgents*self.depth or gameState.isWin() or gameState.isLose():
            return self.evaluationFunction(gameState)
        elif agentIndex==0:
            return self.Max_Value(gameState,agentIndex,currentDepth)[0]   # [0] is bestValue
        else:
            return self.Expected_Value(gameState,agentIndex,currentDepth)


  #  For Max_Value func, pass values(self,gameState,agentIndex,current_Depth) into the func
  #  method call legalActions of the Agentindex=0
  #  initialize best_max_val as negative infinity
  #  Use for loop to check each successorstate of the gamestate
  #  Pass by best_max_val=max(getValue(succesosr)) to return value
  #  best_Action return getAction

    def Max_Value(self,gameState,agentIndex,currentDepth):
        legalActions=gameState.getLegalActions(agentIndex)
        best_Max_Value=float('-inf')
        bestAction='Stop'
        for action in legalActions:
            successorState=gameState.generateSuccessor(agentIndex,action)
            successorDepth=currentDepth+1
            depth_index = successorDepth % self.countAgents # iterate to the agent according to depthIndex (if agent is 2 % 3 which is remainder 2)
            value=self.getValue(successorState, depth_index, successorDepth)
            if value>best_Max_Value:
                best_Max_Value=value
                bestAction=action
        return [best_Max_Value,bestAction]    # bestMaxValue-> getValue(), bestAction-> getAction


  #  ForExpected_Value func, pass values(self,gameState,agentIndex,current_Depth) into the func
  #  method call legalActions of the Agentindex=0
  #  initial expectedUtility[]
  #  Use for loop to check each successorstate of the gamestate
  #  Pass by expectedvalue=sum(expectedUtility*probability)-> return expectedvalue

    def Expected_Value(self,gameState,agentIndex,currentDepth):
        legalActions=gameState.getLegalActions(agentIndex)
        expectedUtility=[]
        for action in legalActions:
            successorState=gameState.generateSuccessor(agentIndex,action)
            successorDepth=currentDepth+1
            depth_index = successorDepth % self.countAgents # iterate to the agent according to depthIndex (if agent is 2 % 3 which is remainder 2)
            value=self.getValue(successorState, depth_index, successorDepth)
            expectedUtility.append(value)
        expectedValue=sum(expectedUtility)*1.0/len(expectedUtility)
        return expectedValue

def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()

    new_pac_pos=currentGameState.getPacmanState()
    newPos=currentGameState.getPacmanPosition()
    score =scoreEvaluationFunction(currentGameState)

    dis_To_Ghost = []
    dist_To_Food = []

    Scared_Index=0.0
    better_evaluate_Score=0.0

    food_weight=0.0
    ghost_weight=0.0

    food_states = currentGameState.getFood()
    for food in food_states.asList():
        dist_To_Food.append(1.0/(manhattanDistance(newPos,food)))
    if len(dis_To_Ghost):
        food_weight = max(dist_To_Food)

    ghost_states = currentGameState.getGhostStates()
    for ghost in ghost_states:
        if ghost.scaredTimer == 0:
            Scared_Index = Scared_Index + 1
        dis_To_Ghost.append(1.0/(manhattanDistance(newPos, ghost.getPosition())))
    if len(dis_To_Ghost):
        ghost_weight = min(dis_To_Ghost)
    better_evaluate_Score = score + food_weight - ghost_weight - Scared_Index

    return better_evaluate_Score


# Abbreviation
better = betterEvaluationFunction
