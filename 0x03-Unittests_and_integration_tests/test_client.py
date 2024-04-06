#!/usr/bin/env python3
""" This is a module to test Clients """
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
import utils
import requests
from unittest import TestCase
from unittest.mock import (MagicMock, patch, Mock, PropertyMock, call)
from parameterized import (parameterized, parameterized_class)


class TestGithubOrgClient(TestCase):
    """ Test that json can be gotten for request """
    @parameterized.expand([
        ("google", {"google": True}),
        ("abc", {"abc": True})
    ])
    @patch('client.get_json')
    def test_org(self, org: str, expected: dict, get_patch: MagicMock) -> None:
        """This is a method to test the org method"""
        get_patch.return_value = MagicMock(return_value=expected)
        org_client = GithubOrgClient(org)
        self.assertEqual(org_client.org(), expected)
        get_patch.assert_called_once_with(
            f"https://api.github.com/orgs/{org}"
        )

    def test_public_repos_url(self) -> None:
        """This method tests {public_repos_url} method"""
        result = "www.mamma.com"
        payload = {'repos_url': result}
        mock_data = 'client.GithubOrgClient.org'
        with patch(mock_data, PropertyMock(return_value=payload)):
            req = GithubOrgClient('x')
            self.assertEqual(req._public_repos_url, result)
