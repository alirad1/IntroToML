from ast import Return
import random
from tracemalloc import stop

# Make a prediction with weights
def classify(row, weights):
    sum = 0
    for i in range(len(row)-1):
        sum += row[i] * weights[i] #calculates f
    sum += weights[len(row)-1] #adds bias
    if (sum > 0):
        return 1 #Mine
    else:
        return 0 #Rock
 
#Estimate Perceptron weights using stochastic gradient descent
def train(train_data, n_epoch, l_rate=1):
    weights = []
    for i in range(len(train_data[0])): #assigns random weights
        weights.append(random.uniform(-1,1)) 
    
    for epoch in range(n_epoch):
        accuracy = 0 #seeing how many are correct
        for x in range(len(train_data)):
            result = classify(train_data[x], weights) #calculates result
            
            if result == train_data[x][-1]: #checks to see if accurate
                accuracy += 1
            elif result != train_data[x][-1]: 
                for y in range(len(weights)-1): #adjusts weights
                    error = train_data[x][-1] - result
                    weights[y] = weights[y] + 1*(error * train_data[x][y])
                weights[-1] = weights[-1] + (train_data[x][-1] - result)*1
        
        percentage = (accuracy/len(train_data))*100 
        print("epoch",epoch,"...", percentage ,"correct.")
        #if percentage >= 97:
            #exit()