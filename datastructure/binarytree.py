# What problem does binary tree solve?
# Set in python
# It is same as list but In list you can save duplicate while in set u can't save duplicate.

# Depth first Search
class BinarySearchTreeNode :
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self,data):
        if data == self.data:
            return

        if data < self.data:
            # IF DATA IN LEFT SUB-TREE
            if self.left:
                self.left.add_child(data)
                
            else:
                self.left = BinarySearchTreeNode(data)
            
        else:
            # IF DATA IN RIGHT SUB-TREE
            if self.right:
                self.right.add_child(data)

            else:
                self.right = BinarySearchTreeNode(data) 

    def in_order_traversal(self):
        elements = []
        # Visit left tree
        if self.left:
            elements += self.left.in_order_traversal()

        # Visit Base Node
        elements.append(self.data)

        # Visit Right Node
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def search(self,val):
        if self.data == val:
            return True

        if val < self.data:
            # Val might be in left subtree
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            # Val might be in right subtree
            if self.right:
                return self.right.search(val)
            else:
                return False
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()
    
    def delete(self,val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.right
            
            min_val = self.right.find_min()
            self.data = min_val  
            self.right = self.right.delete(min_val)

        return self         

        
def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == '__main__':
    numbers = [17,4,1,20,9,23,18,34,18,4]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.in_order_traversal())
    numbers_tree.delete(20)
    print("After Deleting 20 ", numbers_tree.in_order_traversal())
    numbers_tree.delete(17)
    print("After Deleting 17 ", numbers_tree.in_order_traversal())

# # It removes duplicate.
#     print(numbers_tree.search(20))
#     print(numbers_tree.search(21))
#     OUTPUT IS TRUE since no 20 exist in the above set.
#     OUTPUT IS FALSE since no 21 exist in the above set.


# if __name__ == '__main__':
#     countries = ["India","Pakistan","Germany","USA","China","India","UK","USA","Norway"]
#     country_tree = build_tree(countries)

    # print("UK is in the list? ", country_tree.search("UK"))
    # print("Sweden is in the list? ", country_tree.search("Sweden"))

    # print(country_tree.in_order_traversal())
    # Countries will be sorted according to alphabetical order.

# Deleting a node from binary tree
# 1. Delete a node with no child, In this you can directly delete the node.
# 2. DElete a node with 1 child , In this the child node comes up & take the place of delated node.
# 3. Delete a node with 2 cildren, In this you have to rebalance your tree in a way that the basic properties of binary search tree holds true.

