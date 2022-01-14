#####################################
# A quick Link List data structure


#####################################

from creating_data import creating_data_header as ids_lists
from link_list import Link_List


# Setting new variable for link list data structure #
list = Link_List()

print("\nPrinting List for data's and id's\n\n")

# Printing out all elements in lists id and data #
for i in range(ids_lists.__random_list_size__):
    print(ids_lists.ids[i], ": ", ids_lists.data[i])

print("\nNow creating starting Link List\n")

list.addNode(5, "10")


list.addNode(1, "10")




