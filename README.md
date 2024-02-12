# ft_Linear_Regression

## Work Log:

1. Created a new file train.py.
2. getPath() function returns the file path of the file which is used for the program.
3. fetchData() function returns the tuple of two list variables- mileages and prices.
4. gradient_descent_algorithm() function will have the iterative process to find the slope and intercept of the linear regression model.
5. findLosses() function calculates the losses with sum of squares of observed values - predicted values.
6. earlyStopping() function checks if the mean of the first 8 elements of the lossHistory is equal to the last element of the lossHistory. If condition holds, returns true else returns false.
7. boldDriver() function examines the last element of the loss. If the current loss is greater than the previous loss, it gives a new value of t0 and t1 by multiplying with learningRate and divided by the length of the mileages, also learning rate gets a new value which is half of the value of learning rate. If the loss is not greater, then the learning rate will have the new value of 5% more of its value. The function returns the tuple value of t0, t1, learningRate.
8. storeData() function stores the values of t0, t1 in thetas.csv file.
9. plotting() function plots the values of observed values and predicted values on the same graph.
10. Created a new file accuracy.py.
11. estimatePrice() returns the expected price of the model with the given mileage.
12. getThetas() returns the values of thetas when extracted from the csv file.
13. getAccuracy() returns the accuracy of the model by getting the absolute losses of the model first which is (Sum of Squares of Residuals) / (Total Sum of Squares). Then in order to get the accuracy we deduct the resulted value from 1.


## Objectives:

1. ~~Get the path of file which will be used for the program.~~
2. ~~Fetch data from the file using csv.~~
3. ~~Apply gradient descent algorithm to create a linear regression model on the given data.~~
4. ~~Plot the observed data and predicted data oon the same figure.~~
5. ~~Create a new file accuracy.py which will generate the accuracy of the model with the observed data.~~

## Process:

Fetch Data -> Normalize the elements -> Set the parameters -> Find the value of slope and intercept of the predicted model line -> Store the values of slope and intercept in .csv file.

Plot the data with the observed values and the predicted values on the same graph.

## References:

1. [Gradient Descent Wiki](https://en.wikipedia.org/wiki/Gradient_descent)
2. [Gradient Descent Video](https://www.youtube.com/watch?v=sDv4f4s2SB8)
3. [Gradient Descent GFG](https://www.geeksforgeeks.org/gradient-descent-algorithm-and-its-variants/)