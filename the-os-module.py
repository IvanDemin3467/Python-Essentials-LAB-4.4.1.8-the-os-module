# This is the Python Essentials 2 LAB 4.4.1.8 the-os-module

import os 

def find(where, what):
    # This function recursively searches "what" directory
    # in all directories starting from "where"
    for found in os.listdir(where):            # Iterate through files in current directory
        if found == what:                      # If found requred dir -> 
            print(".." + where + "/" + what)   # -> print curent path to cmd
        if os.path.isdir(where + "/" + found): # If found is a dir ->            
            find(where + "/" + found, what)    # -> recursively try to find in it


if __name__ == "__main__":
    find("./tree", "python")
