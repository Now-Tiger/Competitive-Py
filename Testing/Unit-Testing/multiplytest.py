#!/usr/bin/ python3
import multiply
import unittest


class TestMultiply(unittest.TestCase):
    def test_with_two_positives(self):
        self.assertEqual(multiply.numpy_multiply(17, 19), 17 * 19)
        self.assertEqual(multiply.numpy_multiply(1, 2), 2)

    def test_with_one_zero(self):
        self.assertEqual(multiply.numpy_multiply(17, 0), 0)
        self.assertEqual(multiply.numpy_multiply(0, 17), 0)

    def test_with_zeroes(self):
        self.assertEqual(multiply.numpy_multiply(0, 0), 0)

    def test_with_one_negative(self):
        self.assertEqual(multiply.numpy_multiply(17, -19), 17 * (-19))
        self.assertEqual(multiply.numpy_multiply(-19, 17), (-19) * 17)

    def test_with_two_negatives(self):
        self.assertEqual(multiply.numpy_multiply(-17, -19), 17 * 19)


if __name__ == "__main__":
    unittest.main()
    
    
# $ python multiplytest.py
# .....
# ------------------------
# Ran 5 tests in 0.000s

# OK
