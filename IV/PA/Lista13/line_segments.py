import pygame
import numpy as np

pygame.init()

GREEN = (0, 255, 0)
RED = (255, 0, 0)

screen = pygame.display.set_mode((580, 480))
clock = pygame.time.Clock()
running = True

a_start = [12, 115]
a_end = [50, 315]
line_a = [a_start, a_end]

b_start = [15, 180]
b_end = [530, 365]
line_b = [b_start, b_end]


def check_collision(line_1, line_2):
    [a_x, a_y], [b_x, b_y] = line_1
    [c_x, c_y], [d_x, d_y] = line_2

    t = (((c_x - a_x) * (c_y - d_y) - (c_y - a_y) * (c_x - d_x)) /
         ((b_x - a_x) * (c_y - d_y) - (b_y - a_y) * (c_x - d_x)))

    s = (((b_x - a_x) * (c_y - a_y) - (c_x - a_x) * (b_y - a_y)) /
         ((b_x - a_x) * (c_y - d_y) - (b_y - a_y) * (c_x - d_x)))

    # print(t, s)

    if 0 <= t <= 1 and 0 <= s <= 1:
        return True

    return False


def check_degenerated_collision(line_1, line_2):
    [a_x, a_y], [b_x, b_y] = line_1
    [c_x, c_y], [d_x, d_y] = line_2

    # Both are points
    if (a_x, a_y) == (b_x, b_y) and (c_x, c_y) == (d_x, d_y):
        if (a_x, a_y) == (c_x, c_y):
            return True
        return False

    # First is a point
    elif (a_x, a_y) == (b_x, b_y):
        # line_2 is parallel to Oy
        if d_x == c_x:
            t = ((a_y - c_y) / (d_y - c_y))
            if a_x == c_x and 0 <= t <= 1:
                return True
            return False
        # line_2 is parallel to Ox
        elif d_y == c_y:
            t = ((a_x - c_x) / (d_x - c_x))
            if a_y == c_y and 0 <= t <= 1:
                return True
            return False
        # None of the above
        else:
            t = ((a_x - c_x) / (d_x - c_x))
            if 0 <= t <= 1:
                return True
            return False

    # Second is a point
    elif (c_x, c_y) == (d_x, d_y):
        # line_1 is parallel to Oy
        if b_x == a_x:
            t = ((c_y - a_y) / (b_y - a_y))
            if a_x == c_x and 0 <= t <= 1:
                return True
            return False
        # line_2 is parallel to Ox
        elif b_y == a_y:
            t = ((c_x - a_x) / (b_x - a_x))
            if a_y == c_y and 0 <= t <= 1:
                return True
            return False
        # None of the above
        else:
            t = ((c_x - a_x) / (b_x - a_x))
            if 0 <= t <= 1:
                return True
            return False

    # Lines are parallel
    temp_matrix = np.array([[b_x - a_x, b_y - a_y],
                            [d_x - c_x, d_y - c_y]])
    det = np.linalg.det(temp_matrix)
    if det == 0:
        t = (c_x - a_x) / (b_x - a_x) if b_x - a_x != 0 else \
            (c_y - a_y) / (b_y - a_y)
        k = (d_x - a_x) / (b_x - a_x) if b_x - a_x != 0 else \
            (d_y - a_y) / (b_y - a_y)
        left = min(t, k)
        right = max(t, k)
        if 0 <= left <= 1 or 0 <= right <= 1:
            return True
        return False

    # Not degenerated
    if check_collision(line_1, line_2):
        return True

    return False


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    colour = RED if check_degenerated_collision(line_a, line_b) else GREEN

    screen.fill((41, 41, 41))
    pygame.draw.line(screen, colour, a_start, a_end)
    pygame.draw.line(screen, colour, b_start, b_end)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
