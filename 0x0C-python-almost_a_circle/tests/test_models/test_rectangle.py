#!/u/sr/bin/pythion3
import unittest
import io
import os
import sys
from io import StringIO
from contextlib import redirect_stdout
from models.base import Base
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
        
        """testing for varoius TypeError"""
        with self.assertRaises(TypeError):
            rect = Rectangle("1", 5)

        with self.assertRaises(TypeError):
            rect = Rectangle([10, 6], 5)

        with self.assertRaises(TypeError):
            rect = Rectangle(5, [10, 6])

        with self.assertRaises(TypeError):
            rect = Rectangle("string", 5)

        with self.assertRaises(TypeError):
            rect = Rectangle(1.34, 5)

        with self.assertRaises(TypeError):
            rect = Rectangle(5, 1.34)

        """testing for various ValueError"""
        with self.assertRaises(ValueError):
            rect = Rectangle(0, 5)

        with self.assertRaises(ValueError):
            rect = Rectangle(-4, 5)
            rect = Rectangle(5, -4)

        with self.assertRaises(ValueError):
            rect = Rectangle(-2, 3, 4, 5, 6)

    def test_height(self):
        self.assertEqual(10, self.rec.height)

        """testing for varoius TypeError"""
        with self.assertRaises(TypeError):
            rect = Rectangle("1", 5)

        with self.assertRaises(TypeError):
            rect = Rectangle([10, 6], 5)

        with self.assertRaises(TypeError):
            rect = Rectangle(5, [10, 6])

        with self.assertRaises(TypeError):
            rect = Rectangle("string", 5)

        with self.assertRaises(TypeError):
            rect = Rectangle(1.34, 5)


        with self.assertRaises(TypeError):
            rect = Rectangle(5, 1.34)

        """testing for various ValueError"""
        with self.assertRaises(ValueError):
            rect = Rectangle(0, 5)

        with self.assertRaises(ValueError):
            rect = Rectangle(-4, 5)

        with self.assertRaises(ValueError):
            rect = Rectangle(5, -4)

        with self.assertRaises(ValueError):
            rect = Rectangle(-2, 3, 4, 5, 6)

    def test_x(self):
        """testing for x"""
        self.rec.x = 54
        self.assertEqual(54, self.rec.x)
        self.assertEqual(0, self.rec.y)

        """testing for various TypeError"""
        with self.assertRaises(TypeError):
            rect = Rectangle(1, 5, 'str', 4, 3)

        with self.assertRaises(TypeError):
            rect = Rectangle(1, 5, [2, 3], 4, 3)

        with self.assertRaises(TypeError):
            rect = Rectangle(1, 5, 2.3, 4, 5)

        """testing for various ValueError"""
        with self.assertRaises(ValueError):
            rect = Rectangle(1, 5, -3)

        with self.assertRaises(ValueError):
            rect = Rectangle(1, 5, -4, -3, 4)

    def test_y(self):
        """testing for y"""
        self.rec.y = 45
        self.assertEqual(45, self.rec.y)
        self.assertEqual(0, self.rec.x)
        
        """testing for various TypeError"""
        with self.assertRaises(TypeError):
            rect = Rectangle(2, 4, 4, 'str', 3)

        with self.assertRaises(TypeError):
            rect = Rectangle(2, 4, 4, [2, 4], 3)

        with self.assertRaises(TypeError):
            rect = Rectangle(2, 4, 4, 1.23, 3)

        """testing for various ValueError"""
        with self.assertRaises(ValueError):
            rect = Rectangle(2, 4, 4, -3, 3)

        with self.assertRaises(ValueError):
            rect = Rectangle(2, 4, -4, -2, 4)

    def test_area(self):
        """testing for area"""
        self.assertEqual(self.rec.area(), 5 * 10)
        rect = Rectangle(3, 2, 4, 4, 2)
        self.assertEqual(rect.area(), 3 * 2)

    def test_str(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (5) 3/4 - 1/2", str(rect))
    

    def test_display_square(self):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        rect = Rectangle(10, 4)
        rect.display()
        sys.stdout = sys.__stdout__
        output = ("##########\n" +
                  "##########\n" +
                  "##########\n" +
                  "##########\n")


if __name__ == "main__":
    unittest.main()
