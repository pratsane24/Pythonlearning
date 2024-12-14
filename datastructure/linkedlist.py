class Node:
    def __init__(self,data = None, next = None):
        self.data = data
        self.next = next
class linkedlist:
    def __init__(self):
        self.head = None

    def insert_at_begining(self,data):
        node = Node(data,self.head)
        self.head = node
    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)



    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_values(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)


if __name__ == '__main__':
    ll = linkedlist()
    # ll.insert_at_begining(5)
    # ll.insert_at_begining(89)
    # ll.insert_at_end(79)
    # ll.insert_at_end(1)
    # ll.insert_at_end(957)
    # ll.insert_values(["Banana","Mango","Apple","Orange","Grapes"])
    # ll.print()

