
Name : Shan Kwan Cho
SID  : 917599337

Description:

There are five questions in this assignment.

The first question is asking about implementing	the reflex agent for Pacman. The hard part of this question is extracting food locations and ghost location with the Pacman. In this question calling manhanttanDistance func from util files to implement food and ghost location from the Pacman and implement with reciprocal values of those food and ghost.

The second question is about adversarial search agent algorithm searching minimax. In this problem, I used a lot of hint that provided in the file(eg.current GameState is using self.depth and self.evaluation), method called from getLegalActions of agentIndex which is Pacman=0 starting state and increasing agent index. In this problem, the max_value focus on getting value and Pacman action whereas the min_value focus on getting only value.

The third question is very similar to the question 2 which is difference is pruning. Implementation includes alpha, beta which provides in assignment slide. Alpha beta pruning supports more efficient in searching minimax tree(dive into more steps till bottom). Surprisingly, the speed of movement are faster than question 2's movement, initializing alpha, beta to negative infinity and positive infinity.

The fourth question is also similar to the question 2 however this question ask to implement the probabilistic behavior such as estimating or expectation of possible outcome of values. To make that setting up with empty list utility of expectation and adds these into the existing value and calculate the probabilities. 

The fifth question is to contribute better evaluation function that from question 1 which is reflex agent. The evaluation function and states acts like reflex agent. While implementing this, re-using code from reflex agent problem, the program crash and unstoppable. We tried to use disposal for evaluation for some reasons, it didn't succeed. Need to figure out in the future.

I discuss the idea and implementation of this assignment with Naylin Min. 
The Total time I spent for this project is more than 18-20 hours. The materials are quite a bit challenging however I enjoyed searching new things.  