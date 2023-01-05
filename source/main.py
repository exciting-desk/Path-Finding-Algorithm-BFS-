import algo
import drawing
import maze_creator
import keyboard
import os
import time

def main():
    while True:
        os.system('cls')
        print("     --------------------- Breadth First-Search Pathfinding Algorithm -----------------------")
        choice = input("Type 'start' or 'exit' if you wanna leave\n")

        if choice.lower() == 'start':
            maze = maze_creator.create_maze()
            path = algo.find_path(maze[0], maze[1], maze[2], maze[3], maze[4])
            drawing.draw(maze[1], maze[4], maze[2], maze[3], path)
            print("\nPress Space to continue...")
            keyboard.wait('space')

        elif choice.lower() == 'exit':
            print("\nPress Space to Exit...\n")
            keyboard.wait('space')
            break
        
        else:
            print("\nEnter either start or exit...\n")
            time.sleep(1.3)

if __name__ == "__main__":
    main()