print('Name: S. Vyshnavi \nUSN: 1AY24AI098 \nSection: O\n ')

import random, copy

WIDTH = 5
HEIGHT = 5

nextCells = [[random.choice([' ', '#']) for _ in range(WIDTH)] for _ in range(HEIGHT)]

for _ in range(5):
    print('\n' * 5)
    currentCells = copy.deepcopy(nextCells)

    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[y][x], end='')
        print()

    for y in range(HEIGHT):
        for x in range(WIDTH):
            left = (x - 1) % WIDTH
            right = (x + 1) % WIDTH
            above = (y - 1) % HEIGHT
            below = (y + 1) % HEIGHT

            numNeighbors = 0
            for dx in [left, x, right]:
                for dy in [above, y, below]:
                    if (dx, dy) != (x, y) and currentCells[dy][dx] == '#':
                        numNeighbors += 1
            if currentCells[y][x] == '#' and (numNeighbors == 2 or numNeighbors == 3):
                nextCells[y][x] = '#'
            elif currentCells[y][x] == ' ' and numNeighbors == 3:
                nextCells[y][x] = '#'
            else:
                nextCells[y][x] = ' '