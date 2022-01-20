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
            elif int_id > self.head.data.id and int_id < self.tail.data.id:
                # "_addMiddle()" returns True or False, depending if #
                # -"int_id" does or doesn't exist in any Link List Nodes #
                # add_node_success = self._addMiddle(int_id, string_data)
                pass
            # id will always go if it's larger than tail's id #
            else:
                # pass data to "_addTail() and expect a return True #
                # add_node_success = self._addTail(int_id, string_data)
                pass

        return add_node_success


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
            first_node = Node(new_head_id, new_head_data)
            # Set the first Node to both head and tail #
            self.head = first_node
            self.tail = first_node
        # Go here if head and tail are the same, and set new #
        # -Node to head and assign new Node.next to tail #
        elif self.head == self.tail:
            # Set new Node.next to self.tail and re-organize Link List #
            new_head = Node(new_head_id, new_head_data, self.tail)
            self.head = new_head
            self.tail.prev = self.head
        # Go here if new "id" is less than id in head #
        else:
            # Set self.head.prev to new Node and make new Node new Head #
            new_head = Node(new_head_id, new_head_data, self.head)
            self.head = new_head

        # Always return True, since "_addHead()" would always set a new head Node #
        return True


    """
    def _addMiddle(self, new_head_id, new_head_data):
        pass

    def _addTail(self, new_head_id, new_head_data):
        pass
    """

    ############################################
    # Other useful functions
    # printLink does what it says, prints all id's in Link List #
    def printLink(self):
        if (self.head != None):
            temp_node = self.head
            while temp_node != None:
                print(temp_node.data.id)
                temp_node = temp_node.next
