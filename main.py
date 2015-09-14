#!/usr/bin/python3
# main.py authored by Matt Baumann for COMP 412 Loyola University
#The following video was very helpful for this assignment: https://www.youtube.com/watch?v=mlt7MrwU4hY
import csv

#Creation of list objects.
contractorList = []
lobbyistList = []   


#Reading in the contractorList with contracts for the city
cr = open('contractors.csv')
csvCR = csv.reader(cr)    #contractorList name is element 1 or the second element

for i in csvCR:
    contractorList.append(i[1])

cr.close()


#Reading in the lobbbyist's clients
lr = open('lobbyist.csv')
csvLR = csv.reader(lr)    #lobbyist's client's names are element 0   

for i in csvLR:
    lobbyistList.append(i[0])

lr.close()


#Comparison of the two sets
#print(len(contractorList))    #print command to check how many contractors were appended to the list.
#print(len(lobbyistList))    #print command to check how many lobbyists were appended to the list.

contractorSet = set(contractorList)
lobbyistSet = set(lobbyistList)

print('The following names are contractors that have contracts with the city and are clients of registered lobbyists.')
for i in contractorSet.intersection(lobbyistSet):
    print(i)
