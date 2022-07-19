
# Full Name: Kevin T Le

# Student ID: 2406054

# Chapman Email: kevle@chapman.edu

# Course Number and Section: CPSC 230-07

# In Class Programming Assignment 4: Functions; Exercise #1

# Purpose: This program asks the user to enter a DNA string
# and it outputs the DNA string's complementary sequence and
# the reverse of the complementary sequence. Two functions were
# used to find the complement sequence and the reverse of the sequence

# Function will find complementary DNA string
def complement(DNA):

# Asks user for DNA string
    string_DNA = input("Enter your DNA string: ")
# Converts all characters to uppercase
    string_DNA = string_DNA.upper()
# Defines complementary DNA string variable
    complement_DNA = ""

# Function will loop through each character and concatenate complementary base to seperate new string
    for i in string_DNA:
        if i == "A":
            complement_DNA += "T"
        elif i == "T":
            complement_DNA += "A"
        elif i == "G":
            complement_DNA += "C"
        elif i == "C":
            complement_DNA += "G"
# If a character other than "A", "T", "C", or "G" is detected, the complementary DNA string variable will be null
        else:
            complement_DNA = None
            break

    return complement_DNA

# Function reverses the complementary DNA string using String Slicing
def rev_complement(comp_DNA):
    return comp_DNA[::-1]

# Beginning of program

# Explanation of program
print("\nThis program finds the complement and reverse complement DNA sequences of the inputted DNA string.\n")

# Define DNA_string
string_DNA = ""

# Runs the complement function to find complementary DNA string
string_DNA = complement(string_DNA)

# Keeps asking user to enter new input if invalid DNA string
while string_DNA == None:
    print("Invalid DNA string. ", end = "")
    string_DNA = complement(string_DNA)

# Prints complement DNA string
print("\nYour DNA string complement is:", string_DNA)
# Prints reverse complement DNA string
print("\nYour reverse DNA string complement is:", rev_complement(string_DNA), "\n")
