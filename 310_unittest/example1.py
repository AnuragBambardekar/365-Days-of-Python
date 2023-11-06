import unittest

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

class MyTestCase(unittest.TestCase):
    def test_addition(self):
        result = add(2, 3)
        self.assertEqual(result, 5)

    def test_subtraction(self):
        result = subtract(5, 2)
        self.assertEqual(result, 3)

if __name__ == "__main__":
    unittest.main()


# python -m unittest my_test_module.py
