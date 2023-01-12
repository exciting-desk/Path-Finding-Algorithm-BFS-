from os import system
from drawing import draw, split_coords
import time
import algo


coords = []
walls = []
size = 5
start = []
end = []

def test_int(var):
    """
    Test if a variable can be converted to an int

    Args: 
        var: variable to test

    Returns: 
        (Bool): True if var can be converted to an int, False otherwise
    """

    try:
        int(var)
    except:
        return False
    return True


def get_coord():
    """
    Prompt the user for coordinates and validate that they are valid (exist in coords)

    Returns: 
        List[int]: the valid coordinates entered by the user
    """

    print("\nEnter the coordinates :\n")
    x = input("\nX : ")
    test_int(x)
    y = input("Y : ")
    test_int(y)
    coord = [int(y),int(x)]
    if coord not in coords:
        print("\nThe given coordinate [",y,",",x,"] is not in the available coordinates\n")
        time.sleep(1.3)
    else:
        return coord


def set_size():
    """
    Prompt the user for the size of the maze and initialize the coords and walls lists

    """

    while True:
        choice = input("\nEnter the size of your maze\nThe size of the maze should be strictly superior to 0.\n")
        try:
            choice = int(choice)
            if choice<=0:
                raise 'SizeError'
        except:
            print("The size of the maze should be strictly superior to 0.")
        else:
            for i in range(int(choice)):
                for j in range(int(choice)):
                    coords.append([i,j])
            size = int(choice)
            split_coords(coords, size)
            break

def create_maze():
    """
    Main function to create the maze, allowing the user to add/remove walls, set start/end points,
    find the shortest path, and reset the maze

    """
    
    global coords
    global walls
    global size
    global start
    global end

    set_size()

    while True:
        draw(walls, size, start, end)
        choice = input("\nType help if needed.\n$ ")

        system('cls')

        if choice.lower() == "add wall":
            given_coord = get_coord()
            if given_coord:
                walls.append(given_coord)

        elif choice.lower() == "remove wall":
            given_coord = get_coord()
            if given_coord:
                if given_coord in walls:
                    walls.remove(given_coord)
                else:
                    print("\nThis Wall doesn't exist...")
                    time.sleep(1.3)
            
        elif choice.lower() == "set start":
            given_coord = get_coord()
            if given_coord:
                if given_coord in walls:
                    print("There is a wall in there.\nTry removing the wall first...")
                    time.sleep(1.3)
                else:
                    start = given_coord.copy()

        elif choice.lower() == "set end":
            given_coord = get_coord()
            if given_coord:
                if given_coord in walls:
                        print("There is a wall in there.\nTry removing the wall first...")
                        time.sleep(1.3)
                else:
                    end = given_coord.copy()
            
        elif choice.lower() == "reset":
            choice = input("\nAre you sure you wanna reset ?\n")
            if choice.lower() == "yes" or choice.lower() == "y":
                coords = []
                walls = []
                start = []
                end = []
                set_size()


        elif choice.lower() == "done":
            if start == []:
                print("\nYou need to set a starting point...")
                time.sleep(1.3)
            elif end == []:
                print("\nYou need to set an arrival point...")
                time.sleep(1.3)
            else:
                draw(walls, size, start, end)
                choice = input("\nAre you sure you ?\n")
                if choice.lower() == "yes" or choice.lower() == "y":
                    path = algo.find_path(coords, walls, start, end, size)
                    draw(walls, size, start, end, path)
                    break


        elif choice.lower() == "help":
            print("$ add wall:       Adds a wall in the given coordinates\n$ remove wall:    Removes a wall in the given coordinates\n$ set start:      Sets the starting coordinates\n$ set end:        Sets the starting coordinates\n$ reset:          You will be prompted with a confirmation.\n                  Resets your walls and the start and end points.\n$ done:           You will be prompted with a confirmation.\n                  Annouce that you're done with your maze and want to solve it\n\n")
        
        else:
            print("\nThere is not such command...")
            time.sleep(1.3)