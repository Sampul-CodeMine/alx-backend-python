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
    """This is a class to test the {access_nested_map} function"""
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


class TestGetJson(TestCase):
    """
    This is a class to test the {get_json} function
    Arguments are ordered in this format: test_url, test_payload
    """
    @parameterized.expand([
        ('http://example.com', {'payload': True}),
        ('http://holberton.io', {'payload': False})
    ])
    def test_get_json(self, test_url: str, test_payload: dict) -> None:
        """This is a method to test the {get_json} functionalities"""
        response = Mock()
        response.json.return_value = test_payload
        with patch('requests.get', return_value=response):
            output = get_json(test_url)
            self.assertEqual(output, test_payload)
            response.json.assert_called_once()


class TestMemoize(TestCase):
    """
    This is a class to test the {memoize} function
    """
    def test_memoize(self):
        """memoize function"""

        class TestClass:
            """This is a Test Class"""
            def a_method(self):
                """This method when called always returns 42"""
                return 42

            @memoize
            def a_property(self):
                """Returns memoize property"""
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as obj:
            test_cls = TestClass()
            output = test_cls.a_property
            output = test_cls.a_property
            self.assertEqual(output, 42)
            obj.assert_called_once()
