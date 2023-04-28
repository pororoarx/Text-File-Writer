# Text-File-Writer
A method in python to write multiple line of text contents into a text file mylife.txt.
======================================================================================================================================================================
Table of Contents
- Installation
- Usage
- Formulation
- Conclusion

======================================================================================================================================================================
- Installation:
Clone the repository to your local machine: ‘git clone ‘git@github.com:pororoarx/Text-File-Writer.git’
Install the required ‘pyfiglet’ module: ‘pip install pyfiglet’

- Usage:
Open Git Bash and go to the project directory.
Run the program: ‘file_handling_writer.py’
Enter the text you want to write in the file and press enter.
If you have more lines to add, type "y" when prompted and press enter. Otherwise, type "n" and press enter to exit the loop and close the file.

- Formulation:
This program uses the open() method in Python to open a file called mylife.txt in write mode. The while loop repeatedly prompts the user to input lines of text, which are then written to the file using the write() method. After each line is written, the user is asked if they have more lines to input. If the user enters "n", the loop breaks and the file is closed.

- Conclusion:
This program provides a simple way to write multiple lines of text to a file using Python. It can be easily modified to write to different files or to accept different types of input.
======================================================================================================================================================================
