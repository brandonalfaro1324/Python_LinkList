from data import Node


class Link_List():
    def __init__(self):
        # Create and set self. head and tail to None #
        self.head = None
        self.tail = None


    def __del__(self):
        # Delete all Nodes in Link #
        print("\n")
        print(self.head)
        print(self.tail)


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
                add_node_success = self._addMiddle(int_id, string_data)
            # id will always go if it's larger than tail's id #
            elif self.tail.data.id < int_id:
                add_node_success = self._addTail(int_id, string_data)
        return add_node_success  # Returns True or False depending if Data is added to Link List #


    def deleteNode(self, int_id_delete):
        delete_node_success = False

        if int_id_delete > 0 and self.head != None:
            if int_id_delete == self.head.data.id:
                delete_node_success = self._deleteHead()

            elif int_id_delete == self.tail.data.id:
                delete_node_success = self._deleteTail()
                pass

            elif self.head.data.id < int_id_delete < self.tail.data.id:
                delete_node_success = self._deleteMiddle(int_id_delete)

        return delete_node_success  # Returns True or False depending if Data is deleted in Link List #


    ############################################

    ############################################
    # Private Functions #

    # addNode Function #
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
        return True  # Always return True, since "_addHead()" will always set new head#

    # addNode Function #
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

    # addNode Function #
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


    # deleteNode Function #
    def _deleteHead(self):
        # Go here to delete self.head #
        if self.head.next != None:
            # Assign "self.head.next" to be new head and delete "self.head" #
            next_new_head = self.head.next
            next_new_head.prev = None
            self.head.next = None
            self.head = next_new_head

        # Go here if "self.tail" is also "self.head" #
        else:
            # Set both self variables to None #
            self.head = None
            self.tail = None
        return True  # Return True, since "_deleteHead()" guarantees a deleted head Node #

    # deleteNode Function #
    def _deleteMiddle(self, delete_id):
        delete_node_success = False  # Variable to be sent back if Node gets deleted #
        stop_while_search = True  # Variable to stop's while loop #
        temp_node = self.head.next  # First Node to check its id #

        while temp_node != None and stop_while_search == True:
            # Go here if "delete_id" equal's to current id in "temp_node"
            if delete_id == temp_node.data.id:
                # Delete current Node and re-organize Link List #
                temp_node.prev.next = temp_node.next
                temp_node.next.prev = temp_node.prev

                delete_node_success = True
                stop_while_search = False  # Set variable False to stop while loop #
            temp_node = temp_node.next  # Assign "temp_node.next" Node to "temp_node"  #
        return delete_node_success

    # deleteNode Function #
    def _deleteTail(self):
        # Go here if previous tail doesn't equal to "self.head" #
        if self.tail.prev != None and self.tail.prev != self.head:
            # Delete tail and set previous tail node to new "self.tail" #
            next_new_tail = self.tail.prev
            next_new_tail.next = None
            self.tail.prev = None
            self.tail = next_new_tail

        # Go here if "self.tail.prev" is "self.head" #
        else:
            # Delete node "self.tail" and assign "self.head" #
            self.head.next = None
            self.tail.prev = None
            self.tail = self.head
        return True  # Return True, since "_deleteTail()" guarantees a deleted head Node #


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

        while temp_node2 != None:
            print(temp_node2.data.id, "\t", end="")
            for i in range(temp_node2.data.id):
                print('#', end="")
            print(" ",temp_node2,end="")
            print()
            temp_node2 = temp_node2.prev