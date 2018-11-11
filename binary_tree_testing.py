import unittest

from Binary_Search_Tree import Binary_tree,filling_tree
class Binary_tree_testing(unittest.TestCase):
  
  def setUp(self):
    self.tree  = Binary_tree()
    self.tree  = filling_tree(self.tree)
  
  def test_object_of_class(self):
    self.assertIsInstance(self.tree,Binary_tree)
    
  def test_filling_tree(self):
    import re
    with open('binary.txt','r') as file:
      file_contents = file.readline()
      valueList = re.sub("[^\w]", " ",  file_contents).split()
      checking_first_element = int(valueList[0])
      print(checking_first_element)
    self.assertEqual(self.tree.root.value,checking_first_element)
    self.assertNotEqual(self.tree.root,None)
  
  def 
    
if __name__ == '__main__':
  unittest.main()
  