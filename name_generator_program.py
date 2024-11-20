from random_person_name import random_person_name

while True:
    print("\nPlease select an option: ")
    print("1. Show the total number of names")
    print("2. Add new name")
    print("3. Select a random name")
    print("4. Exit")

    option = int(input("\nEnter your choice (1-4): "))

    filename = "names.txt"

    try:
        with open(filename, 'r') as file:
            names = [line.strip() for line in file if line.strip()]
        
        total_names = len(names)


        if option == 1:
            print(f"Total number of names in the file: {total_names}")

        elif option == 2:
            new_name = input("Enter the new name to add: ")
            if new_name.strip():
                with open(filename, 'a') as file:
                    file.write(new_name.title() + "\n")
                print(f"{new_name.title()} has been added to the file.")
            else:
                print("Please enter a valid name!")

        elif option == 3:
            random_name = random_person_name(filename=filename)
        
        elif option == 4:
            print("Thank you for using Advanced Person Name Generator!")
            break

        else:
            print("Invalid input! Please enter correct option from menu (i.e., 1 to 4)")

    except ValueError:
        print("Invalid input! Please enter correct option from menu (i.e., 1 to 4)")
