import unittest
import example


class TestCase(unittest.TestCase):

    def test_one(self):
        self.assertEqual(example.add(5, 5), 10)

    def test_two(self):
        self.assertEqual(example.subtract(15, 5), 10)

    def test_three(self):
        self.assertEqual(example.multiply(5, 5), 25)

    def test_four(self):
        self.assertEqual(example.divide(25, 5), 5)


if __name__ == '__main__':
    unittest.main()
