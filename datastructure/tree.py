class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self,child):
        child.parent = self
        self.children.append(child)

    # def __str__(self):
    #     children_data = [child.data for child in self.children]
    #     return f"TreeNode({self.data},Children = {children_data})"
        

# def built_product_tree():
#     root = TreeNode("Electronics")
#     laptop = TreeNode("Laptop")
#     root.add_child(laptop)
#     return root 

# if __name__ == '__main__':
#     root = built_product_tree()
#     print("Root Node:", root)
   
# NOTE:- THE ABOVE E.G IS OF DEMO OR JUST FOR REFERENCE, NOW LET'S CREATE FULL TREE

    def print_tree(self):
        spaces = ' ' * self.get_level() * 10
        prefix = spaces + "|__" if self.parent else ""
        
        print(prefix + self.data)
        if self.children: 
            for child in self.children:
                child.print_tree()

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1 
            p = p.parent
        return level

def built_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))

    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("iphone"))
    cellphone.add_child(TreeNode("vivo"))
    cellphone.add_child(TreeNode("Google Pixel"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("L.G"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    return root

if __name__ == '__main__':
    root = built_product_tree()
    root.print_tree()
    # print(root.level())
    # print("Root Node:", root)
    pass
   
