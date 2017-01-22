#!/usr/bin/python3

def add(userList,index1,index2):
    tmp = []
    tmp.append(userList[index1][index2])
    tmp.append(index1)
    tmp.append(index2)
    return (tmp)

def foundNeighbors(userList,firstIndex,secondIndex): # Found neighbors of Zero and stores each of them in a list like : [value,indexI,indeJ].
    neighbor = []
    tmp1 = secondIndex + 1
    if tmp1 == 2:
        neighbor.append(add(userList,firstIndex,0))
        neighbor.append(add(userList,firstIndex,2))
    else:
        neighbor.append(add(userList,firstIndex,1))
        
    tmp2 = firstIndex + 1
    if tmp2 == 2:
        neighbor.append(add(userList,0,secondIndex))
        neighbor.append(add(userList,2,secondIndex))
    else:
        neighbor.append(add(userList,1,secondIndex))

    return (neighbor)
