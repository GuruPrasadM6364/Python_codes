print(“Guru Prasad M\n 1AY24AI037\n M Section")

print('Name: Guru Prasad M \nUSN: 1AY24AI037 \nSection: M ')

grid = [
    ['.', '.', '.', '.', '.', '.'],
    ['.', 'O', 'O', '.', '.', '.'],
    ['O', 'O', 'O', 'O', '.', '.'],
    ['O', 'O', 'O', 'O', 'O', '.'],
    ['.', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', '.'],
    ['O', 'O', 'O', 'O', '.', '.'],
    ['.', 'O', 'O', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.']
]

for x in range(len(grid[0])):
    for y in range(len(grid)):
        print(grid[y][x], end='')
    print()
