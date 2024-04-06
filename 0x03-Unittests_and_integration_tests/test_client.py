#!/usr/bin/env python3
""" This is a module to test Clients """
import client
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

    @patch('client.get_json')
    def test_public_repos(self, get_json_mock):
        """This is a test for public_repos function"""
        payload = {
                   'repos_url': 'https://api.github.com/users/mamma/repos',
                   'repos': [{
                              "name": "tester",
                              "is_staff": True,
                              "contact": {
                                  "addr": "User1 Contact Address",
                                  "email": "tester@test.com",
                                  "mobile": "1234567890",
                                }
                            },
                            {
                                "name": "user",
                                "is_staff": False,
                                "contact": {
                                    "addr": "User2 Contact Address",
                                    "email": "user@test.com",
                                    "mobile": "9876012345",
                                }
                            }]
                   }
        get_json_mock.return_value = payload['repos']
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as obj:
            obj.return_value = payload['repos_url']
            self.assertEqual(GithubOrgClient('google').public_repos(),
                             ['tester', 'user',],)
            obj.assert_called_once()
        get_json_mock.assert_called_once()

    @parameterized.expand([
        ({'license': {'key': "bsd-3-clause"}}, "bsd-3-clause", True),
        ({'license': {'key': "bsl-1.0"}}, "bsd-3-clause", False),
    ])
    def test_has_license(self, repo: dict, key: str, expected: bool) -> None:
        """This is a testmethod to tests the `has_license` method."""
        self.assertEqual(GithubOrgClient.has_license(repo, key), expected)


@parameterized_class([
    {
        'org_payload': TEST_PAYLOAD[0][0],
        'repos_payload': TEST_PAYLOAD[0][1],
        'expected_repos': TEST_PAYLOAD[0][2],
        'apache2_repos': TEST_PAYLOAD[0][3],
    },
])
class TestIntegrationGithubOrgClient(TestCase):
    """This is a class to perform Integration Tests"""
    @classmethod
    def setUpClass(cls) -> None:
        """Sets up the class {fixtures} before running tests."""
        route_payload = {
            'https://api.github.com/orgs/google': cls.org_payload,
            'https://api.github.com/orgs/google/repos': cls.repos_payload,
        }

        def get_payload(url):
            """This is a method to get payloads from URLS"""
            if url in route_payload:
                return Mock(**{'json.return_value': route_payload[url]})
            return requests.HTTPError

        cls.get_patcher = patch("requests.get", side_effect=get_payload)
        cls.get_patcher.start()

    def test_public_repos(self) -> None:
        """This is to tests the `public_repos` method."""
        self.assertEqual(
            GithubOrgClient("google").public_repos(),
            self.expected_repos,
        )

    def test_public_repos_with_license(self) -> None:
        """This is to test the `public_repos` method with a license."""
        self.assertEqual(
            GithubOrgClient("google").public_repos(license="apache-2.0"),
            self.apache2_repos,
        )

    @classmethod
    def tearDownClass(cls) -> None:
        """This method removes the fixtures class after all tests are run."""
        cls.get_patcher.stop()
