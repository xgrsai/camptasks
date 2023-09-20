import numpy as np
import time
import pygame
import copy
import sys


def draw_grid(matrix, screen):
    rows, cols = matrix.shape
    cell_size = 20
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == 1:
                pygame.draw.rect(screen, (255, 255, 255), (col * cell_size, row * cell_size, cell_size, cell_size))
            else:
                pygame.draw.rect(screen, (0, 0, 0), (col * cell_size, row * cell_size, cell_size, cell_size))


def task_2():  # 7 iterations without random
    cols_size = 7
    rows_size = 7
    matrix = np.array([[1, 0, 0, 0, 0, 0, 0],
                       [0, 0, 1, 0, 0, 1, 1],
                       [1, 0, 0, 1, 0, 0, 1],
                       [0, 1, 1, 0, 1, 1, 0],
                       [1, 1, 1, 1, 0, 0, 1],
                       [1, 1, 1, 1, 1, 1, 1],
                       [1, 1, 0, 1, 1, 0, 1]])

    pygame.init()
    # print the initial matrix
    screen = pygame.display.set_mode((cols_size * 20, rows_size * 20))
    pygame.display.set_caption("Game \"Game\"")
    screen.fill((255, 255, 255))
    draw_grid(matrix, screen)
    pygame.display.flip()
    time.sleep(2)
    iterations = 0
    while True:
        if iterations == 7:
            break
        else:
            iterations += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        new_matrix = copy.deepcopy(matrix)

        for i in range(rows_size):
            for j in range(cols_size):
                neighbors = []
                cell = matrix[i][j]
                for x_offset in [-1, 0, 1]:
                    for y_offset in [-1, 0, 1]:
                        if x_offset == 0 and y_offset == 0:
                            continue
                        x_wrap = (i + x_offset) % rows_size
                        y_wrap = (j + y_offset) % cols_size
                        neighbors.append(matrix[x_wrap, y_wrap])

                live_neighbors = sum(neighbors)

                if cell == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        new_matrix[i][j] = 0
                else:
                    if live_neighbors == 3:
                        new_matrix[i][j] = 1

        screen.fill((255, 255, 255))
        draw_grid(new_matrix, screen)
        pygame.display.flip()

        matrix = new_matrix.copy()
        time.sleep(1)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


def task_2_random():  # random and infinite iterations
    try:
        cols_size = abs(int(input("Width: ")))
        rows_size = abs(int(input("Height: ")))
        matrix = np.random.randint(2, size=(rows_size, cols_size))

        pygame.init()

        # print the initial matrix
        screen = pygame.display.set_mode((cols_size * 20, rows_size * 20))
        pygame.display.set_caption("Game \"Game\"")
        screen.fill((255, 255, 255))
        draw_grid(matrix, screen)
        pygame.display.flip()
        time.sleep(2)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            new_matrix = copy.deepcopy(matrix)

            for i in range(rows_size):
                for j in range(cols_size):
                    neighbors = []
                    cell = matrix[i][j]
                    for x_offset in [-1, 0, 1]:
                        for y_offset in [-1, 0, 1]:
                            if x_offset == 0 and y_offset == 0:
                                continue
                            x_wrap = (i + x_offset) % rows_size
                            y_wrap = (j + y_offset) % cols_size
                            neighbors.append(matrix[x_wrap, y_wrap])

                    live_neighbors = sum(neighbors)

                    if cell == 1:
                        if live_neighbors < 2 or live_neighbors > 3:
                            new_matrix[i][j] = 0
                    else:
                        if live_neighbors == 3:
                            new_matrix[i][j] = 1

            screen.fill((255, 255, 255))
            draw_grid(new_matrix, screen)
            pygame.display.flip()

            matrix = new_matrix.copy()
            time.sleep(1)

        pygame.quit()
    except ValueError:
        print("Error. Please write the numbers")


if __name__ == "__main__":
    task_2()
