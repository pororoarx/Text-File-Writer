# Write a method in python to write multiple line of text contents into a text file mylife.txt. 

# import pyfiglet
import pyfiglet

# Set and print the title of the activity in color and different font
title_of_assign = "Module 2 - Prob 3"
font = "slant"
print("\033[38;5;40m", pyfiglet.figlet_format(title_of_assign, font=font))


# Start
# Create a function called process
def process():
    # Open the mylife.txt (write)
    with open("mylife.txt", "w") as file_1:
        while True:
            # Ask the user to enter an input string
            input_text = input("Enter line: ")
            # Write the line to the file
            file_1.write(input_text + "\n")
            # Ask the user if they want to input string again
            input_more_lines = input("Are there more lines y/n? ")
            # If user enters 'n', exit the loop
            if input_more_lines.lower() == "n":
                break


# execute the function
process()