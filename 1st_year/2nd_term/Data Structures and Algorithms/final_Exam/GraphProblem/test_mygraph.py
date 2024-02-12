import unittest
import graphproblem as gp
import copy

class Test_MyGraph(unittest.TestCase):
    mark = 0

    def setUp(self):
        vertices = ['A', 'B', 'C', 'D', 'E']
        self.g = gp.MyGraph(vertices)
        self.g.add_edge('A', 'B')
        self.g.add_edge('A', 'C')
        self.g.add_edge('B', 'C')
        self.g.add_edge('A', 'D')
        self.g.add_edge('D', 'E')
        # print(self.g)

        # Draw the graph (we have removed the edge (A, D)).
        self.nonconnected = gp.MyGraph(vertices)
        self.nonconnected.add_edge('A', 'B')
        self.nonconnected.add_edge('A', 'C')
        self.nonconnected.add_edge('B', 'C')
        self.nonconnected.add_edge('D', 'E')
        # print(self.nonconnected)

        vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        self.g3 = gp.MyGraph(vertices)
        self.g3.add_edge('A', 'B')
        self.g3.add_edge('B', 'C')
        self.g3.add_edge('C', 'D')
        self.g3.add_edge('C', 'E')
        self.g3.add_edge('D', 'E')
        self.g3.add_edge('D', 'F')
        self.g3.add_edge('D', 'G')
        self.g3.add_edge('E', 'F')

        # print(self.g3)

    def test1(self):
        """ is_connected """
        print("\n test1: is_connected: True")
        print(self.g)

        actual = self.g.is_connected()
        print('actual = ', actual)
        print('expected = True')
        self.assertIsNotNone(actual)

        self.assertTrue(actual)
        Test_MyGraph.mark += 2

    def test2(self):
        """ is_connected: False"""
        print("\n test2: is_connected: False")
        print(self.nonconnected)

        actual = self.nonconnected.is_connected()
        print('actual = ', actual)
        print('expected = False')
        self.assertIsNotNone(actual)

        self.assertFalse(actual)
        Test_MyGraph.mark += 2

    def test3(self):
        """ is_bridge: True"""
        print("\n test3: is_bridge: True")
        # we do a copy of the graph self.g3 (it is a different object)
        input_g3 = copy.deepcopy(self.g3)
        # print(self.g3)
        actual = self.g3.is_bridge('A', 'B')
        print('actual = ', actual)
        print('expected = True')
        self.assertIsNotNone(actual)

        self.assertTrue(actual)
        # self.g3 must be equal to the original
        self.assertEqual(self.g3, input_g3)
        Test_MyGraph.mark += 2

    def test4(self):
        """ is_bridge: True"""
        print("\n test4: is_bridge: True")
        input_g3 = copy.deepcopy(self.g3)
        # print(self.g3)

        actual = self.g3.is_bridge('B', 'A')
        print('actual = ', actual)
        print('expected = True')
        self.assertTrue(actual)
        self.assertIsNotNone(actual)

        # self.g3 must be equal to the original
        self.assertEqual(self.g3, input_g3)
        Test_MyGraph.mark += 1

    def test5(self):
        """ is_bridge: True"""
        print("\n test5: is_bridge: True")
        input_g3 = copy.deepcopy(self.g3)
        # print(self.g3)

        actual = self.g3.is_bridge('B', 'C')
        print('actual = ', actual)
        print('expected = True')
        self.assertIsNotNone(actual)

        self.assertTrue(actual)
        # self.g3 must be equal to the original
        self.assertEqual(self.g3, input_g3)
        Test_MyGraph.mark += 2

    def test6(self):
        """ is_bridge: True"""
        print("\n test6: is_bridge: True")
        input_g3 = copy.deepcopy(self.g3)
        # print(self.g3)

        actual = self.g3.is_bridge('C', 'B')
        print('actual = ', actual)
        print('expected = True')
        self.assertIsNotNone(actual)

        self.assertTrue(actual)
        # self.g3 must be equal to the original
        self.assertEqual(self.g3, input_g3)
        Test_MyGraph.mark += 1

    def test7(self):
        """ is_bridge: True"""
        print("\n test7: is_bridge: True")
        input_g3 = copy.deepcopy(self.g3)
        # print(self.g3)

        actual = self.g3.is_bridge('D', 'G')
        print('actual = ', actual)
        print('expected = True')
        self.assertIsNotNone(actual)
        self.assertTrue(actual)
        # self.g3 must be equal to the original
        self.assertEqual(self.g3, input_g3)
        Test_MyGraph.mark += 2

    def test8(self):
        """ is_bridge: True"""
        print("\n test8: is_bridge: True")
        input_g3 = copy.deepcopy(self.g3)
        # print(self.g3)

        actual = self.g3.is_bridge('G', 'D')
        print('actual = ', actual)
        print('expected = True')
        self.assertIsNotNone(actual)
        self.assertTrue(actual)
        # self.g3 must be equal to the original
        self.assertEqual(self.g3, input_g3)
        Test_MyGraph.mark += 1

    def test9(self):
        """ is_bridge: False"""
        print("\n test9: is_bridge: False (edge no exist)")
        input_g3 = copy.deepcopy(self.g3)
        # print(self.g3)
        # the edge (does not exist)
        actual = self.g3.is_bridge('A', 'C')
        print('actual = ', actual)
        print('expected = False')
        self.assertIsNotNone(actual)
        self.assertFalse(actual)
        # self.g3 must be equal to the original
        self.assertEqual(self.g3, input_g3)
        Test_MyGraph.mark += 1

    def test_10(self):
        """ is_bridge: False"""
        print("\n test_10: is_bridge: False")
        input_g3 = copy.deepcopy(self.g3)
        # print(self.g3)

        actual = self.g3.is_bridge('C', 'D')
        print('actual = ', actual)
        print('expected = False')
        self.assertIsNotNone(actual)
        self.assertFalse(actual)
        # self.g3 must be equal to the original
        self.assertEqual(self.g3, input_g3)
        Test_MyGraph.mark += 1

    def test_11(self):
        """ is_bridge: False"""
        print("\n test_10: is_bridge: False")
        input_g3 = copy.deepcopy(self.g3)
        # print(self.g3)

        actual = self.g3.is_bridge('C', 'E')
        print('actual = ', actual)
        print('expected = False')
        self.assertIsNotNone(actual)
        self.assertFalse(actual)
        # self.g3 must be equal to the original
        self.assertEqual(self.g3, input_g3)
        Test_MyGraph.mark += 1

    def test_12(self):
        """ is_bridge: False"""
        print("\n test_12: is_bridge: False")
        input_g3 = copy.deepcopy(self.g3)
        # print(self.g3)

        actual = self.g3.is_bridge('D', 'E')
        print('actual = ', actual)
        print('expected = False')
        self.assertIsNotNone(actual)
        self.assertFalse(actual)
        # self.g3 must be equal to the original
        self.assertEqual(self.g3, input_g3)
        Test_MyGraph.mark += 1

    def test_13(self):
        """ is_bridge: False"""
        print("\n test_13: is_bridge: False")
        input_g3 = copy.deepcopy(self.g3)
        # print(self.g3)

        actual = self.g3.is_bridge('D', 'F')
        print('actual = ', actual)
        print('expected = False')
        self.assertIsNotNone(actual)
        self.assertFalse(actual)
        # self.g3 must be equal to the original
        self.assertEqual(self.g3, input_g3)
        Test_MyGraph.mark += 1

    def test_14(self):
        """ is_bridge: False"""
        print("\n test_14: is_bridge: False")
        input_g3 = copy.deepcopy(self.g3)
        # print(self.g3)

        actual = self.g3.is_bridge('E', 'F')
        print('actual = ', actual)
        print('expected = False')
        self.assertIsNotNone(actual)
        self.assertFalse(actual)
        # self.g3 must be equal to the original
        self.assertEqual(self.g3, input_g3)
        Test_MyGraph.mark += 1

    def test_15(self):
        """ is_bridge: False"""
        print("\n test_15: is_bridge: False")
        input_g3 = copy.deepcopy(self.g3)
        # print(self.g3)

        actual = self.g3.is_bridge('F', 'E')
        print('actual = ', actual)
        print('expected = False')
        self.assertIsNotNone(actual)
        self.assertFalse(actual)
        # self.g3 must be equal to the original
        self.assertEqual(self.g3, input_g3)
        Test_MyGraph.mark += 1

    def test_z(self):
        print('\n\n\nNota provisional: ', Test_MyGraph.mark)


if __name__ == "__main__":
    unittest.main()
