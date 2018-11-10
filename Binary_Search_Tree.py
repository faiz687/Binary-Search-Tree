class node:
  def __init__(self,value = None):
    self.value = value
    self.right_child = None
    self.left_child = None
    self.parent = None

class Binary_tree:
  def __init__(self):
    self.root = None
  
  def inserting_node(self,value):
    if self.root == None: 
      self.root = node(value)
    elif self.root != None:
      self.insert_node(self.root,value)
      
  def insert_node(self,present_node,value):
    if value < present_node.value:
      if present_node.left_child == None:
        present_node.left_child = node(value)
        present_node.left_child.parent = present_node
      else:
        self.insert_node(present_node.left_child,value)
    elif value > present_node.value: 
      if present_node.right_child == None:
        present_node.right_child = node(value)
        present_node.right_child.parent = present_node
      else:
        self.insert_node(present_node.right_child,value)
    else:
      print("Value In Tree")
  
  def print_tree(self):
    if self.root == None:
      print("Tree is Empty")
    else:
      self.pre_order_traversal(self.root)
  
  def pre_order_traversal(self,present_node):
    if present_node == None: 
      return
    print("{}".format(present_node.value))
    self.pre_order_traversal(present_node.left_child)
    self.pre_order_traversal(present_node.right_child)
    
  def search_return(self, value):
    if self.root != None:
      print("traversing path :-")
      print(self.root.value)
      return self.searching_element(value,self.root)
    else:
      return print("No Elements In Tree")
  
  def searching_element(self,value,cur_node):
    if value == cur_node.value:
      return (print("Value Found : {} ".format(value)),cur_node)
    elif value < cur_node.value and cur_node.left_child != None:
      print(cur_node.left_child.value)
      return self.searching_element(value , cur_node.left_child)
    elif value > cur_node.value and cur_node.right_child != None:
      print(cur_node.right_child.value)
      return self.searching_element(value , cur_node.right_child)
    return (print("Value Not Found : {} ".format(value)),cur_node)
  
  def delete_node(self,value):
    if self.root == None:
      return print("Tree empty Insert first")
    else:
      deleting_node = self.search_return(value)
      deleting_node = deleting_node[1]
      
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
        while left_side.left_child != None:
          left_side = left_side.left_child
        deleting_node.value = left_side.value
        if left_side.right_child == None:
          left_side.parent.left_child = None
        if left_side.right_child != None:
          left_side.parent.left_child =  left_side.right_child
          
        
        
      
      
      
      
      
        
    
    
      
      
      
    
      
    
    
    

  
  
  
my_tree = Binary_tree()
my_tree.inserting_node(5)
my_tree.inserting_node(0)
my_tree.inserting_node(2)
my_tree.inserting_node(1)
my_tree.inserting_node(23)
my_tree.inserting_node(12)
my_tree.inserting_node(7)
my_tree.inserting_node(9)
my_tree.inserting_node(45)
my_tree.inserting_node(33)
my_tree.print_tree()
#my_tree.search_return(21)
my_tree.delete_node(23)
my_tree.print_tree()
