import pygame
from math import *
window = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

projectionMatrix = [[1,0,0], 
                    [0,1,0], 
                    [0,0,0]]

cubePoints = [n for n in range(8)]
cubePoints[0] = [[-1], [-1], [1]]
cubePoints[1] = [[1], [-1], [1]]
cubePoints[2] = [[1], [1], [1]]
cubePoints[3] = [[-1], [1], [1]]
cubePoints[4] = [[-1], [-1], [-1]]
cubePoints[5] = [[1], [-1], [-1]]
cubePoints[6] = [[1], [1], [-1]]
cubePoints[7] = [[-1], [1], [-1]]




def MultiplyM(a, b):
    aRows = len(a)
    aCols = len(a[0])

    bRows = len(b)
    bCols = len(b[0])

    product = [[0 for _ in range(bCols)] for _ in range(aCols)]

    if aCols == bRows:
        for i in range(aRows):
            for j in range(bCols):
                for k in range(bRows):
                    product[i][j] += a[i][k] * b[k][j]
    else:
        print("incompatible matrix")

    return product

def ConnectPoints(i, j, points):
    pygame.draw.line(window, (255, 255, 255), (points[i][0], points[i][1]), (points[j][0], points[j][1]) )

scale = 100
angleX = angleY = angleZ = 0
while True:
    clock.tick(60)

    window.fill((0,0,0))

    rotationX = [[1, 0, 0],
                    [0, cos(angleX), -sin(angleX)],
                    [0, sin(angleX), cos(angleX)]]

    rotationY = [[cos(angleY), 0, sin(angleY)],
                    [0, 1, 0],
                    [-sin(angleY), 0, cos(angleY)]]

    rotationZ = [[cos(angleZ), -sin(angleZ), 0],
                    [sin(angleZ), cos(angleZ), 0],
                    [0, 0, 1]]

    angleX += 0.01
    angleY += 0.01


    points = [0 for _ in range(len(cubePoints))]
    i = 0
    for point in cubePoints:

        rotateX = MultiplyM(rotationX, point)
        rotateY = MultiplyM(rotationY, rotateX)
        rotateZ = MultiplyM(rotationZ, rotateY)



        point2D = MultiplyM(projectionMatrix, rotateZ)

        x = (point2D[0][0] * scale + 400)
        y = (point2D[1][0] * scale + 400)

        points[i] = (x,y)
        i += 1
        pygame.draw.circle(window, (255, 0, 0), (x, y), 5)

    ConnectPoints(0, 1, points)
    ConnectPoints(0, 3, points)
    ConnectPoints(0, 4, points)
    ConnectPoints(1, 2, points)
    ConnectPoints(1, 5, points)
    ConnectPoints(2, 6, points)
    ConnectPoints(2, 3, points)
    ConnectPoints(3, 7, points)
    ConnectPoints(4, 5, points)
    ConnectPoints(4, 7, points)
    ConnectPoints(6, 5, points)
    ConnectPoints(6, 7, points)

    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()