inp = float(input("Enter a number, 0 to finish: "))
var_n = 0
var_even = 0
var_pos = 0

while(inp != 0):
	var_n += 1
	
	if(inp % 2 == 0):
		var_even += 1

	if(inp > 0):
		var_pos += 1

	inp = float(input("Enter a number, 0 to finish:"))

print("Summary:")
print("Numbers entered:" + str(var_n))
print("Odd numbers: " + str(var_n - var_even))
print("Even numbers: " + str(var_even))
print("Positive numbers: " + str(var_pos))
print("Negative numbers: " + str(var_n - var_pos))