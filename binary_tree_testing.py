import unittest
import sys 
import io

from Binary_Search_Tree import Binary_tree,filling_tree
class Binary_tree_testing(unittest.TestCase):
  
  def setUp(self):
    self.tree  = Binary_tree()
    
  def test_object_of_class(self):
    self.assertIsInstance(self.tree,Binary_tree)
    
  def test_filling_tree(self):
    import re
    with open('binary.txt','r') as file:
      file_contents = file.readline()
      valueList = re.sub("[^\w]", " ",  file_contents).split()
      checking_first_element = int(valueList[0])
    #self.assertEqual(self.tree.root.value,checking_first_element)
    #self.assertNotEqual(self.tree.root,None)
  
  def test_inserting_node(self):
    elements_to_check = [5,1,2]
    for i in elements_to_check:
      self.tree.inserting_node(i)
    self.assertEqual(self.tree.root.value,elements_to_check[0])
    self.assertEqual(self.tree.root.left_child.value,elements_to_check[1])
    self.assertEqual(self.tree.root.right_child,None)
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    a = self.tree.inserting_node(2)
    self.assertEqual(capturedOutput.getvalue(),'Value in tree\n')
    sys.stdout = sys.__stdout__  
    
  def test_print_tree(self):
    a = self.tree.print_tree()
    print(a, 'hello')
    
    
      
    
if __name__ == '__main__':
  unittest.main()
  