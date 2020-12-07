import sys

def create_map(path):
    map = []
    with open(path) as file:
        content = [ line.rstrip('\n') for line in file ]
        for line in content:
            row = [x for x in line]
            map.append(row)
    return map

def find_tree_count(map, delta_right, delta_down):
    tree_count = 0
    row = 0
    col = 0
    height = len(map)
    width = len(map[0]) # width is the length of each element so just check the first
    while row < height - 1:
        row += delta_down
        col = (col + delta_right) % width
        print(row, col)
        if map[row][col] == '#':
            tree_count += 1
    return tree_count

file_path = sys.argv[1]
map = create_map(file_path)
tree_count = find_tree_count(map, int(sys.argv[2]), int(sys.argv[3]))
print(tree_count)
