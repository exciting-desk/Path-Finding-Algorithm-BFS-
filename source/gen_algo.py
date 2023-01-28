import drawing
from random import shuffle
from time import sleep
from os import system
import algo
sets = []
coords = []
walls = []
cells = []
size = 0

def set_coords(n_size):
    """
    This function sets the coordinates of the cells in the grid.

    Args :
        n_size (int) : the size of the grid, it creates a grid of n_size*n_size

    """
    global size
    global coords
    size = n_size
    for i in range(0,size):
        for j in range(0,size):
            coords.append([i,j])
    drawing.split_coords(coords, size)


def intialize():
    """
    This function initializes the walls and sets of the grid.

    """
    global coords
    global walls

    s_coords = drawing.s_coords.copy()
    for i in s_coords:
        for j in i :
            if s_coords.index(i)%2 == 0:
                walls.append(j)
            else:
                if i.index(j)%2 == 0:
                    walls.append(j)
    
    for i in coords:
        if i not in walls:
            sets.append([i])
            cells.append(i)


def find_set_ind(cell):
    """
    This function finds the index of the set in which a given cell is present.

    Args:
        cell (list) : the cell for which the index of the set is to be found.

    Returns:
        (int) : the index of the set in which the cell is present

    """
    global sets

    for i in sets:
        if cell in i :
            return sets.index(i)


def find_n(cell):
    """
    This function finds the next cell which can be joined to the current cell.

    Args:
        cell (list) : the current cell

    Returns: 
        (list) : the next cell which can be joined to the current cell.

    """
    global cells

    tmp_reach = cell.copy()
    reach_cells = []

    tmp_reach[0]+=2
    if tmp_reach in cells:
        reach_cells.append(tmp_reach)
    tmp_reach = cell.copy()

    tmp_reach[0]-=2
    if tmp_reach in cells:
        reach_cells.append(tmp_reach)
    tmp_reach = cell.copy()

    tmp_reach[1]+=2
    if tmp_reach in cells:
        reach_cells.append(tmp_reach)
    tmp_reach = cell.copy()

    tmp_reach[1]-=2
    if tmp_reach in cells:
        reach_cells.append(tmp_reach)
    tmp_reach = cell.copy()

    if reach_cells:
        shuffle(reach_cells)
        return reach_cells[0]
    return reach_cells


def join(cell1, cell2):
    """
    This function joins two sets containing cell1 and cell2 respectively.

    Args:
        cell1 (list) : the first cell to be joined
        cell2 (list) : the second cell to be joined

    """
    global sets
    global walls
    set1 = sets[find_set_ind(cell1)]
    set2 = sets[find_set_ind(cell2)]

    set1+=set2
    sets.remove(set2)

    if cell1[1] == cell2[1]:
        if cell1[0]<cell2[0]:
            rem_wall = cell1.copy()
            rem_wall[0]+=1
            walls.remove(rem_wall)
        else:
            rem_wall = cell2.copy()
            rem_wall[0]+=1
            walls.remove(rem_wall)

    elif cell1[0] == cell2[0]:
        if cell1[1]<cell2[1]:
            rem_wall = cell1.copy()
            rem_wall[1]+=1
            walls.remove(rem_wall)
        else:
            rem_wall = cell2.copy()
            rem_wall[1]+=1
            walls.remove(rem_wall)


def main_algo():
    """
    Main algorithm for generating the maze. It is responsible for shuffling the cells, 
    checking for neighboring cells, and joining the sets containing those cells.

    Args:
        visualize (bool) : a boolean value indicating whether the maze should be visualized as it is generated
        user_size (int) : an integer value representing the size of the maze to be generated

    """
    shuffle(cells)
    while len(sets)>1:
        for i in cells:
            n_cell = find_n(i)
            if n_cell and (find_set_ind(n_cell) != find_set_ind(i)):
                join(i, n_cell)
            

    
def draw_maze(user_size):
    """
    Function that creates the maze by calling other functions in the correct order. 
    It sets the coordinates, initializes the sets, calls the main algorithm and draws the maze.

    Args:
        user_size (int) : an integer value representing the size of the maze to be generated
        visualize (bool) : a boolean value indicating whether the maze should be drawn as it is generated

    """
    set_coords(user_size)
    intialize()
    main_algo()
    drawing.draw(walls, size)

def solve_maze():
    global coords
    global walls
    global size

    while True:
        system('cls')
        drawing.draw(walls, size, [], [])
        try :
            start_y = input("Start coordinates\nX : ")
            start_x = input("Y : ")
            
            start_x = int(start_x)
            start_y = int(start_y)

            start = [start_x, start_y]
            assert start in coords
            assert start not in walls

            end_y = input("\nEnd coordinates\nX : ")
            end_x = input("Y : ")

            end_x = int(end_x)
            end_y = int(end_y)
            
            end = [end_x, end_y]
            assert end in coords
            assert end not in walls
        
        except:
            print("Enter correct coordinates !\n")

        else:
            break

    path = algo.find_path(coords, walls, start, end, size)
    drawing.draw(walls, size, start, end, path)


