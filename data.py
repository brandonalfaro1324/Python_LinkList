class Struct_link_data:
    def __init__(self, int_id, string_data):
        self.id = int_id
        self.data = string_data
    

class Node():

    def __init__(self, int_id = 0, string_data = "", next_node = None, prev_node = None):
        self.next = next_node
        self.prev = prev_node

        self.data = Struct_link_data(int_id, string_data)
