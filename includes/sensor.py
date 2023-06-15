import math
import pygame
import numpy as np


class Sensor:
    def __init__(self, sensor_range, floor_map, measurement_error):
        self.sensor_range = sensor_range
        self.floor_map = floor_map
        self.speed = 4
        self.sigma = np.array(measurement_error)
        self.pos = (0, 0)
        self.width, self.height = pygame.display.get_surface().get_size()
        self.obstacles = []

    def distance(self, obstacle_pos):
        px = (obstacle_pos[0] - self.pos[0]) ** 2
        py = (obstacle_pos[1] - self.pos[1]) ** 2
        return math.sqrt(px + py)

    def calcUncertainty(self, distance, angle):
        mean = np.array([distance, angle])
        covariance = np.diag(self.sigma ** 2)
        distance, angle = np.random.multivariate_normal(mean, covariance)
        distance = max(distance, 0)
        angle = max(angle, 0)
        return [distance, angle]

    def senseObstacle(self):
        data = []
        x1, y1 = self.pos[0], self.pos[1]
        for angle in np.linspace(0, 2 * math.pi, 60, False):
            x2, y2 = (x1 + self.sensor_range * math.cos(angle), y1 - self.sensor_range * math.sin(angle))
            for i in range(0, 100):
                u = i / 100
                x = int(x2 * u + x1 * (1 - u))
                y = int(y2 * u + y1 * (1 - u))
                if (0 < x < self.width) and (0 < y < self.height):
                    color = self.floor_map.get_at((x, y))
                    if color == (0, 0, 0):
                        distance = self.distance((x, y))
                        output = self.calcUncertainty(distance, angle)
                        output.append(self.pos)
                        data.append(output)
                        break
        if len(data) > 0:
            return data
        return False
