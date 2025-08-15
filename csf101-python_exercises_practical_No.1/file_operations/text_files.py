#Write a function that creates a new text file and writes a few lines to it.


def create_and_write_file(filename):
    with open(filename, 'w') as file:
        file.write("This is the first line.\n")
        file.write("This is the second line.\n")
        file.write("This is the third line.\n")

create_and_write_file('sample.txt')
print("File created and written successfully.")