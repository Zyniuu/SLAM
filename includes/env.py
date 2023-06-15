import math
import pygame


class Environment:
    def __init__(self, dimensions):
        pygame.init()
        self.points = []
        self.floor_plan = pygame.image.load("D:/Program Files/Python/SLAM/imgs/floor_schema.png")
        self.width, self.height = dimensions
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screen.blit(self.floor_plan, (0, 0))
        self.infomap = None
        self.black = (0, 0, 0)
        self.grey = (70, 70, 70)
        self.blue = (0, 0, 255)
        self.green = (0, 255, 0)
        self.red = (255, 0, 0)
        self.white = (255, 255, 255)

    def addPos(self, distance, angle, robot_pos):
        x = distance * math.cos(angle) + robot_pos[0]
        y = -distance * math.sin(angle) + robot_pos[1]
        return int(x), int(y)

    def storeData(self, data):
        print(len(self.points))
        if data:
            for element in data:
                point = self.addPos(element[0], element[1], element[2])
                if point not in self.points:
                    self.points.append(point)

    def showData(self):
        print(len(self.points))
        self.infomap = self.screen.copy()
        for point in self.points:
            self.infomap.set_at((int(point[0]), int(point[1])), self.red)
