
Name : Shan Kwan Cho
SID  : 917599337

Description:

There are sixth questions in this assignment.

For question 1, we have to do the training with the actual and predicted. By taking the arg max score, we have to update the weight if our prediction and already trained(actual) goes off. We have to use perceptron analogy of w(new) = w(old) +/- features vector ( subtraction is for its goes off).


For question 2, this is just have to test with the weight for representative of perceptron by changing in answers.py with return either a or b in the method q2 in this case. 


For question 3, first we iterate through the iterations. For each iterations, we iterate through the training data. For each legal labels in the current image of the training data, we get prediction value by multiplying the currentData with the weight of the label. We then update the bestScore if prediction is > than bestScore. If the label for the bestScore does not equal actual label, we update the weights by multiplying t value to the feature vector. Much like question 1, however, we use the given formula in the instruction for the t value.  


For question 4, we tested the pixels of the image to see if they are in bound and updated the feature vector accordingly. We also tested for neighbors of the pixels. If the pixels have more than 2 neighbors, we updated the feature vector. However, was only able to score 3 out of 6 on this one. Was not able to further improve on it. 


For question 5, this question is very similar to the question 1 , within two different types of classifiers, just need to update the weight after each iteration using w(new) = w(old) +/- feature vectors, correct and guessed action respectively. Of each training, getting highest scores ( arg max scores ) of label, take those and update each. Training accuracy got above 70 prediction.  


For question 6, as stated in the hints, we use the format <feature name> : <feature value> for the feature vector. We first get successor of the state and get a list of food for that successor state. Then, we iterate through the food and convert the coordinates of the food to a string and store that for <feature name> and calculate the inverse of ManhattanDistance and set that as <feature value>.


I discuss the idea and implementation of this assignment with Naylin Min. 
The Total time I spent for this project is more than 4 days. It took time for me to understand how the functions we are to used worked. The materials are quite a bit challenging however I enjoyed searching new things especially the Bayes Nets which is essential/ fundamental theory for machine learning. 

