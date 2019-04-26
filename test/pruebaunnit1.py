import unittest
from funciones11 import functions111

class TestCollectionMethods(unittest.TestCase):

 def test_mayor(self):

  lista = (2, 3, 4, 5, 6)

  result1 = functions111.mayor(lista)
  self.assertEqual(result1, (6))


 def test_menor(self):

  lista2 = (8, 13, 2, 7, 6)

  result2 = functions111.menor(lista2)
  self.assertEqual(result2, (2))