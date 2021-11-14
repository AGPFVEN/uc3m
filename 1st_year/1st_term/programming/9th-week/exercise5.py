import string

def corrector(your_list, mark):
    if(your_list[mark] in string.ascii_lowercase):
        if(mark == 0 or (your_list[mark -1] == " " and  your_list[mark] == "i" and your_list[mark + 1] == " ")):
                return your_list[mark].upper()
        
        else:
            aux = 1

            while(your_list[mark -aux] == " "):
                aux += 1

            first_non_blank = your_list[mark - aux]
            if(first_non_blank == "." or first_non_blank == "?" or first_non_blank == "!"):
                return your_list[mark].upper()

    return your_list[mark]

def str_to_list(your_str):
    final_ls = []
    
    for i in your_str:
        final_ls.append(i)

    return final_ls

def list_to_str(your_list):
    my_string = ""

    for i in your_list:
        my_string += i

    return my_string

a_str = "what time do i have to be there? what is the address?"

a_ls = str_to_list(a_str)

for i in range(len(a_ls)):
    a_ls[i] = corrector(a_ls, i)
    
print(list_to_str(list(a_ls)))