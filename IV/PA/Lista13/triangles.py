import pygame

pygame.init()

screen = pygame.display.set_mode((580, 480))
clock = pygame.time.Clock()
running = True

point1 = [100, 100]
point2 = [150, 100]
point3 = [125, 150]
triangle_vertices = [point1, point2, point3]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                for point in triangle_vertices:
                    point[1] -= 5
            if event.key == pygame.K_s:
                for point in triangle_vertices:
                    point[1] += 5

    screen.fill((41, 41, 41))
    pygame.draw.polygon(screen, (255, 255, 255), triangle_vertices)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
