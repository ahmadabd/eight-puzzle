#!/usr/bin/python3

import makeChild

final = [['1','2','3'],['8','0','4'],['7','6','5']]

def make(userList,neighbors):  # Gets input list and check diffrence of it by final list ,then stores differences on h.
    childs = makeChild.child(userList, neighbors)
    for i in range(len(childs)):
        h = 0
        for j in range(len(childs[i])):
            for k in range(len(childs[i][j])):
                if childs[i][j][k] != final[j][k]:
                    h += 1
        childs[i].append(h)
    return (childs)

