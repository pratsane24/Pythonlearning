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


    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count


    def remove_at(self,index):
        if index<0 or index>self.get_length():
            raise Exception("Invalid index")

        if index==0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index -1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1

    def insert_at(self,index,data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index ==0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr :
            if count == index -1:
                node = None(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1    


if __name__ == '__main__':
    ll = linkedlist()
    # ll.insert_at_begining(5)
    # ll.insert_at_begining(89)
    # ll.insert_at_end(79)
    # ll.insert_at_end(1)
    # ll.insert_at_end(957)
    ll.insert_values(["Banana","Mango","Apple","Orange","Grapes"])
    ll.print()

    # QUESTION:- Impliment a function which can return the length of a linkedlist
    # print("Length: " ,ll.get_length())

    # Implement a method which can remove an element at a given index?
    # REmove element at index 2
    ll.remove_at(2)
    ll.print()

    # Insert at 0 index
    ll.insert_at(0,"figs")
    ll.print()

    ll.insert_at(2,"jackfruit") 
    #  ------> GETTING ERROR AT THIS POINT.
    ll.print()

    # NOTE :- ANOTHER EG
    # ll.insert_values([45,7,12,567,99])
    # ll.insert_at_end(67)
    # ll.print()
    # ll.remove_at(2)
    # ll.print()



