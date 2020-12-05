from functools import reduce
TREE = '#'

def move(current_position, right, down, le_map):
    new_x = current_position[0] + right
    new_y = current_position[1] + down
    new_x = new_x % len(le_map[0])

    return (new_x, new_y)

def get_tree_count(le_map, le_slope):
    right = le_slope[0]
    down = le_slope[1]

    current_position = (0, 0)
    num_trees_encountered = 0
    max_y = len(le_map)

    while current_position[1] < max_y - down:
        current_position = move(current_position, right, down, le_map)
        x = current_position[0]
        y = current_position[1]
        if le_map[y][x] == TREE:
            num_trees_encountered += 1

    return num_trees_encountered

if __name__ == '__main__':
    f = open('input_day3')
    right = 3
    down = 1

    le_map = []

    for line in f:
        le_map.append(list(line.strip()))

    slopes = [
      (1, 1),
      (3, 1),
      (5, 1),
      (7, 1),
      (1, 2)
    ]

    trees_encountered = []
    for slope in slopes:
        num_trees_encountered = get_tree_count(le_map, slope)
        print(f"For slope {slope}, encountered {num_trees_encountered} trees.")
        trees_encountered.append(num_trees_encountered)

    result = reduce((lambda x, y: x * y), trees_encountered)
    print(f"Multiplying them all together, got {result}")

    f.close()
