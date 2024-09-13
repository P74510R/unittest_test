import unittest

def calculate_rectangle_area(length, width):
  """Calculates the area of a rectangle.

  Args:
    length: The length of the rectangle.
    width: The width of the rectangle.

  Returns:
    The area of the rectangle.
  """
  return length * width

class TestRectangleArea(unittest.TestCase):

  def test_positive_values(self):
    self.assertEqual(calculate_rectangle_area(5, 3), 15)

  def test_zero_length(self):
    self.assertEqual(calculate_rectangle_area(0, 3), 0)

  def test_zero_width(self):
    self.assertEqual(calculate_rectangle_area(5, 0), 0)

  def test_negative_values(self):
    with self.assertRaises(ValueError):
      calculate_rectangle_area(-5, 3)

if __name__ == '__main__':
  unittest.main()
