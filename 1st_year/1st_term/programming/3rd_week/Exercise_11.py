#This exercise aims to prove the efficency of the slicing in strings

#Original strings
twinkle_twinkle = """Twinkle, twinkle, little star,
    how I wonder what you are!
        Up above the world so high,
        like a diamond in the sky.
Twinkle, twinkle, little star,
    how I wonder what you are."""

#Declaring the variables using string slicing
first_part = twinkle_twinkle[:30]
second_part = twinkle_twinkle[70:97]
third_part = twinkle_twinkle[-26:]

#Printing the result
print(first_part, "\n", second_part, "\n", third_part)