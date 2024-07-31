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
# ----------

# Perceptron implementation
from operator import le
import Helpers.util
import random


class PerceptronClassifier:

    def __init__( self, legalLabels, max_iterations):
        self.legalLabels = legalLabels
        self.type = "perceptron"
        self.epochs = max_iterations
        self.weights = None 


    def classify(self, data):
        sum = float('-inf')
        big = 0
        #predictionsList = []
        for i in range(len(self.legalLabels)):
            temp = 0
            for j in range(len(data)-1):
                temp += data[j] * self.weights[i][j] #calculates f
            temp += self.weights[i][-1] * 1 #adds bias
            if temp > sum:
                sum = temp
                big = i
        return big
 
    def train(self, train_data, labels):
        self.weights = []
        for i in range(len(self.legalLabels)): #assigns random weights
            temp = []
            for j in range(len(train_data[0])):   
                temp.append(random.uniform(-1,1))
            self.weights.append(temp)
            
        for epoch in range(self.epochs):
            accuracy = 0 #seeing how many are correct
            for x in range(len(train_data)):
                result = self.classify(train_data[x]) #calculates result
                actual = labels[x]
                if result == actual: #checks to see if accurate
                    accuracy += 1
                elif result != actual: 
                    for j in range(len(train_data[x])):
                        self.weights[result][j] -= train_data[x][j]
                        self.weights[actual][j] += train_data[x][j]                     
            percentage = (accuracy/len(train_data))*100 
            print("epoch",epoch,"...", percentage ,"correct.")