import os

def run_console():
    os.system("python console_editor.py")

def run_gui():
    os.system("python grid_editor.py")

def main():
    print("🧠 Welcome to GridWorld Launcher")
    print("[1] Console mode (main.py)")
    print("[2] GUI mode (grid_editor.py)")
    choice = input("Select a mode (1 or 2): ").strip()

    if choice == "1":
        run_console()
    elif choice == "2":
        run_gui()
    else:
        print("❌ Invalid choice. Exiting.")

if __name__ == "__main__":
    main()
