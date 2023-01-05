from os import system
from drawing import draw, split_coords
import time


coords = []
walls = []
size = 5
start = []
end = []

def test_int(var):
    try:
        int(var)
    except:
        return False
    return True

def get_coord():
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
                    return (coords, walls, start, end, size)


        elif choice.lower() == "help":
            print("$ add wall:       Adds a wall in the given coordinates\n$ remove wall:    Removes a wall in the given coordinates\n$ set start:      Sets the starting coordinates\n$ set end:        Sets the starting coordinates\n$ reset:          You will be prompted with a confirmation.\n                  Resets your walls and the start and end points.\n$ done:           You will be prompted with a confirmation.\n                  Annouce that you're done with your maze and want to solve it\n\n")
        
        else:
            print("\nThere is not such command...")
            time.sleep(1.3)