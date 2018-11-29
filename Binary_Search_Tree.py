class node:
  def __init__(self,value = None):
    self.value = value
    self.right_child = None
    self.left_child = None
    self.parent = None
    self.frequency = 1

class Binary_tree:
  def __init__(self):
    self.root = None
  
  def inserting_node(self,value):
    """Method to insert node in tree , it takes a word(str) comapres it with existing words 
    and inserts at it respetive position in tree"""
    if self.root == None: 
      self.root = node(value)
    elif self.root != None:
      return self.insert_node(self.root,value)
    
  def insert_node(self,present_node,value):
    """Method to insert node in tree and create a node at left and right position accordingly
    also increases frequecny of the node if two words appear again"""
    if value == present_node.value:
      present_node.frequency = present_node.frequency + 1
    if value < present_node.value:
      if present_node.left_child == None:
        present_node.left_child = node(value)
        present_node.left_child.parent = present_node
      else:
        return self.insert_node(present_node.left_child,value)
    elif value > present_node.value:
      if present_node.right_child == None:
        present_node.right_child = node(value)
        present_node.right_child.parent = present_node
      else:
        return self.insert_node(present_node.right_child,value)
    else:
      
       return print("World Already in tree , frequecny increased : {}.".format(value))
  
  
  def print_tree(self):
    """method to print tree if tree empty returns a string with respective message"""
    if self.root == None:
      return 'Tree is Empty'
    else:
      print("Printing Tree Elements In Pre-Order Format :- ")
      self.pre_order_traversal(self.root)
  
  
  def pre_order_traversal(self,present_node):
    """Method to print the entire tree , it starts from the root node goes to the left side
    of the tree and returns to print the right side of tree recurisvely"""
    if present_node == None: 
      return
    print("{}".format(present_node.value))
    self.pre_order_traversal(present_node.left_child)
    self.pre_order_traversal(present_node.right_child)
    
  def search_return(self,value):
    if self.root != None:
      print("Travesing Path To Node :-")
      print(self.root.value)
      return self.searching_element(value,self.root)
    else:
      return print("No Elements In Tree")
  
  def searching_element(self,value,cur_node):
    """method to search for the word in tree , with a base case if it founds , recursively 
    compares with left and right child and keeps moving downwards returns the node and accepts an word(str)"""
    
    if value == cur_node.value:
      print("Word Present : YES")
      return cur_node
    elif value < cur_node.value and cur_node.left_child != None:
      print(cur_node.left_child.value)
      return self.searching_element(value , cur_node.left_child)
    elif value > cur_node.value and cur_node.right_child != None:
      print(cur_node.right_child.value)
      return self.searching_element(value , cur_node.right_child)
    else:
      print("Word Present : NO ")
      return cur_node
  
  def delete_node(self,value):
    """method to delete node accepts a word(str) calls search_return to return the node with that word,
    to delete , and deletes the node accordingly to the number of children it has"""
    if self.root == None:
      return print("Tree empty Insert first")
    else:
      deleting_node = self.search_return(value)
    def childrens(node):
      number_of_childrens = 0
      if node.left_child != None:
        number_of_childrens += 1
      if node.right_child != None:
        number_of_childrens += 1
      return number_of_childrens
    
    number_of_childrens = childrens(deleting_node)

    if number_of_childrens == 0:
      if deleting_node.parent.left_child == None:
        deleting_node.parent.right_child  = None
      else:
        deleting_node.parent.left_child =  None
        
    if number_of_childrens == 1:
      if deleting_node.left_child != None:
        dele_child = deleting_node.left_child
      else:
        dele_child = deleting_node.right_child
      
      if deleting_node.parent.left_child == deleting_node:
        deleting_node.parent.left_child = dele_child
      else:
        deleting_node.parent.right_child = dele_child
      
    if number_of_childrens == 2:
        left_side = deleting_node.right_child
        while left_side.left_child == None:
          if left_side.right_child !=  None:
            left_side = left_side.right_child
          else:
            break
        if left_side.left_child != None:
          deleting_node.value = left_side.left_child.value
          left_side.left_child = None
        else:
          deleting_node.value = left_side.value
          left_side.parent.right_child =  None
    print("Node Deleted") 
def filling_tree(tree):
  """ A function to fill the tree accepts the tree(object) imports reges module which helps 
  to helps to split , add in list and remove commas , punctuation or full stops , and insert 
  in the tree"""
  import re 
  with open('binary.txt','r') as file:
    file_contents = file.readline()
    valueList = re.sub("[^\w]", " ",  file_contents).split()
    for i in valueList:
      tree.inserting_node(int(i))  
  return tree


tree = Binary_tree()
tree = filling_tree(tree)
tree.print_tree()
tree.inserting_node(9)
tree.search_return(20)
tree.delete_node(8)
tree.print_tree()



          
          
