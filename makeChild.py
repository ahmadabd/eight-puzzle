#!/usr/bin/python3

def child(userList,neighbors):  # make new list by changing Zero by its neighbors.
    childs = []
    for i in range(len(neighbors)):
        tmp = []
        for j in range(len(userList)):
            l = []
            for k in range(len(userList[j])):
                if userList[j][k] != '0':
                    l.append(userList[j][k])
                else:
                    l.append(neighbors[i][0])
            tmp.append(l)
        childs.append(tmp)
    for i in range(len(childs)):
        childs[i][neighbors[i][1]][neighbors[i][2]] = '0'

    return (childs)

    
