import drawing
paths = []

looking = True

def find_n(node, coords, walls, des_path):
    av_coords = []
    fix_node = node.copy()

    def av(dir):
        if (dir not in coords) or (dir in walls) or (dir in des_path):
            return False
        return True

    node[1] -= 1
    if av(node):
        av_coords.append(node)
    node = fix_node.copy()
    
    node[1] += 1
    if av(node):
        av_coords.append(node)
    node = fix_node.copy()

    node[0] -= 1
    if av(node):
        av_coords.append(node)
    node = fix_node.copy()

    node[0] += 1
    if av(node):
        av_coords.append(node)
    node = fix_node.copy()

    return av_coords

def find_path(coords, walls, start, end, size):
    global paths

    drawing.split_coords(coords, size)
    paths.append([start.copy()])

    while True:
        dummy_path = paths.copy()

        for i in dummy_path:
                av_dir = find_n(i[-1].copy(), coords, walls, i)

                if len(av_dir) == 1:
                    i.append(av_dir[0])
                else:
                    for j in av_dir:
                        new_p = i.copy()
                        new_p.append(j)
                        paths.append(new_p)
                        if i in paths:
                            paths.remove(i)

        for i in paths:
            if end in i:
                return i