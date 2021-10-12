#Ask for sentence and declaring my vars
inp = input("Input a sentence: \n")
characters = []

#Loop to fill the list
for char in inp:
    if(characters.count(char)):
        characters.append(char)

#Trasnform list in tuple
characters_tuple= tuple(characters)
print(characters)