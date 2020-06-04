"""Write a string to a file and return the number of written characters"""


def write_file(filename="", text=""):
    """Function to wite a string to a text file"""    
    with open(filename, 'w') as myFile:        
        return (myFile.write(text))
