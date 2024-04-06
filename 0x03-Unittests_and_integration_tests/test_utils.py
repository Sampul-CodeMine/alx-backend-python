#!/usr/bin/env python3
"""
This is a Unittest Module to Test the utils.py functionalities
"""

from unittest import (TestCase, mock)
from unittest.mock import (Mock, patch)
from parameterized import parameterized
from typing import (Dict, Tuple, Union)
from utils import (access_nested_map, get_json, memoize)


class TestAccessNestedMap(TestCase):
    """This is a class to test the access_nested_map function"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self,
                               nested_map: dict,
                               path: Tuple[str],
                               expected: Union[Dict, int]) -> None:
        """This is a test method for the {access_nested_map} funtionality"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self,
                                         nested_map: dict,
                                         path: Tuple[str],
                                         error: Exception) -> None:
        """This test method checks for the exceptions raised"""
        with self.assertRaises(KeyError) as err:
            access_nested_map(nested_map, path)
            self.assertEqual(error, err.exception)
