import unittest
import math


def Fibonacci(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a


def binet(n):
    sqrt5 = math.sqrt(5)
    return int((((1 + sqrt5) ** n - (1 - sqrt5) ** n) / (2 ** n * sqrt5)))


class MyTestCase(unittest.TestCase):

    def test_1_to_50_fib_comparing_2_diff_algorythm(self):
        myList = list(range(1, 50))

        for n in myList:
            self.assertEqual(binet(n), Fibonacci(n))  # add assertion here


if __name__ == '__main__':
    unittest.main()
