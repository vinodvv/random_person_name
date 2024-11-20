import random


def random_person_name(filename):
    try:
        with open(filename, 'r') as file:
            # Read and clean up lines
            names = [line.strip() for line in file if line.strip()]
            if names:
                selected_name = random.choice(names)
                print(f"Randomly selected name: {selected_name}!")
            else:
                print("The file is empty.")
    except FileNotFoundError:
        print("File not found. Please check the filename and try again.")



if __name__ == "__main__":
    random_person_name("names.txt")
