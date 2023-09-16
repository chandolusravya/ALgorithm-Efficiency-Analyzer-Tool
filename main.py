import math
import random
import sys
import time

from PyQt5.QtWidgets import QApplication
from matplotlib import pyplot as plt

from gui import SortingApp


#  utils functions
def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        logger(f"Time taken by {func.__name__}: {time.perf_counter() - start}")
        return result

    return wrapper


def is_valid_input(text):
    text = text.replace(',', ' ')
    if not text:
        return False
    if '.' in text:
        gui.get_checkboxes()[6].setChecked(False)
        gui.get_checkboxes()[7].setChecked(False)
        logger('Radix Sort and Counting Sort only work with integers')
        logger('Removed Radix Sort and Counting Sort from selected algorithms')

    def is_valid_number(s):
        try:
            float(s) if '.' in s else int(s)
            return True
        except ValueError:
            return False

    return all(map(is_valid_number, text.split()))


def parse_input(text):
    text = text.replace(',', ' ')

    def parse_number(s):
        return float(s) if '.' in s else int(s)

    return list(map(parse_number, text.split()))


def measure_efficiency(sorting_algorithm, input_array):
    sorted_array, execution_time = sorting_algorithm.sort(input_array.copy())
    return sorted_array, execution_time


# static Functions
def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


def merge(array, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * n1
    R = [0] * n2

    for i in range(n1):
        L[i] = array[l + i]
    for j in range(n2):
        R[j] = array[m + 1 + j]

    i = j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        array[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        array[k] = R[j]
        j += 1
        k += 1


def partition(array, low, high):
    i = low - 1
    pivot = array[high]

    for j in range(low, high):
        if array[j] < pivot:
            i += 1
            swap(i, j, array)
    swap(i + 1, high, array)
    return i + 1


# Algorithms

class SortingAlgorithm:

    def swap(self, i, j, array):
        swap(i, j, array)

    def sort(self, array):
        pass


class InsertionSort(SortingAlgorithm):
    def sort(self, array):
        start_time = time.perf_counter()
        for i in range(1, len(array)):
            j = i
            while j > 0 and array[j] < array[j - 1]:
                self.swap(j, j - 1, array)
                j -= 1
        end_time = time.perf_counter()
        return array, end_time - start_time


class BubbleSort(SortingAlgorithm):
    def sort(self, array):
        start_time = time.perf_counter()
        isSorted = False
        counter = 0
        while not isSorted:
            isSorted = True
            for i in range(len(array) - 1 - counter):
                if array[i] > array[i + 1]:
                    self.swap(i, i + 1, array)
                    isSorted = False
            counter += 1
        end_time = time.perf_counter()
        return array, end_time - start_time


class QuickSort(SortingAlgorithm):
    def sort(self, array):
        start_time = time.perf_counter()
        self.quickSortHelper(array, 0, len(array) - 1)
        end_time = time.perf_counter()
        return array, end_time - start_time

    def quickSortHelper(self, array, startIdx, endIdx):
        if startIdx >= endIdx:
            return
        pivotIdx = startIdx
        leftIdx = startIdx + 1
        rightIdx = endIdx
        while rightIdx >= leftIdx:
            if array[leftIdx] > array[pivotIdx] and array[rightIdx] < array[pivotIdx]:
                self.swap(leftIdx, rightIdx, array)
            if array[leftIdx] <= array[pivotIdx]:
                leftIdx += 1
            if array[rightIdx] >= array[pivotIdx]:
                rightIdx -= 1
        self.swap(pivotIdx, rightIdx, array)
        leftSubarraySmaller = rightIdx - 1 - startIdx < endIdx - (rightIdx + 1)
        if leftSubarraySmaller:
            self.quickSortHelper(array, startIdx, rightIdx - 1)
            self.quickSortHelper(array, rightIdx + 1, endIdx)
        else:
            self.quickSortHelper(array, rightIdx + 1, endIdx)
            self.quickSortHelper(array, startIdx, rightIdx - 1)


class MergeSort(SortingAlgorithm):
    def sort(self, array):
        start_time = time.perf_counter()
        if len(array) <= 1:
            return array, 0.0
        auxiliaryArray = array[:]
        self.mergeSortHelper(array, 0, len(array) - 1, auxiliaryArray)
        end_time = time.perf_counter()
        return array, end_time - start_time

    def mergeSortHelper(self, mainArray, startIdx, endIdx, auxiliaryArray):
        if startIdx == endIdx:
            return
        middleIdx = (startIdx + endIdx) // 2
        self.mergeSortHelper(auxiliaryArray, startIdx, middleIdx, mainArray)
        self.mergeSortHelper(auxiliaryArray, middleIdx + 1, endIdx, mainArray)
        self.doMerge(mainArray, startIdx, middleIdx, endIdx, auxiliaryArray)

    def doMerge(self, mainArray, startIdx, middleIdx, endIdx, auxiliaryArray):
        k = startIdx
        i = startIdx
        j = middleIdx + 1
        while i <= middleIdx and j <= endIdx:
            if auxiliaryArray[i] <= auxiliaryArray[j]:
                mainArray[k] = auxiliaryArray[i]
                i += 1
            else:
                mainArray[k] = auxiliaryArray[j]
                j += 1
            k += 1
        while i <= middleIdx:
            mainArray[k] = auxiliaryArray[i]
            i += 1
            k += 1
        while j <= endIdx:
            mainArray[k] = auxiliaryArray[j]
            j += 1
            k += 1


class CountingSort(SortingAlgorithm):
    def sort(self, array):
        start_time = time.perf_counter()
        max_value = max(array)
        min_value = min(array)
        range_of_elements = max_value - min_value + 1
        count_array = [0] * range_of_elements
        output_array = [0] * len(array)

        for num in array:
            count_array[num - min_value] += 1

        for i in range(1, len(count_array)):
            count_array[i] += count_array[i - 1]

        for i in range(len(array) - 1, -1, -1):
            output_array[count_array[array[i] - min_value] - 1] = array[i]
            count_array[array[i] - min_value] -= 1

        for i in range(len(array)):
            array[i] = output_array[i]

        end_time = time.perf_counter()
        return array, end_time - start_time


class HeapSort(SortingAlgorithm):
    def sort(self, array):
        start_time = time.perf_counter()
        self.build_max_heap(array)
        for i in range(len(array) - 1, 0, -1):
            self.swap(0, i, array)
            self.max_heap(array, index=0, size=i)
        end_time = time.perf_counter()
        return array, end_time - start_time

    def build_max_heap(self, array):
        n = len(array)
        for i in range(n // 2 - 1, -1, -1):
            self.max_heap(array, index=i, size=n)

    def max_heap(self, array, index, size):
        largest = index
        leftNumber = 2 * index + 1
        rightNumber = 2 * index + 2
        if leftNumber < size and array[leftNumber] > array[largest]:
            largest = leftNumber
        if rightNumber < size and array[rightNumber] > array[largest]:
            largest = rightNumber
        if largest != index:
            self.swap(index, largest, array)
            self.max_heap(array, largest, size)

    def heap_sort(self, array):
        return self.sort(array)


class SelectionSort(SortingAlgorithm):
    def find_min_index(self, array, start):
        min_index = start
        for j in range(start + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        return min_index

    def sort(self, array):
        start_time = time.perf_counter()
        for i in range(len(array)):
            min_index = self.find_min_index(array, i)
            self.swap(i, min_index, array)
        end_time = time.perf_counter()
        return array, end_time - start_time


class RadixSort(SortingAlgorithm):
    def sort(self, array):
        start_time = time.perf_counter()
        max_value = max(array, key=abs)
        num_digits = int(math.log10(abs(max_value))) + 1 if max_value != 0 else 1

        for digit_place in range(num_digits):
            counting_sort = CountingSort()
            sorted_array, _ = counting_sort.sort(array)
            array = sorted_array

        end_time = time.perf_counter()
        return array, end_time - start_time


all_algorithms = [
    {
        "id": 0,
        "name": "Bubble Sort",
        "instance": BubbleSort(),
        "description": "Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.",
        "time_complexity": "O(n^2)",
        "space_complexity": "O(1)"
    },
    {
        "id": 1,
        "name": "Selection Sort",
        "instance": SelectionSort(),
        "description": "The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning.",
        "time_complexity": "O(n^2)",
        "space_complexity": "O(1)"
    },
    {
        "id": 2,
        "name": "Insertion Sort",
        "instance": InsertionSort(),
        "description": "Insertion sort is a simple sorting algorithm that works similar to the way you sort playing cards in your hands.",
        "time_complexity": "O(n^2)",
        "space_complexity": "O(1)"
    },
    {
        "id": 3,
        "name": "Merge Sort",
        "instance": MergeSort(),
        "description": "Merge Sort is a Divide and Conquer algorithm. It divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves.",
        "time_complexity": "O(nlogn)",
        "space_complexity": "O(n)"
    },
    {
        "id": 4,
        "name": "Quick Sort",
        "instance": QuickSort(),
        "description": "QuickSort is a Divide and Conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot.",
        "time_complexity": "O(nlogn)",
        "space_complexity": "O(1)"
    },
    {
        "id": 5,
        "name": "Heap Sort",
        "instance": HeapSort(),
        "description": "Heap sort is a comparison based sorting technique based on Binary Heap data structure. It is similar to selection sort where we first find the maximum element and place the maximum element at the end.",
        "time_complexity": "O(nlogn)",
        "space_complexity": "O(1)"
    },
    {
        "id": 6,
        "name": "Radix Sort",
        "instance": RadixSort(),
        "description": "Radix sort is a sorting technique that sorts the elements by first grouping the individual digits of the same place value. Then, sort the elements according to their increasing/decreasing order.",
        "time_complexity": "O(nk)",
        "space_complexity": "O(n+k)"
    },
    {
        "id": 7,
        "name": "Counting Sort",
        "instance": CountingSort(),
        "description": "Counting sort is a sorting technique based on keys between a specific range. It works by counting the number of objects having distinct key values.",
        "time_complexity": "O(n+k)",
        "space_complexity": "O(n+k)"
    }
]


#  Visualizations Utils

def show_visualization(labels, data):
    # Create a figure with two subplots
    fig, (plt1, plt2) = plt.subplots(1, 2, figsize=(15, 8))

    # Plot the line chart on the first subplot (plt1)
    plt1.plot(labels, data, marker='o', linestyle='-')
    plt1.set_ylabel('Time in Seconds')
    plt1.set_xticks(labels)
    plt1.set_xticklabels(labels, rotation=45, ha='right')
    plt1.set_title('Efficiency of Algorithms')

    # Plot the bar graph on the second subplot (plt2)
    plt2.bar(labels, data, color="maroon")
    plt2.set_ylabel('Time in Seconds')
    plt2.set_xticks(labels)  # Ensure all labels are shown
    plt2.set_xticklabels(labels, rotation=45, ha='right')
    plt2.set_title('Efficiency of Algorithms (Bar Graph)')

    # Customize the appearance as needed
    plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
    plt.tight_layout()  # Ensure labels are not cut off
    for x, y in zip(labels, data):
        plt1.annotate(f'{y:6f}', (x, y), textcoords="offset points", xytext=(0, 10), ha='center')
    # Add labels to each bar
    for x, y in zip(labels, data):
        plt2.annotate(f'{y:6f}', (x, y), textcoords="offset points", xytext=(0, 10), ha='center')

    # Show the plots
    plt.show()
    return 0


def analyze_visualization(input_array, contains_float=False):
    algos = all_algorithms
    if contains_float:
        algos = all_algorithms[:-2]
    labels = list(map(lambda algo: algo['name'], algos))
    efficiency_list = []
    for selected_algorithm in algos:
        output, efficiency = measure_efficiency(selected_algorithm['instance'], input_array)
        efficiency_list.append(efficiency)

    data = [float(val) for val in efficiency_list]
    show_visualization(labels, data)


def run_callback(args):
    text = gui.get_input_text()
    if not is_valid_input(gui.get_input_text()):
        logger("Please enter valid input")
        return

    nums = parse_input(text)
    labels = []
    data = []
    for id, checkbox in gui.get_checkboxes().items():
        if checkbox.isChecked():
            # find the algorithm from id
            sorted_elements, efficiency = all_algorithms[id]['instance'].sort(nums)
            logger(f"--------------------{id}----------------------------")
            logger("Algorithm: " + all_algorithms[id]['name'])
            logger(f"Sorted Elements: {sorted_elements}")
            logger(f"Time Taken: {efficiency}")
            logger("------------------------------------------------------")
            labels.append(all_algorithms[id]['name'])
            data.append(efficiency)
    if len(labels) != 0:
        show_visualization(labels, data)
    # combined_visualization(labels, data)


def analyze_callback(args):
    text = gui.get_input_text()
    if not is_valid_input(gui.get_input_text()):
        logger("Please enter valid input")
        return
    nums = parse_input(text)
    analyze_visualization(nums, contains_float='.' in text)


def show_stats_callback(args):
    for algo in all_algorithms:
        logger(f"--------------------{algo['id']}----------------------------")
        logger("Algorithm: " + algo['name'])
        logger("Description: " + algo['description'])
        logger("Time Complexity: " + algo['time_complexity'])
        logger("Space Complexity: " + algo['space_complexity'])
        logger("--------------------------------------------------")


def random_button_clicked(args):
    random_elements = [random.randint(0, 100) for _ in range(random.randint(10, 25))]
    text = ','.join(map(str, random_elements))
    gui.update_text_box(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = SortingApp()
    logger = gui.log_message
    logger('Welcome to Sorting Algorithms Efficiency Analyzer Tool')
    logger(
        'Please enter a list of numbers to sort, and analyze their efficiency. ( Comma Separated or Space Separated )')
    logger('Select the algorithms you want to run, and click on Run Selected Algorithms button')
    logger('Click on All Algorithms Efficiency button to see the efficiency of all algorithms')
    logger('Click on Show Stats button to see the stats of all algorithms')
    gui.on_run_button_clicked(run_callback)
    gui.on_analyze_button_clicked(analyze_callback)
    gui.on_show_stats_button_clicked(show_stats_callback)
    gui.on_random_button_clicked(random_button_clicked)
    sys.exit(app.exec_())
    # App End
