# Write a method in python to write multiple line of text contents into a text file mylife.txt. 

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
            # Ask the ser if they want to input string again
            # If user enters 'n', exit the loop


# execute the function