import unittest # package that contains the classes t

from MidTermExam87_2 import MyBST

class Test(unittest.TestCase):
   
    mark = 0

    def setUp(self) -> None:
        self.tree1 = MyBST()
        self.data = [46, 11, 81, 51, 56, 94, 5, 20,49]
        for x in self.data:
            self.tree1.add(x)
        #self.tree1.draw()
        
        self.tree2 = MyBST()
        self.data = [46, 11, 81, 51, 94, 5, 20]
        for x in self.data:
            self.tree2.add(x)
        #self.tree2.draw()
        
        self.tree3 = MyBST()
        self.data = [46, 81, 51, 94]
        for x in self.data:
            self.tree3.add(x)
        #self.tree3.draw()
        print()
        
                
    def test1(self) -> None:
        print("test1: empty tree")
        input_tree = MyBST()
        expected = True
        result = input_tree.isFullBinary()
        self.assertEqual(result, expected)

        Test.mark += 1

    def test2(self) -> None:
        print("test2: tree with 1 element")
        input_tree = MyBST()
        input_tree.add(20)
        expected = True
        result = input_tree.isFullBinary()
        self.assertEqual(result, expected)

        Test.mark += 1
    
    def test3(self) -> None:
        print("test2: tree with 2 elements")
        input_tree = MyBST()
        input_tree.add(20)
        input_tree.add(30)
        expected = False
        result = input_tree.isFullBinary()
        self.assertEqual(result, expected)

        Test.mark += 1
        
    def test4(self) -> None:
        print("test4: tree 1 full binary")
        self.tree1.draw()
        expected = True
        result = self.tree1.isFullBinary()
        self.assertEqual(result, expected)
        
        Test.mark += 2
        
                
    def test5(self) -> None:
        print("test5: tree 2 full binary")
        self.tree2.draw()
        expected = True
        result = self.tree2.isFullBinary()
        self.assertEqual(result, expected)
        
        Test.mark += 2


    def test6(self) -> None:
        print("\ntest6: tree 3 not full binary")
        self.tree3.draw()
        expected = False
        result = self.tree3.isFullBinary()
        self.assertEqual(result, expected)

        Test.mark += 1
        
    def test7(self) -> None:
        print("\ntest7: tree not full binary")
        expected = False
        self.tree1.remove(49)
        self.tree1.draw()
        result = self.tree1.isFullBinary()
        self.assertEqual(result, expected)

        Test.mark +=1
 
    def test8(self) -> None:
        print("\ntest7: tree not full binary")
        expected = False
        self.tree2.remove(5)
        self.tree2.draw()
        result = self.tree2.isFullBinary()
        self.assertEqual(result, expected)

        Test.mark += 1


    def test_z(self):
        print("Provisional mark:", Test.mark)


if __name__ == "__main__":
    unittest.main()