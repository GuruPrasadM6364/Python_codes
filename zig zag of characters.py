print('Name: Guru Prasad M \nUSN: 1AY24AI037 \nSection: M\n ')

def print_zigzag(rows, cols):
    """Prints a zigzag pattern with the given number of rows and columns."""
    for i in range(rows):
        for j in range(cols):
            if (i + j) % 2 == 0:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

print_zigzag(5, 10)
