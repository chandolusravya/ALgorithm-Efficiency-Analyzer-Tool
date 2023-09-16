# Performing unit testing for sorting algorithms

import random
import unittest

from main import BubbleSort, InsertionSort, SelectionSort, MergeSort, QuickSort, HeapSort


class TestSortingAlgorithms(unittest.TestCase):

    def setUp(self):
        self.test_list = [random.randint(0, 100) for i in range(10)]
        self.sorted_list = sorted(self.test_list)
        self.reverse_list = sorted(self.test_list, reverse=True)
        self.empty_list = []
        self.one_element_list = [1]
        self.two_element_list = [1, 2]

    def test_bubble_sort(self):
        self.assertEqual(BubbleSort().sort(self.test_list)[0], self.sorted_list)
        self.assertEqual(BubbleSort().sort(self.reverse_list)[0], self.sorted_list)
        self.assertEqual(BubbleSort().sort(self.empty_list)[0], self.empty_list)
        self.assertEqual(BubbleSort().sort(self.one_element_list)[0], self.one_element_list)
        self.assertEqual(BubbleSort().sort(self.two_element_list)[0], self.two_element_list)

    def test_insertion_sort(self):
        self.assertEqual(InsertionSort().sort(self.test_list)[0], self.sorted_list)
        self.assertEqual(InsertionSort().sort(self.reverse_list)[0], self.sorted_list)
        self.assertEqual(InsertionSort().sort(self.empty_list)[0], self.empty_list)
        self.assertEqual(InsertionSort().sort(self.one_element_list)[0], self.one_element_list)
        self.assertEqual(InsertionSort().sort(self.two_element_list)[0], self.two_element_list)

    def test_selection_sort(self):
        self.assertEqual(SelectionSort().sort(self.test_list)[0], self.sorted_list)
        self.assertEqual(SelectionSort().sort(self.reverse_list)[0], self.sorted_list)
        self.assertEqual(SelectionSort().sort(self.empty_list)[0], self.empty_list)
        self.assertEqual(SelectionSort().sort(self.one_element_list)[0], self.one_element_list)
        self.assertEqual(SelectionSort().sort(self.two_element_list)[0], self.two_element_list)

    def test_merge_sort(self):
        self.assertEqual(MergeSort().sort(self.test_list)[0], self.sorted_list)
        self.assertEqual(MergeSort().sort(self.reverse_list)[0], self.sorted_list)
        self.assertEqual(MergeSort().sort(self.empty_list)[0], self.empty_list)
        self.assertEqual(MergeSort().sort(self.one_element_list)[0], self.one_element_list)
        self.assertEqual(MergeSort().sort(self.two_element_list)[0], self.two_element_list)

    def test_quick_sort(self):
        self.assertEqual(QuickSort().sort(self.test_list)[0], self.sorted_list)
        self.assertEqual(QuickSort().sort(self.reverse_list)[0], self.sorted_list)
        self.assertEqual(QuickSort().sort(self.empty_list)[0], self.empty_list)
        self.assertEqual(QuickSort().sort(self.one_element_list)[0], self.one_element_list)
        self.assertEqual(QuickSort().sort(self.two_element_list)[0], self.two_element_list)

    def test_heap_sort(self):
        self.assertEqual(HeapSort().sort(self.test_list)[0], self.sorted_list)
        self.assertEqual(HeapSort().sort(self.reverse_list)[0], self.sorted_list)
        self.assertEqual(HeapSort().sort(self.empty_list)[0], self.empty_list)
        self.assertEqual(HeapSort().sort(self.one_element_list)[0], self.one_element_list)
        self.assertEqual(HeapSort().sort(self.two_element_list)[0], self.two_element_list)


# Test that it can algorithm can sort all the positive numbers
class PositiveNumSortData(unittest.TestCase):
    # testing for INSERTION sort
    def test_list_int(self):
        data = [10, 89, 45, 34, 90, 0, 4]
        result = InsertionSort().sort(data)[0]
        data.sort()
        self.assertEqual(result, data)

    # testing for BUBBLE sort
    def test_list_int(self):
        data = [10, 89, 45, 34, 90, 0, 4]
        result = BubbleSort().sort(data)[0]
        data.sort()
        self.assertEqual(result, data)

    # testing for QUICKSORT
    def test_list_int(self):
        data = [10, 89, 45, 34, 90, 0, 4]
        result = QuickSort().sort(data)[0]
        data.sort()
        self.assertEqual(result, data)

    # testing for MERGE sort
    def test_list_int(self):
        data = [10, 89, 45, 34, 90, 0, 4]
        result = MergeSort().sort(data)[0]
        data.sort()
        self.assertEqual(result, data)


# Test if algorithm can sort all big numbers
class LargeNumSortData(unittest.TestCase):
    # testing for INSERTION sort
    def test_list_int(self):
        data = [101, 6545, 231, 2313, 564, 100, 986521, 789]
        result = InsertionSort().sort(data)[0]
        data.sort()
        self.assertEqual(result, data)

    # testing for BUBBLE sort
    def test_list_int(self):
        data = [101, 6545, 231, 2313, 564, 100, 986521, 789]
        result = BubbleSort().sort(data)[0]
        data.sort()
        self.assertEqual(result, data)

    # testing for QUICKSORT
    def test_list_int(self):
        data = [101, 6545, 231, 2313, 564, 100, 986521, 789]
        result = QuickSort().sort(data)[0]
        data.sort()
        self.assertEqual(result, data)

    # testing for MERGE sort
    def test_list_int(self):
        data = [101, 6545, 231, 2313, 564, 100, 986521, 789]
        result = MergeSort().sort(data)[0]
        data.sort()
        self.assertEqual(result, data)


# Test if algorithm can sort floating numbers
class FloatNumSortData(unittest.TestCase):
    # testing for INSERTION sort
    def test_list_int(self):
        data = [10.6, 1.2, 7.8, 3.4, 0.03, 2.3, 9.5, 7.8]
        result = InsertionSort().sort(data)[0]
        data.sort()
        self.assertEqual(result, data)

    # testing for BUBBLE sort
    def test_list_int(self):
        data = [10.6, 1.2, 7.8, 3.4, 0.03, 2.3, 9.5, 7.8]
        result = BubbleSort().sort(data)[0]
        data.sort()
        self.assertEqual(result, data)

    # testing for QUICKSORT
    def test_list_int(self):
        data = [10.6, 1.2, 7.8, 3.4, 0.03, 2.3, 9.5, 7.8]
        result = QuickSort().sort(data)[0]
        data.sort()
        self.assertEqual(result, data)

    # testing for MERGE sort
    def test_list_int(self):
        data = [10.6, 1.2, 7.8, 3.4, 0.03, 2.3, 9.5, 7.8]
        result = MergeSort().sort(data)[0]
        data.sort()
        self.assertEqual(result, data)

        # Test if algorithm can sort floating numbers


# Test if algorithm can sort mixed (floating and int) numbers
class MixedNumSortData(unittest.TestCase):
    # testing for INSERTION sort
    def test_list_int(self):
        data = [2, 7.8, 10, 0.03, 2.3, 9.5, 7.8]
        result = InsertionSort().sort(data)[0]
        data.sort()
        self.assertEqual(result, data)

    # testing for BUBBLE sort
    def test_list_int(self):
        data = [2, 7.8, 10, 0.03, 2.3, 9.5, 7.8]
        result = BubbleSort().sort(data)[0]
        data.sort()
        self.assertEqual(result, data)

    # testing for QUICKSORT
    def test_list_int(self):
        data = [2, 7.8, 10, 0.03, 2.3, 9.5, 7.8]
        result = QuickSort().sort(data)[0]
        data.sort()
        self.assertEqual(result, data)

    # testing for MERGE sort
    def test_list_int(self):
        data = [2, 7.8, 10, 0.03, 2.3, 9.5, 7.8]
        result = MergeSort().sort(data)[0]
        data.sort()
        self.assertEqual(result, data)

    # Test if algorithm can sort negative numbers


class NegativeNumSortData(unittest.TestCase):
    # testing for INSERTION sort
    def test_list_int(self):
        data = [-1, 3, -6, 2, -2.3, 1, -9.3, -0.002]
        result = InsertionSort().sort(data)[0]
        data.sort()
        self.assertEqual(result, data)

    # testing for BUBBLE sort
    def test_list_int(self):
        data = [-1, 3, -6, 2, -2.3, 1, -9.3, -0.002]
        result = BubbleSort().sort(data)[0]
        data.sort()
        self.assertEqual(result, data)

    # testing for QUICKSORT
    def test_list_int(self):
        data = [-1, 3, -6, 2, -2.3, 1, -9.3, -0.002]
        result = QuickSort().sort(data)[0]
        data.sort()
        self.assertEqual(result, data)

    # testing for MERGE sort
    def test_list_int(self):
        data = [-1, 3, -6, 2, -2.3, 1, -9.3, -0.002]
        result = MergeSort().sort(data)[0]
        data.sort()
        self.assertEqual(result, data)


if __name__ == '__main__':
    unittest.main()
