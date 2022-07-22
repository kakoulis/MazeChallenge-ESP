import time
import board
import random
import supervisor
import mottor
import map 

driverRotary = mottor.TB6600('0')
driverFrontBack = mottor.TB6600('1')

def drawMap(maze,position):
    for i in range(0,21):
        print()
        for j in range(0,33):
            if (position[0] == i) and (position[1] == j):
                print("X", end=' ')
            elif maze[i][j] == 0:
                print(" ", end=' ')
            elif maze[i][j] == 1:
                print("#", end=' ')

def move(maze,position,input):
#Add a div here to make it rolling the table
    #right
    if input == "d":
        if position[1] == 32:
                position[1] = 0
                driverRotary.step("clockwise")
        else:
            if available_move(maze,position[0],position[1]+1):
                position[1]+=1
                driverRotary.step("clockwise")
    #left
    elif input == "a":
        if position[1] == 0:
            position[1] = 32
            driverRotary.step("counterclockwise")
        else:
            if available_move(maze,position[0],position[1]-1):
                position[1]-=1
                driverRotary.step("counterclockwise")
    #up
    elif input == "w":
        if available_move(maze,position[0]-1,position[1]):
            position[0]-=1
            driverFrontBack.frontstep("back")

    #down    
    elif input == "s":
        if available_move(maze,position[0]+1,position[1]):
            position[0]+=1
            driverFrontBack.frontstep("front")


def available_move(maze,posX,posY):
    if maze[posX][posY] == 0:
        return True
    else:
        return False



position = [19,7]
maze = map.maze

print("Where do you want to move ?")

while True:

    
    #Dimensions (starting from 1)
    height = 21
    width = 33
    #Starting position starting from 0
    starting_height = 19
    starting_width = 9
    finishing_height = 0
    finishing_width = 15

    if supervisor.runtime.serial_bytes_available:
        value = input().strip()
        print(f"Received: {value}\r") 
        print("Where do you want to move next?")
        move(maze,position,value)
        drawMap(maze,position)
        print(position)
    time.sleep(0.5) 
