#!/usr/bin/python3
# main.py authored by Matt Baumann for COMP 412 Loyola University

import csv

#Reading in the contractorList with contracts for the city
cr = open('contractors.csv')
csvCR = csv.reader(cr)    #contractorList name is element 1 or the second element

contractorList = []

for i in csvCR:
    contractorList.append(i[1])

cr.close()

#Reading in the lobbbyist's clients
lr = open('lobbyist.csv')
csvLR = csv.reader(lr)    #lobbyist's client's names are element 0
    
lobbyistList = []    

for i in csvLR:
    lobbyistList.append(i[0])

lr.close()

#Comparison of the two sets
print(len(contractorList))
print(len(lobbyistList))

contractorSet = set(contractorList)
lobbyistSet = set(lobbyistList)

print(contractorSet.intersection(lobbyistSet))