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
        if map[row][col] == '#':
            tree_count += 1
    return tree_count

#This is so dumb lol
if len(sys.argv) <= 2 or sys.argv[2] == "-h":
    print("Usage:\n <file> [<right_change> <down_change>] OR [Input Set File: -l <inputs_file_path>]\n -h Help, This message ")
    exit()
file_path = sys.argv[1]
map = create_map(file_path)
if sys.argv[2] != "-l":
    tree_count = find_tree_count(map, int(sys.argv[2]), int(sys.argv[3]))
    print("Tree Count: {0}".format(tree_count))
#this is extra dumb
else:
    slopes = []
    with open(sys.argv[3]) as file:
        content = [ line.rstrip('\n') for line in file]
        for row in content:
            rl = []
            for char in row:
                if char != " ":
                    rl.append(int(char))
            slopes.append(rl)

    product = 1
    for input in slopes:
        tree_count = find_tree_count(map, input[0], input[1])
        print("Tree Count for Input {0} {1}: {2}".format(input[0], input[1], tree_count))
        product = product * tree_count

    print("Product of answers: {0}".format(product))
