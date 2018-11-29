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
    self.assertIsNotNone(self.tree.root.value)
  
  def test_inserting_node(self):
    self.assertIsNotNone(self.tree.root)
    self.assertIsNotNone(self.tree.root.left_child)
    self.assertIsNotNone(self.tree.root.right_child)
    a = self.tree.inserting_node("of")
    self.assertEqual(a,'World Already in tree , frequecny increased :of') 
    
  def test_print_tree(self):
    self.assertIsNotNone(self.tree.root)
    printing_output = io.StringIO()
    sys.stdout = printing_output
    self.tree.pre_order_traversal(self.tree.root)
    self.assertEqual(printing_output.getvalue(),printing_output.getvalue())
    sys.stdout = sys.__stdout__
  
  def test_search_return(self):
    empty_tree = self.tree.search_return("hello")
    self.assertNotEqual(empty_tree,'No Elements In Tree Insert First')
    node_absent  = self.tree.search_return("file")
    self.assertEqual(node_absent,'No')
    node_present = self.tree.search_return("Reason")
    self.assertIsNot(node_present,self.tree.root.value)
      
  def test_delete_node(self):
    delete_node =  self.tree.delete_node("the")
    self.assertNotEqual(delete_node,'Tree empty Insert first')
    self.assertEqual(delete_node,'Node Deleted')
        
if __name__ == '__main__':
  unittest.main()
  