from unittest import TestCase
from random import randint

from src.Sorting.bubble_sort import bubble_sort
from src.Sorting.insertion_sort import insertion_sort

import unittest

SMALL = 64
LARGE = 1 << 10


class TestSorting(TestCase):
    CASES = []
    def setUp(self):
        self.CASES.clear()
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
        print("done")

    def sorting_algo(self, descrip:str, algo, reverse=False):
        print(descrip)
        for label, inp, ans in self.CASES:
            print(f"\ttest {label}", end=" -- ")
            inp_co, ans_co = inp.copy(), ans.copy()
            if reverse:
                ans_co.reverse()
            algo(inp_co, reverse)

            assert inp_co == ans_co, "sorted:{}\nans:{}".format(inp_co, ans_co)
            print("done")

    def test_bubble_sort_ascending(self):
        self.sorting_algo(descrip="Bubble sort ascending", algo=bubble_sort, reverse=False)

    def test_bubble_sort_descending(self):
        self.sorting_algo(descrip="Bubble sort descending", algo=bubble_sort, reverse=True)

    def test_insertion_sort_ascending(self):
        self.sorting_algo(descrip="Insertion sort ascending", algo=insertion_sort, reverse=False)

    def test_insertion_sort_descending(self):
        self.sorting_algo(descrip="Insertion sort descending", algo=insertion_sort, reverse=True)















