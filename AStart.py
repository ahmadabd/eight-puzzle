#!/usr/bin/python3

### Solve Table of number by AStar algorithm.
### auther : Ahmad Abdollahzade (ahmadabd13741112@gmail.com)
## while you enter input values :
# 1) Your values should be same as final values.
# 2) For empty value enter Zero.

import foundNeighbors as neighbor
import makeHn as Hn
#import sys
#sys.setrecursionlimit(100000)

final = [['1','2','3'],['8','0','4'],['7','6','5']]
passedTables = []

def getValue():  # Get input values and stores them into userList list.
    userList = []
    print("One important point:\n1. Your input values should be same as final list.\n")
    print("Final:")
    for i in range(len(final)):
        print(final[i])
    print("------------------------------------------------------")
    for i in range(3):
        tmp = []
        for j in range(3):
            tmp.append(input("[{0}][{1}]:".format(i,j)))
        userList.append(tmp)
    if final == userList:
        print("your input value is the answer.")
        exit()
    print("------------------------------------------------------")
    print("Input:")
    for i in range(len(userList)):
        print(userList[i])
    print("0================Enter for next level=================")
    input()
    neighbors = foundNeighborsOfZero(userList)
    checkChilds(passedTables,0,userList,neighbors)
    
def checkChilds(passedTables,g,userList,neighbors):
    g += 1
    f = []
    childs = Hn.make(userList, neighbors)

    for i in range(len(childs)):
        childs[i][3] = g + childs[i][3]
        f.append(childs[i][3])
    minChildIndex = f.index(min(f))
    del f[:]

    for i in range(len(childs)):
        for j in range(len(childs[i])):
            print(childs[i][j])
        print("\n")
    print("======================The best========================")

    for i in range(len(childs)):
        if childs[i][0:3] == final:
            print("we found answer :)")
            print("final: ")
            for j in range(len(final)):
                print(final[j])
            exit()

    if len(passedTables) > 0:
        for i in range(len(passedTables)):
            f.append(passedTables[i][3])
    if len(f) > 0:
        minChildIndexPassed = f.index(min(f))
        if passedTables[minChildIndexPassed][3] <= childs[minChildIndex][3]:
            newTable = passedTables[minChildIndexPassed]

            for i in range(3):
                print(newTable[0:3][i])
            print("{}================Enter for next level=================".format(g))
            input()
            neighbors = foundNeighborsOfZero(newTable[0:3])
            del passedTables[minChildIndexPassed]
            checkChilds(passedTables,g,newTable[0:3],neighbors)
        else:
            foundBestChild(childs,minChildIndex,passedTables,g)
    else:
        foundBestChild(childs,minChildIndex,passedTables,g)

def foundBestChild(childs,minChildIndex,passedTables,g):
    newTable = childs[minChildIndex]

    for i in range(3):
        print(newTable[0:3][i])
    print("{}================Enter for next level=================".format(g))
    input()
    neighbors = foundNeighborsOfZero(newTable[0:3])
    del childs[minChildIndex]
    for i in range(len(childs)):
        passedTables.append(childs[i])
    checkChilds(passedTables, g, newTable[0:3], neighbors)

def foundNeighborsOfZero(userList): # found index of empty value.
    for i in range(len(userList)):
        for j in range(len(userList[i])):   
            if userList[i][j] == '0':
                firstIndex,secondIndex = i,j
                break
    return (neighbor.foundNeighbors(userList,firstIndex,secondIndex))
    
getValue()


            
