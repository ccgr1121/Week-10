import unittest

class TestStringMethods(unittest.TestCase):
    def test_capitalise(self):
        text="hello"
        self.assertEqual("Hello", text.capitalize())
    def test_replace(self):
        text="hello"
        self.assertEqual("Bello", test.replace("h", "B"))