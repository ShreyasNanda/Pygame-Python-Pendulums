import pygame
import math

pygame.init()
CLOCK = pygame.time.Clock()
FPS = 60

WIDTH = 800
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Pendulum :
    def __init__(self, angle, length) :
        G = 6.6743 * 10 ** -11 # N*M^2/kg^2
        r_earth = 6.371 * 10 ** 6 # in m
        mass_e = 5.9722 * 10 ** 24 # in kg
        self.g = G * (mass_e / (r_earth ** 2))

        self.theta = math.radians(angle) 
        self.length = length
        self.omega = 0.0

        self.center_x = WIDTH / 2
        self.center_y = HEIGHT / 2


    def physics_update(self, dt) :
        # alpha = -(g / L) * sin(theta)

        angular_acceleration = -1 * ((self.g) / (self.length)) * math.sin(self.theta)

        self.omega += angular_acceleration * dt
        self.theta += self.omega * dt
        



    def draw(self, screen) :
        starting_pos = (self.center_x, self.center_y)

        end_x_pos = self.center_x + (self.length * math.sin(self.theta))
        end_y_pos = self.center_y + (self.length * math.cos(self.theta))
        end_pos = (end_x_pos, end_y_pos)

        pygame.draw.line(screen, WHITE, starting_pos, end_pos, 3)
        pygame.draw.circle(screen, RED, end_pos, 15)






def main() :
    running = True

    test_pend_001 = Pendulum(45, 200)

    pendulums = [test_pend_001]


    while running :
        dt = CLOCK.tick(FPS) / 90.0
        # CLOCK.tick(FPS)
        screen.fill(BLACK)

        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                running = False

        for pendulum in pendulums :
            pendulum.physics_update(dt)
            pendulum.draw(screen)

        pygame.display.update()

    pygame.quit()


main()