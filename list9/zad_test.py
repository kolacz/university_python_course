import unittest
from math import pi, log
from zad import *


class SimpleTestCase(unittest.TestCase):
    def testSkladana(self):
        self.assertEqual(doskonale_skladana(1000), [6, 28, 496],
                         "Wynik wersji skladanej jest niepoprawny")

    def testFunkcyjna(self):
        self.assertEqual(doskonale_funkcyjna(1000), [6, 28, 496],
                         "Wynik wersji funkcyjnej jest niepoprawny")

    def testIterator(self):
        self.assertEqual(doskonale_iter(1000), [6, 28, 496],
                         "Wynik wersji z iteratorem jest niepoprawny")

    def testDomain(self):
        self.assertRaises(ArgumentNotIntegerError, doskonale_skladana, 1.5)
        self.assertRaises(ArgumentNotIntegerError, doskonale_funkcyjna, pi)
        self.assertRaises(ArgumentNotIntegerError, doskonale_iter, log(17))


class BigTestCase(unittest.TestCase):
    def testSkladana(self):
        self.assertEqual(doskonale_skladana(10000), [6, 28, 496, 8128],
                         "Wynik wersji skladanej dla dużego n jest niepoprawny")

    def testFunkcyjna(self):
        self.assertEqual(doskonale_funkcyjna(10000), [6, 28, 496, 8128],
                         "Wynik wersji funkcyjnej dla dużego n jest niepoprawny")

    def testIterator(self):
        self.assertEqual(doskonale_iter(10000), [6, 28, 496, 8128],
                         "Wynik wersji z iteratorem dla dużego n jest niepoprawny")


if __name__ == "__main__":
    unittest.main()


# profilowanie -> python -m profile _.py
