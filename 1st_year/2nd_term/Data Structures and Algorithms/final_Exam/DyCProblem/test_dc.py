import unittest

import dcproblem as dc


class Test_DC(unittest.TestCase):
    mark = 0

    def setUp(self):
        self.a = [4, 1, 7, 4, 4, 8, 8, 3, 1, 2]
        self.b = [5, 7, 1, 6, 4, 8, 7, 4, 7, 3]

    def test1(self):
        """ x does not exist"""
        print("\n test1: x does not exist")
        x = 0
        actual = dc.find_first_last(self.a, x)
        expected = (-1, -1)
        print('actual = ', actual)
        print('expected = ', expected)
        self.assertEqual(actual, expected)
        Test_DC.mark += 1

    def test2(self):
        """ list empty"""
        print("\n test2: list is empty")
        x = 0
        actual = dc.find_first_last([], x)
        expected = (-1, -1)
        print('actual = ', actual)
        print('expected = ', expected)
        self.assertEqual(actual, expected)
        Test_DC.mark += 1

    def test3(self):
        """ x only has 1 occurrence"""
        print("\n test3: x only has 1 occurrence")
        x = 3
        actual = dc.find_first_last(self.a, x)
        expected = (self.a.index(x), len(self.a)-self.a[::-1].index(x)-1)
        print('actual = ', actual)
        print('expected = ', expected)
        self.assertEqual(actual, expected)
        Test_DC.mark += 2

    def test4(self):
        """ x only has 1 occurrence (at the end)"""
        print("\n test4: x only has 1 occurrence (at the end)")
        x = 2
        actual = dc.find_first_last(self.a, x)
        expected = (self.a.index(x), len(self.a)-self.a[::-1].index(x)-1)
        print('actual = ', actual)
        print('expected = ', expected)
        self.assertEqual(actual, expected)
        Test_DC.mark += 2

    def test4_a(self):
        """ x only has 1 occurrence (at the beginning)"""
        print("\n test4_a: x only has 1 occurrence (at the beginning)")
        x = 5
        actual = dc.find_first_last(self.b, x)
        expected = (self.b.index(x), len(self.b)-self.b[::-1].index(x)-1)
        print('actual = ', actual)
        print('expected = ', expected)
        self.assertEqual(actual, expected)
        Test_DC.mark += 2

    def test5(self):
        """ x has two occurrences"""
        print("\n test5: x has two occurrences")
        x = 1
        actual = dc.find_first_last(self.a, x)
        expected = (self.a.index(x), len(self.a)-self.a[::-1].index(x)-1)
        print('actual = ', actual)
        print('expected = ', expected)
        self.assertEqual(actual, expected)
        Test_DC.mark += 2

    def test6(self):
        """ x has two occurrences (no beginning)"""
        print("\n test6: x has two occurrences (no beginning)")
        x = 8
        actual = dc.find_first_last(self.a, x)
        expected = (self.a.index(x), len(self.a)-self.a[::-1].index(x)-1)
        print('actual = ', actual)
        print('expected = ', expected)
        self.assertEqual(actual, expected)
        Test_DC.mark += 2

    def test6_a(self):
        """ x has two occurrences"""
        print("\n test6: x has two occurrences, (3)")
        x = 4
        actual = dc.find_first_last(self.b, x)
        expected = (self.b.index(x), len(self.b)-self.b[::-1].index(x)-1)
        print('actual = ', actual)
        print('expected = ', expected)
        self.assertEqual(actual, expected)
        Test_DC.mark += 2

    def test7(self):
        """ x has more than two occurrences"""
        print("\n test7: x has more than two occurrences")
        x = 4
        actual = dc.find_first_last(self.a, x)
        expected = (self.a.index(x), len(self.a)-self.a[::-1].index(x)-1)
        print('actual = ', actual)
        print('expected = ', expected)
        self.assertEqual(actual, expected)
        Test_DC.mark += 3

    def test8(self):
        """ x has more than two occurrences"""
        print("\n test8: x has more than two occurrences")
        x = 7
        actual = dc.find_first_last(self.b, x)
        expected = (self.b.index(x), len(self.b)-self.b[::-1].index(x)-1)
        print('actual = ', actual)
        print('expected = ', expected)
        self.assertEqual(actual, expected)
        Test_DC.mark += 3

    def test_z(self):
        print('Nota provisional: ', Test_DC.mark)

if __name__ == "__main__":
    unittest.main()
