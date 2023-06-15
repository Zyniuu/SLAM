from includes.env import Environment
from includes.sensor import Sensor
import pygame


env = Environment((1200, 600))
env.original = env.screen.copy()
sensor = Sensor(200, env.original, measurement_error=(0.5, 0.01))
env.screen.fill(env.black)
env.infomap = env.screen.copy()
run = True

while run:
    isOn = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if pygame.mouse.get_focused():
            isOn = True
        elif not pygame.mouse.get_focused():
            isOn = False

    if isOn:
        sensor.pos = pygame.mouse.get_pos()
        sensed_data = sensor.senseObstacle()
        env.storeData(sensed_data)
        env.showData()
    env.screen.blit(env.infomap, (0, 0))
    pygame.display.update()
