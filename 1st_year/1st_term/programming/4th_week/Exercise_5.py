#this program is to comparate ages
#first we need to ask for the inputs

f_name = input("Input a name")
s_name = input("Input another name")

f_age = int(input("Input age"))
s_age = int(input("Input another age"))

#then we compare them and print
if (f_name == s_name):
    print(f_name, " and ", s_name, " are the same age")

elif(f_age > s_age):
    print(f_name, " is older than ", s_name)

else:
    print(s_name, " is older than ", f_name)
