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

# Perceptron implementation for imitation learning
import Helpers.util
from Exercises.perceptron_multiclass import PerceptronClassifier
import random
from pacman import GameState

class PerceptronClassifierPacman(PerceptronClassifier):
    def __init__(self, legalLabels, maxIterations):
        PerceptronClassifier.__init__(self, legalLabels, maxIterations)
        self.epochs = maxIterations
        self.weights = [] 

    def convert_data(self, data):
        # fixes datatype issues
        # if it comes in inside of a list, pull it out of the list
        if isinstance(data, list):
            data = data[0]

        #data comes as a tuple
        all_moves_features = data[0] #grab the features (dict of action->features)
        legal_moves = data[1]        #grab the list of legal moves from this state
        return_features = {}
        #loop each action
        for key in all_moves_features:
            #convert feature values from dict to list
            list_features = list(all_moves_features[key].values()) 
            return_features[key] = list_features

        return (return_features, legal_moves) 

    def classify(self, data):
        #leave this call to convert_data here!
        features, legal_moves = self.convert_data(data) #features are maps; legal moves - list of things

        ##your code goes here##
        scoreslist = []
        for move in legal_moves:
            sum = 0
            for x in range(len(features[move])):
                sum += features[move][x] * self.weights[x]
            scoreslist.append(sum)                 

        #your predicted_label needs to be returned inside of a list for the PacMan game
        maxScore = scoreslist[0]
        maxLabel = legal_moves[0]
        for i in range(len(scoreslist)):
            if scoreslist[i] > maxScore:
                maxScore = scoreslist[i]
                maxLabel = legal_moves[i]
        
        return [maxLabel]

    def train(self, train_data, labels):
        for i in range(14): #assigns random weights
            self.weights.append(random.uniform(-1,1))
        
        for epoch in range(self.epochs):
            for x in range(len(train_data)):
                result = self.classify(train_data[x])[0] #calculates result
                actual = labels[x]
                features, legal_moves = self.convert_data(train_data[x])
                
                if result != actual:
                    resultFeatures = features[result]
                    actualFeatures = features[actual]
                    length = 0
                    if len(resultFeatures) < len(actualFeatures):
                        length = len(resultFeatures)
                    else:
                        length = len(actualFeatures)
                    for j in range(length):
                        self.weights[j] -= resultFeatures[j]
                        self.weights[j] += actualFeatures[j]