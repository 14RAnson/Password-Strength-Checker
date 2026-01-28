# Password-Strength-Checker

# What the program is

A command-line based program to evaluate the strengths of passwords
using many different criteria while using an external API to check if words
in the password match words in the dictionary which would decrease its strength.
It decreases its strength as in attacks hackers would search through real english words
first.

# Criteria

The program analyses the strength of a password based on:
    Length
    Upper and lower case characters
    Special characters and numbers
    Whether words are valid english words using dictionaryapi.dev

# Purpose

I built this project to explore python further beyond the GCSE specification and in
particular to develop an understanding on APIs and how I can use them to help me enhance
my further projects. For this program to use a local list to store a dictionary would be unnecessary
which is why the API is important in reducing file size.

# Reflection

One of the errors I made was a logic error where my functions in the main program section
were the wrong way around so the program was requesting to use the password before the user
even inputted it. Surprisingly, this took me very long to figure out as the answer was so simple
yet so hard to find.

Another error was to do with line 26 and 35. Originally, I did not have the enumerate loop which
would have made the .index(character) return a value of the first index that a character appeared
making it non-functional for certain cases of repeated character passwords. I fixed this by adding the
enumerate loop to confirm it was actually the final character in the list.
