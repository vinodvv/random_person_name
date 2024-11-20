import random


def read_names(filename):
    """Read names from a text file and return a list of names"""
    try:
        with open(filename, 'r') as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print("File not found. Please check the filename and try again.")
        return []


def total_names(filename):
    """Find the total number of names in the file"""
    names = read_names(filename=filename)
    print(f"Total number of names in the file: {len(names)}")


def add_name(filename, name):
    """Add a new name to the file"""
    with open(filename, 'a') as file:
        file.write(name.title() + "\n")
    print(f"{name.title()} has been added to the file.")


def select_random_name(filename):
    """Select a random name from the file"""
    names = read_names(filename)
    if names:
        selected_name = random.choice(names)
        print(f"Randomly selected name: {selected_name}")
    else:
        print("File is empty!")


def main():
    filename = "names.txt"

    while True:
        print("\nPlease select an option: ")
        print("1. Show the total number of names")
        print("2. Add new name")
        print("3. Select a random name")
        print("4. Exit")

        try:
            option = int(input("\nEnter your choice (1-4): "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 4.")
            continue

        if option == 1:
            total_names(filename=filename)
        elif option == 2:
            new_name = input("Enter the new name to add: ")
            if new_name.strip():
                add_name(filename, new_name)
            else:
                print("Please enter a valid name.")
        elif option == 3:
            select_random_name(filename)
        elif option == 4:
            print("Thank you for using Advanced Person Name Generator!")
            break
        else:
            print("Invalid input! Please enter a number between 1 to 4.")


if __name__ == "__main__":
    main()
    