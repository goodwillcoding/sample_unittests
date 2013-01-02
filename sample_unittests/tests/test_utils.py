# -*- coding: utf-8 -*-

"""
Test utils
"""

import unittest

from ..utils import NoSeparatorError


# --------------------------------------------------------------------------- #
class Test_split_argument(unittest.TestCase):

    # ....................................................................... #
    def _callFUT(self, test_string):
        from ..utils import split_argument
        return split_argument(test_string)

    # ....................................................................... #
    def test_colon_separator(self):
        test_string = "a:b"
        desired_return_tuple = ("a", "b")

        self.assertTupleEqual(self._callFUT(test_string), desired_return_tuple)

    # ....................................................................... #
    def test_equal_separator(self):
        test_string = "a=b"
        desired_return_tuple = ("a", "b")

        self.assertTupleEqual(self._callFUT(test_string), desired_return_tuple)

    # ....................................................................... #
    def test_colon_separator_first(self):
        test_string = "a:=b"
        desired_return_tuple = ("a", "=b")

        self.assertTupleEqual(self._callFUT(test_string), desired_return_tuple)

    # ....................................................................... #
    def test_equal_separator_first(self):
        test_string = "a=:b"
        desired_return_tuple = ("a", ":b")

        self.assertTupleEqual(self._callFUT(test_string), desired_return_tuple)

    # ....................................................................... #
    def test_no_separator_exception(self):
        test_string = "ab"
        self.assertRaises(NoSeparatorError, self._callFUT, test_string)


# --------------------------------------------------------------------------- #
class Test_split_argument2(unittest.TestCase):

    # ....................................................................... #
    def _callFUT(self, test_string):
        from ..utils import split_argument2
        return split_argument2(test_string)

    # # ....................................................................... #
    def test_colon_separator(self):
        test_string = "a:b"
        desired_return_tuple = ("a", "b")

        self.assertTupleEqual(self._callFUT(test_string), desired_return_tuple)

    # # ....................................................................... #
    # def test_equal_separator(self):
    #     test_string = "a=b"
    #     desired_return_tuple = ("a", "b")

    #     self.assertTupleEqual(self._callFUT(test_string), desired_return_tuple)

    # # ....................................................................... #
    # def test_colon_separator_first(self):
    #     test_string = "a:=b"
    #     desired_return_tuple = ("a", "=b")

    #     self.assertTupleEqual(self._callFUT(test_string), desired_return_tuple)

    # # ....................................................................... #
    # def test_equal_separator_first(self):
    #     test_string = "a=:b"
    #     desired_return_tuple = ("a", ":b")

    #     self.assertTupleEqual(self._callFUT(test_string), desired_return_tuple)

    # # ....................................................................... #
    def test_no_separator_exception(self):
        test_string = "ab"
        self.assertRaises(NoSeparatorError, self._callFUT, test_string)
