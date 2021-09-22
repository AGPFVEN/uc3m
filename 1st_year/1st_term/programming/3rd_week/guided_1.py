"""This is the first guided exercie:
It is needed to fill the gaps in the """

#This text is the given one (the %s are the gaps which must be filled with the answers of the user)
text = """Given the current situation that King’s Landing is facing, the House %s is asking for your economic services because
of the following cause %s.
The estimated total quantity is %s gold coins. The loan will be returned during the %s following years with
%s of bank interest. Thus, the money recovered from the bank, once the loan is completely returned, will be %s
gold coins
I hope the bank will consider this proposal because the House %s always pays its debts."""

first_input = input("Name of the house ")

second_input = input("Name of a service")

third_input = float(input("Quantity of gold you want to get"))

fourth_input = input("Numbers of years you need to return the previous quantity")

fifth_input = float(input("Interest of the loan" + "%"))

sixth_input = third_input + (third_input * fifth_input)

seventh_input = first_input

print(text % (first_input, second_input, third_input, fourth_input, fifth_input, sixth_input, seventh_input))