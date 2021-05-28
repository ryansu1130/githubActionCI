import unittest
import example

class TestCase(unittest.TestCase):
    def test_one(self):
        self.assertEqual(example.add(5,5), 10)

if __name__ == '__main__':
    unittest.main()
