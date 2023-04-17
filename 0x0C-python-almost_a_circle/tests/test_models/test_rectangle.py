#!/u/sr/bin/python3
import unittest
from models.rectangle import Rectangle


class test_rectanglr(unittest.TestCase):
    """testing rectangle"""
    
    def setUp(self):
        """setting the width and height
        for the rectangle
        """
        self.rec = Rectangle(5, 10)

    def tearUp(self):
        """deleting instances created"""
        del self.rec

    def test_width(self):
        self.assertEqual(5, self.rec.width)

    def test_height(self):
        self.assertEqual(10, self.rec.height)

    def test_x(self):
        """testing for x"""
        self.rec.x = 54
        self.assertEqual(54, self.rec.x)
        self.assertEqual(0, self.rec.y)

    def test_y(self):
        """testing for y"""
        self.rec.y = 45
        self.assertEqual(45, self.rec.y)
        self.assertEqual(0, self.rec.x)

    def test_area(self):
        """testing for area"""
        self.assertEqual(self.rec.area(), 5 * 10)
        rect = Rectangle(3, 2, 4, 4, 2)
        self.assertEqual(rect.area(), 3 * 2)

if __name__ == "__main__":
    unittest.main()
