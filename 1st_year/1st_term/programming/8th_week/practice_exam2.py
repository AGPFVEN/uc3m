print("Welcome to the Programming Course Movie Database (PCMDB)")
print("1: Enter a new film")
print("2: Like/dislike a film")
inp = int(input("Enter your option (0 exit): "))

films = [[],[],[]]

while (inp != 0):
	if(inp == 1):
		name = input("Enter the film name:" )
		films[0].append(name)
		films[1].append(0)
		films[2].append(0)
		print("")

	elif(inp == 2):
		for i in range(len(films[0])):
			print(str(i + 1) + " " + films[0][i])
			print("		likes: " + str(films[1][i]) + " dislikes: " + str(films[2][i]))

		locator = int(input("Enter the number of the movie you want to vote: "))
		inp = input("Did you like it (yes/no)? ")
		
		if(inp == "yes"):
			films[1][locator - 1] += 1

		elif(inp == "no"):
			films[2][locator - 1] += 1
		
		print("Thanks, now this film has:")
		print("Likes: " + str(films[1][locator -1]))
		print("Dislikes: " + str(films[2][locator -1]) + "\n")

	else:
		print("wrong option\n")

	print("1: Enter a new film")
	print("2: Like/dislike a film")
	inp = int(input("Enter your option (0 exit): "))

print("Thanks for using this program!")