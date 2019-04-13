
Name : Shan Kwan Cho
SID  : 917599337

Description:

There are eight questions in this assignment.

For question 1, we populated the edges and variableDomainsDict. We then iterate through each housePos and pass them in gameState.getHouseWalls to get obsPos. We then use the obsPos to calculate obsVar, as shown in the ‘hint’ portion of the code. We use this obsVar to update edges and variableDomainsDict. 

For question 2a, we pretty much copy fillXCPT method for fillYCPT. As suggested in the HTML page, fillXCPT was similar to fillYCPT.

For question 2b, we are to implement fillObsCPT method. For this we iterate through possible housePos and use them to get obsPos. We then iterate through each obsPos. For each obsPos we calculate obsVar and use that to get obsFactor. From the obsFactor we use getAllPossibleAssignmentDiscts() function to get assignment. We then iterate through each assignment to test if the current position is food or ghost. If they are we then setProbability function to set the probability for that obsFactor. Lastly we use setCPT using obsVar and obsFactor. 

For question 3, we are to implement joinFactors. To do so, we first create an empty set of unconditional and conditional sets. Then we iterate through each factor of the argument factors to get the unconditional and conditional sets. We then use those sets as well as the variableDomainsDict to get a new factor. Next we get possible assignments from it using getAllPossibleAssignmentDict() function. We then iterate through each assignment and calculate the probability, which we set it to the new factor using setProbability() method. 

For question 4, we are to eliminate given variable from a factor. To do this first we get conditioned and unconditioned variables of the factor. We then eliminate the eliminationVariable off the unconditional set by discarding it. We then delete the eliminationVariable off variableDomainsDict of the factor. We form a new factor using the updated conditional, unconditional, and variableDomainsDict. Next is to calculate the new probabilities for the assignments of the new factor. To do this, we iterated through possible assignments of the new factor and for each assignment, we iterate through the eliminationVariable set. Using the values of the eliminationVariable set, we find the probability of the given assignment and the current value of eliminationVariable set and accumulate them. After iterating through the eliminationVariable set for a given assignment, we should get an accumulated sum of the probability of the current assignment iterated through the eliminationVariable set. We then set the probability of that assignment of the new factor using the updated probability. 

For question 5, we first have to find unconditioned variables with exactly one entry in their domain, as stated in the comments. To do so, we first have to get the conditioned and unconditioned variables. Then, we iterate through the unconditioned variables to see if the length of the variableDomainsDict of that unconditioned variable is 1 (single entry). If so, we add that unconditioned variable to a list called oneDomain. Once we get oneDomain list, we then iterate through it and add them to conditioned and remove them from unconditioned. We then form a new factor using the updated list of conditioned and unconditioned, as well as variableDomainsDict. We also need to calculate the probability
Sum of the factor. If the sum = 0, we are to return None. We then iterate through assignments in the new factor to calculate the newProb and use that to update the probability of the new factor.

For question 6, we get all the factors where we know the evidence variables in order to able to reduce the size of the tables passing by evidenceDict through BayesNet.getAllCPTsWithEvidence which return all conditional probability. And then we join all those factors by eliminationOrder and then eliminate and normalize the joinFactors.

For question 7, to find the most portable position of food house, we need to call the variable elimination method include foodHouse, ghostHouse and etc such as inference.inferenceByVariableElimination(bayesNet, ['foodHouse', 'ghostHouse'], evidence, eliminationOrder) and from dict factor.getProbability(dict).

For question 8a, To get value of perfect information, assign those left and right houses by getting joint distribution of inference procedure and compute rushing of left and right expected value. 
For question 8b, we use the method called getExplorationProbsAndOutcomes of the form probability and do the formula of expectedValue += prob * max(self.computeEnterValues(explorationEvidence, enterEliminationOrder)) and return the expectedValue

I discuss the idea and implementation of this assignment with Naylin Min SID:917101684. 
The Total time I spent for this project is more than 4 days. It took time for me to understand how the functions we are to used worked. The materials are quite a bit challenging however I enjoyed searching new things especially the Bayes Nets which is essential/ fundamental theory for machine learning. 

