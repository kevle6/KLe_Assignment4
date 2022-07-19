
# Full Name: Kevin T Le

# Student ID: 2406054

# Chapman Email: kevle@chapman.edu

# Course Number and Section: CPSC 230-07

# In Class Programming Assignment 4: Functions; Exercise #2

# Purpose: This program combines a couple name based on their two names. It utilizes
# three functions to find the first part of the name, the second part of the name, and
# then combines the two parts together into the final name.

# Function first_split returns first part of couple name up to and including the first consonant
def first_split(name_1):
    # User enters a name as a string
    name_1 = input("\nInput a name: ")
    # Verify name_1 input is only letters and prompts users to reenter if otherwise
    while name_1.isalpha() != True:
        name_1 = input("\nInvalid name. Input a new name: ")
    # First letter of name is converted into an uppercase letter
    name_1 = name_1.title()
    # First letter of 1st name is concatenated to the seperate "first part" string
    name_1_first = name_1[0]
    # Loop over each letter and add it into seperate "first part" string until there is a consonant
    for char in name_1[1:len(name_1)]:
        if char in vowel_list:
            name_1_first += char
        else:
            # Consonant is added to the sepearte string before the loop breaks
            name_1_first += char
            break

    # Function returns the first part of the couple name as a string
    return name_1_first

#Function last_split gets the last part of couple name after first consonant of 2nd input
def last_split(name_2):
    # User enters second name as string
    name_2 = input("\nInput another name: ")
    # Verify name_2 input is only letters and prompts users to reenter if otherwise
    while name_2.isalpha() != True:
        name_2 = input("\nInvalid name. Input another name: ")
    # First letter of name is converted to uppercase
    name_2 = name_2.lower()
    # Defining the string storing last part of 2nd name
    name_2_last = ""
    # If name starts with vowel, the 2nd part of couple name will be the whole 2nd name
    if name_2[0] in vowel_list:
        name_2_last = name_2
        # If the name starts with a consonant, the 2nd part of the couple name
        # will be after the first consonant, excluding the first letter in name
    else:
        consonant_index = 0
        for char in name_2[1:len(name_2)]:
            if char not in vowel_list:
                consonant_index = name_2.index(char) + 1
                break
        name_2_last = name_2[consonant_index:len(name_2)]

    # Function returns the first part of the couple name as a string
    return name_2_last

# Function couple_name concatenates first part and second part of couple name
def couple_name(name_1,name_2): #Function takes in two strings: First and Last part of couple name
    couple_name = name_1 + name_2

    # Function outputs couple name as a string
    return couple_name

vowel_list = ["A","a","E","e","I","i","O","o","U","u"]

name_1 = ""

name_2 = ""

print("\n\nThis program combines a couple name based on their two names.")
print("\n",couple_name(first_split(name_1),last_split(name_2)), "is the couple name.\n\n")
