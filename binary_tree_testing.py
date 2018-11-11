import unittest
import sys 
import io
from Binary_Search_Tree import Binary_tree,filling_tree
class Binary_tree_testing(unittest.TestCase):
  
  def setUp(self):
    self.tree  = Binary_tree()
    filling_tree(self.tree)
    
  def test_object_of_class(self):
    self.assertIsInstance(self.tree,Binary_tree)
    
  def test_filling_tree(self):
    filltree = filling_tree(self.tree)
    self.assertIsNotNone(filltree.root.value)
  
  def test_inserting_node(self):
    filling_tree(self.tree)
    self.assertIsNotNone(self.tree.root)
    self.assertIsNotNone(self.tree.root.left_child)
    self.assertIsNotNone(self.tree.root.right_child)
    a = self.tree.inserting_node(2)
    self.assertEqual(a,'Value in tree') 
    
  def test_print_tree(self):
    self.assertIsNotNone(self.tree.root)
    self.assertIsNotNone(self.tree.root)
    printing_output = io.StringIO()
    sys.stdout = printing_output
    self.tree.pre_order_traversal(self.tree.root)
    self.assertEqual(printing_output.getvalue(),'5\n0\n2\n1\n23\n12\n7\n9\n45\n33\n34\n35\n')
    sys.stdout = sys.__stdout__
  
  def test_search_return(self):
      self.assertIsNotNone(self.tree.root)
      searchinhg_value = self.tree.search_return(100)[0]
      self.assertEqual('No',searchinhg_value)
      searchinhg_value =  self.tree.search_return(5)[0]
      self.assertEqual('Yes',searchinhg_value)
      
  def test_delete_node(self):
    self.tree.delete_node(5)
    self.assertNotEqual(self.tree.root.value,5)
    self.tree.delete_node(1)
    searchinhg_value = self.tree.search_return(1)[0]
    self.assertEqual(searchinhg_value,'No')
    self.tree.delete_node(0)
    searchinhg_value = self.tree.search_return(0)[0]
    self.assertEqual(searchinhg_value,'No')
    
      
    
    

      
  
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
if __name__ == '__main__':
  unittest.main()
  