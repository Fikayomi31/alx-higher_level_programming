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

    def test_rectangle_id(self):
        """testing for the id of rectangle"""
        rect = (1, 33, 0, 0, 199)
        self.assertEqual(199, rect.id)


if __name__ == "__main__":
    unittest.main()
