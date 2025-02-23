name = "mahmood sinan"

# len(name) # returns the length of the string
# name.find("a") # returns the first occurence in 0 indexed string
# name.rfind("a") # returns the last occurence in 0 indexed string
# name.find("p") # returns -1 if not found
# name.capitalize() # capitalize first letter
# name.upper() # make every character uppercase
# name.lower() # make every character lowercase
# name.isdigit() # returns True if the name contains only numbers, otherwise False
# name.isalpha() # returns True if the name contains only alphabetical letters, otherwise False
# name.count("a") # returns the number of occurence of a in name
# name.replace("a", "b") replaces all a with b, if "b" is just "" it eliminates all "a"

#***********************
# name[number] # returns the character at index-number in name
# name[start: end] # returns the substring starting from start index(inclusive) to end index(exclusive)
# name[start: end: step] # returns the substring starting from start index(inclusive) to end index(exclusive) taking only step-th characters only

# if start is ommitted, the python assummes it as 0 (if ':' is put on)
# if end is omitted, the python assummes it as ending index (if ':' is put on)
# if step is omitted, the python assummes it as 1 (getting every character)
# -1 is the index of last index, -2 is second last and so on
# if the step is -1, the substring will be reversed.



print(help(str)) # prints all string methods, hold enter to get more output

# print() will print just a new line character