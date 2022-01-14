import creating_data_header
import random

def main():

###################
    # Generating two lists that produce a random number of elements, one with numbers and the other with text

    for i in range(creating_data_header.__random_list_size__):
        random_num = random.randint(1, 500)

        while (check_duplicate_num(random_num, i) == True):
            random_num = random.randint(1, 500)
        #    print("TRUE")
        #else:
        #    print("FALSE: EXIT")
            
        creating_data_header.ids.append(random_num)
        creating_data_header.data.append("")

        for j in range(creating_data_header.__max_char_string__):
            creating_data_header.data[i] += chr(random.randint(33, 122))

            """
            ### Second option for generating random text ###
            if (random.randint(1,2) % 2 == 0):
               creating_data_variables.data[i] += chr(ord('a') + (random.randint(0, creating_data_variables.__max_char_string__)))
            else:
               creating_data_variables.data[i] += chr(ord('A') + (random.randint(0, creating_data_variables.__max_char_string__)))
            """

     #print(creating_data_header.RANDOM_LIST_SIZE)
     #print(creating_data_header.ids)
     #print(creating_data_header.data)
###################



###################
# "check_duplicate_num()" function checks for non-unique elements in "ids[]"
def check_duplicate_num(random_num, current_i_loop):
    duplicate_found = False
    i = 0

    while (i < current_i_loop):
        if creating_data_header.ids != None and random_num == creating_data_header.ids[i]:
            duplicate_found = True
        i += 1

    return duplicate_found
###################



main()