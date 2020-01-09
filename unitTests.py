import unittest
import sorting

class TestInsertionSorting(unittest.TestCase):
    # this setUp method will be called automatically by the framework for each single test
    def setUp(self):
        self.nums = [4, 2, 6, 1, 5, 3]
        self.expected = [1, 2, 3, 4, 5, 6]

    def test_emptyList(self):
        emptyList = []
        sorting.insertion(emptyList)
        self.assertEqual(len(emptyList), 0)

    def test_normalList(self):
        sorting.insertion(self.nums)
        self.assertEqual(self.nums, self.expected)

class TestBubbleSorting(unittest.TestCase):
    # this setUp method will be called automatically by the framework for each single test
    def setUp(self):
        self.nums = [4, 2, 6, 1, 5, 3]
        self.expected = [1, 2, 3, 4, 5, 6]

    def test_emptyList(self):
        emptyList = []
        sorting.insertion(emptyList)
        self.assertEqual(len(emptyList), 0)

    def test_normalList(self):
        sorting.bubble(self.nums)
        self.assertEqual(self.nums, self.expected)

class TestHeapSorting(unittest.TestCase):
    # this setUp method will be called automatically by the framework for each single test
    def setUp(self):
        self.nums = [4, 2, 6, 1, 5, 3]
        self.expected = [1, 2, 3, 4, 5, 6]
    
    def test_heapify(self):
        sorting.max_heapify(self.nums, len(self.nums), 0)
        self.assertEqual(self.nums, [6, 2, 4, 1, 5, 3])
    
    def test_construct_heap(self):
        sorting.constuct_heap(self.nums)
        self.assertEqual(self.nums, [6, 5, 4, 1, 2, 3])    

    def test_empty_list(self):
        empty_list = []
        sorting.heap_sort(empty_list)
        self.assertEqual(len(empty_list), 0)

    def test_normalList(self):
        sorting.heap_sort(self.nums)
        self.assertEqual(self.nums, self.expected)

if __name__ == '__main__':
    unittest.main()