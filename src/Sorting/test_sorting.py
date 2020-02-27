from unittest import TestCase, skipIf
from random import randint

import time

from src.Sorting.bubble_sort import bubble_sort
from src.Sorting.selection_sort import selection_sort
from src.Sorting.insertion_sort import insertion_sort

SMALL = 16
LARGE = 1 << 10

DEBUG = 0

class TestSorting(TestCase):
    CASES = []
    total_time = 0.0
    def setUp(self):
        print("-"*16, "preparing ...", end="\t")
        arr1 = [randint(0, 1) % 2 for _ in range(SMALL)]
        arr1_ans = list(sorted(arr1))
        self.CASES.append(
            ("repeated", arr1, arr1_ans),
        )
        arr2 = [x for x in range(SMALL)]
        self.CASES.append(
            ("sorted", arr2, arr2)
        )
        arr3 = [randint(0, 100000)  for _ in range(SMALL)]
        arr3_ans = list(sorted(arr3))
        self.CASES.append(
            ("random", arr3, arr3_ans)
        )
        self.CASES.append(
            ("empty", [],[])
        )
        arr4 = [randint(0, 1000000007) for _ in range(LARGE)]
        arr4_ans = list(sorted(arr4))
        self.CASES.append(
            ("big-size", arr4, arr4_ans)
        )
        arr5 = [1, 0]
        arr5_ans = [0, 1]
        self.CASES.append(
            ("short", arr5, arr5_ans)
        )
        print("done")

    def tearDown(self):
        print("\ttotal: {:.3f}ms".format(self.total_time))
        self.total_time = 0.0
        self.CASES.clear()

    def sorting_algo(self, descrip:str, algo, reverse=False):
        print(descrip)
        self.total_time = 0.0
        for label, inp, ans in self.CASES:
            print(f"\ttest {label}", end=" -- ")
            inp_co, ans_co = inp.copy(), ans.copy()
            if reverse:
                ans_co.reverse()
            st = time.perf_counter()
            algo(inp_co, reverse)
            delta = (time.perf_counter() - st) * 1000

            assert inp_co == ans_co, "sorted:{}\nans:{}".format(inp_co, ans_co)
            print("done -- {:.3f}ms".format(delta))
            self.total_time += delta

    @skipIf(DEBUG > 0, "")
    def test_bubble_sort_ascending(self):
        self.sorting_algo(descrip="Bubble sort ascending", algo=bubble_sort, reverse=False)

    @skipIf(DEBUG > 0, "")
    def test_bubble_sort_descending(self):
        self.sorting_algo(descrip="Bubble sort descending", algo=bubble_sort, reverse=True)

    @skipIf(DEBUG > 0, "")
    def test_selection_sort_ascending(self):
        self.sorting_algo(descrip="Selection sort ascending", algo=selection_sort, reverse=False)

    @skipIf(DEBUG > 0, "")
    def test_selection_sort_descending(self):
        self.sorting_algo(descrip="Selection sort descending", algo=selection_sort, reverse=True)

    #@skipIf(DEBUG > 0, "")
    def test_insertion_sort_ascending(self):
        self.sorting_algo(descrip="Insertion sort ascending", algo=insertion_sort, reverse=False)

    #@skipIf(DEBUG > 0, "")
    def test_insertion_sort_descending(self):
        self.sorting_algo(descrip="Insertion sort descending", algo=insertion_sort, reverse=True)












