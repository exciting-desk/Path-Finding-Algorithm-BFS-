import algo
import drawing
import gen_algo
import maze_creator
import keyboard
import os
import time

def main():
    while True:
        os.system('cls')
        print("     --------------------- Breadth First-Search Pathfinding Algorithm -----------------------")
        choice = input("1. Create maze\n2. Generate maze\n3. Exit\n")

        if choice.lower() == 'create' or choice == '1':
            maze = maze_creator.create_maze()
            print("\nPress Space to continue...")
            keyboard.wait('space') 

        elif choice.lower() == 'generate' or choice == '2':
            gen_algo.draw_maze(10)
            gen_algo.solve_maze()
            print("\nPress Space to Exit...\n")
            keyboard.wait('space')

        elif choice.lower() == 'exit' or choice == '3':
            print("\nPress Space to Exit...\n")
            keyboard.wait('space')
            break
        
        else:
            print("\nEnter a correct command...\n")
            time.sleep(1.3)

if __name__ == "__main__":
    main()