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

    def test_public_repo_url(self) -> None:
        """This method tests {public_repos_url} method"""
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {
                'repos_url': 'https://api.github.com/users/mamma/repos',
            }
            self.assertEqual(
                GithubOrgClient('mamma')._public_repos_url,
                "https://api.github.com/users/mamma/repos",
            )
