import pyautogui 
import time
import os



positions = []


def record_mouse_positions():
    input("Press Enter to start recording mouse positions...")
    while True:
        x, y = pyautogui.position()
        positions.append((x, y))
        print(f"Recorded position: ({x}, {y})")
        choice = input("Press Enter to record the next position, or q to quit: ")
        if choice == "q":
            choice = input("Do you want to see the recorded positions? (y/n): ")
            if choice.lower() == "y" or choice.lower() == "yes":
                
                print(f"Recorded positions: {positions}")
                break
            else:       
                print("Exiting without showing recorded positions.")
                break
                
def file():
    choices = ["1. Save recorded positions to a file",
                "2. Load recorded positions from a file",
                "3. Clear positions from a file",
                "4. Back to main menu"]
    for line in choices:
        print(line.center(50), "\n")
    choice = input("Enter your choice with a number: ")
    if choice == "1":
        choice = input("Do you want to save the recorded positions to a file? (y/n): ")
        if choice.lower() == "y" or choice.lower() == "yes":
            file_path = "recorded_positions.txt"

            with open(file_path, "w") as file:
                for position in positions:
                    file.write(f"({position[0]}, {position[1]})\n")
            print(f"Recorded positions saved to {file_path}.")
        else:
            print("Exiting without saving recorded positions.")    
    elif choice == "2":
        file_path = "recorded_positions.txt"
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                loaded_positions = []
                for line in file:
                    x, y = line.strip()[1:-1].split(", ")
                    loaded_positions.append((int(x), int(y)))
            print(f"Loaded positions: {loaded_positions}")
            positions.clear()
            positions.extend(loaded_positions)
            return loaded_positions 
            
        else:
            print(f"No saved positions found at {file_path}.")
    elif choice == "3":
        file_path = "recorded_positions.txt"
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"Recorded positions cleared from {file_path}.")
    elif choice == "4":
        main()
    else:
        print("Invalid choice. Please try again.")
                

def move_mouse_to_positions(positions):
    input("Press Enter to start moving the mouse to the recorded positions...")
    for position in positions:
        pyautogui.moveTo(position)
        time.sleep(0.5)

def click_mouse_at_positions(positions):
    input("Press Enter to start clicking the mouse at the recorded positions...")
    choice = input("What btn do u wanna press?(left/right): ")
    if(choice.lower() == "left" or choice.lower() == "l"):
        for position in positions:
            pyautogui.leftClick(position)
            time.sleep(0.5)
    elif(choice.lower() == "right" or choice.lower() == "r"):
        for position in positions:
            pyautogui.rightClick(position)
            time.sleep(0.5)
    else:
        print("Invalid direction!")

def key_btn_press(positions):
    input("Press Enter to start throwing the items on the ground...")
    key = input("Enter the key you want to press while moving the mouse: ")
    pyautogui.mouseDown(button='left')
    for position in positions:
        pyautogui.moveTo(position)
        pyautogui.keyDown(key)
        #time.sleep(0.001)

def menu():
    text = ["---------Mouse Recorder Menu: ---------",
    "1. Record mouse positions (Do this first to get the positions!)",
    "2. Move mouse to recorded positions",
    "3. Click mouse at recorded positions",
    "4. Press a key while moving the mouse to recorded positions",
    "5. Remove the recorded positions (Clear the list)",
    "6. Recorded positions to a file",
    "7. Exit",
    "---------------------------------------"]
    for line in text:
        print(line.center(50), "\n")
def main():
    while True:
        menu()
        choice = input("Enter your choice with a number: ")
        
        if choice == "1":
            record_mouse_positions()
        elif choice == "2":
            move_mouse_to_positions(positions)
        elif choice == "3":
            click_mouse_at_positions(positions)
        elif choice == "4":
            key_btn_press(positions)
        elif choice == "5":
            positions.clear()
            print("Recorded positions cleared.")
        elif choice == "6":
            file()
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

main()