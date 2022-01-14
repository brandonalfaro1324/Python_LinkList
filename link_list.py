from data import Node

class Link_List():
    def __init__(self):
        self.head = None
     
    """
    def __del__(self):
        #("Deleting Everything")
        pass 
    """


    
    def addNode(self, int_id, string_data):
        add_node_sucess = False

        # Checking if id is above 0 and data is not empty #
        if int_id > 0 and string_data != "":
            # Checking if id needs to be place in self.head #
            if self.head == None or int_id < self.head.data.id:   
                self.addHead(int_id, string_data) # Passing data to "addHead()"#
                add_node_sucess = True # set add_node_sucess true #
            

        return add_node_sucess

    
    """
    def deleteNode(self, int_id_to_delete):
        pass
    """





############################################

    def addHead(self, new_head_id, new_head_data):
        # Cheking if self.head is empty #
        if self.head == None:
            print("Head Empty")

            self.head = Node(new_head_id, new_head_data)
            print(self.head.data.id)

        else:
            print("Head not Empty")

            new_head = Node(new_head_id, new_head_data, self.head)
            self.head = new_head

############################################




