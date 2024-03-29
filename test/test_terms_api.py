# coding: utf-8

"""
    Waterloo OpenData API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.terms_api import TermsApi


class TestTermsApi(unittest.TestCase):
    """TermsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = TermsApi()

    def tearDown(self) -> None:
        pass

    def test_v3_terms_code_get(self) -> None:
        """Test case for v3_terms_code_get

        Gets Term data for a specific Term filtered by code
        """
        pass

    def test_v3_terms_current_get(self) -> None:
        """Test case for v3_terms_current_get

        Gets the current Term data
        """
        pass

    def test_v3_terms_foracademicyear_year_get(self) -> None:
        """Test case for v3_terms_foracademicyear_year_get

        Gets Term data for terms that are part of a specific academic year
        """
        pass

    def test_v3_terms_get(self) -> None:
        """Test case for v3_terms_get

        Gets all Term data that is effective at the current time
        """
        pass


if __name__ == '__main__':
    unittest.main()
