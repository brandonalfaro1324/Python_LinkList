from data import Node


class Link_List():
    def __init__(self):
        # Create and set self. head and tail to None #
        self.head = None
        self.tail = None

    """
    def __del__(self):
        # Delete all Nodes in Link #
        pass 
    """


    ############################################
    # Public Functions #

    def addNode(self, int_id, string_data):
        add_node_success = False

        # Checking if id is above 0 and data is not empty #
        if int_id > 0 and string_data != "":
            # Checking if id needs to be place in self.head #
            if self.head == None or int_id < self.head.data.id:
                # pass data to "_addHead() and expect a return True #
                add_node_success = self._addHead(int_id, string_data)
            # Checking if id needs to be place between head and tail id #
            elif self.head.data.id < int_id < self.tail.data.id:
                # "_addMiddle()" returns True or False, depending if #
                # -"int_id" does or doesn't exist in any Link List Nodes #
                add_node_success = self._addMiddle(int_id, string_data)
            # id will always go if it's larger than tail's id #
            elif self.tail.data.id < int_id:
                # pass data to "_addTail() and expect a return True #
                add_node_success = self._addTail(int_id, string_data)
        return add_node_success  # Returns True or False depending if Data is added to Link List #

    """
    def deleteNode(self, int_id_to_delete):
        pass
    """


    ############################################

    ############################################
    # Private Functions #

    def _addHead(self, new_head_id, new_head_data):
        # Checking if self.head is empty, if so set new Node to head and tail #
        if self.head == None:
            # Set the first Node to both head and tail #
            first_node = Node(new_head_id, new_head_data)
            self.head = first_node
            self.tail = first_node
        # Go here if head and tail are the same, and set new #
        # -Node to head and pass "self.tail" to "Node" 3rd argument #
        elif self.head == self.tail:
            # Set new "Node.next" to "self.tail" and re-organize Link List #
            new_head = Node(new_head_id, new_head_data, self.tail)
            self.head = new_head
            self.tail.prev = self.head
        # Go here if new "new_head_id" is less than id in head #
        else:
            # Set self.head.prev to new "Node" and make new "Node" new Head #
            new_head = Node(new_head_id, new_head_data, self.head)
            self.head.prev = new_head
            self.head = new_head
        # Always return True, since "_addHead()" would always set a new head Node #
        return True


    def _addMiddle(self, new_head_id, new_head_data):
        add_node_success = False  # Set False and later True when adding new Data passes #
        stop_while_search = True  # Set True and later False to stop while loop #
        temp_node = self.head  # Set "temp_node" to the beginning of "self.head" #

        # While Loop goes through all id's in Link List and #
        # - checks if that id can be added to Link List #
        while temp_node != self.tail and stop_while_search == True:
            # Go here if new id is greater than current "temp_node.data.id" #
            # -and less than "temp_node.next.data.id" #
            if temp_node.data.id < new_head_id < temp_node.next.data.id:
                # Create new "Node" and insert "Node" between current #
                # -"temp_node" and the next "temp_node"
                new_node = Node(new_head_id, new_head_data, temp_node.next, temp_node)
                temp_node.next.prev = new_node
                temp_node.next = new_node

                add_node_success = True  # Set variable True, new Node is added to Link List #
                stop_while_search = False  # Set variable False to stop while loop #
            # Go here if "new" id already exist in Link List #
            elif new_head_id == temp_node.data.id:
                stop_while_search = False  # Stop while loop #

            temp_node = temp_node.next  # Set the current next node to "temp_variable" #
        return add_node_success  # Return a True or False #


    def _addTail(self, new_head_id, new_head_data):
        # Go here if head and tail are the same, and set new #
        # -Node to tail and pass "self.head" to "Node" 4th argument #
        if self.head == self.tail:
            # Set "self.head" to "Node.prev" and re-organize Link List #
            new_tail = Node(new_head_id, new_head_data, None, self.head)
            self.tail = new_tail
            self.head.next = self.tail
        # Go here if new "new_head_id" is bigger than tail's id #
        else:
            # Set self.tail.next to new "Node" and make new "Node" new Tail #
            new_tail = Node(new_head_id, new_head_data, None, self.tail)
            self.tail.next = new_tail
            self.tail = new_tail
        return True  # Return True always, since going to "_addTail()" guarantees a new Tail #



    ############################################
    # Other useful functions

    # printLink does what it says, prints all id's in Link List #
    def printLink(self):
        temp_node = self.head
        temp_node2 = self.tail
        while temp_node != None:
            print(temp_node.data.id, "\t", end="")
            for i in range(temp_node.data.id):
                print('#', end='')
            print()
            temp_node = temp_node.next

        print("\n")

        while temp_node2 != None:
            print(temp_node2.data.id, "\t", end="")
            for i in range(temp_node2.data.id):
                print('#', end='')
            print()
            temp_node2 = temp_node2.prev