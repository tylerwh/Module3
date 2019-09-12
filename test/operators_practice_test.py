import unittest


class OperatorsTest(unittest.TestCase):


  def test_equal_operator(self):
    a = 7
    b = -2
    self.assertFalse(a == b)
  

  def test_notequal_operator(self):
    a = 5
    b = 4
    self.assertTrue(a != b)


  def test_greaterthan_operator(self):
    a = 9
    b = 8
    self.assertTrue(a > b)
  

  def test_lessthan_operator(self):
    a = 8
    b = 9
    self.assertFalse(b < a)
  

  def test_greaterthan_or_equalto_operator(self):
    a = 25
    b = 20
    self.assertTrue(a >= b)
  

  def test_lessthan_or_equalto_operator(self):
    a = -1
    b = 0
    self.assertTrue(a <= b)


if __name__ == "__main__":
    unittest.main()