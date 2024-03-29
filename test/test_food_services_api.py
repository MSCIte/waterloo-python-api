# coding: utf-8

"""
    Waterloo OpenData API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.food_services_api import FoodServicesApi


class TestFoodServicesApi(unittest.TestCase):
    """FoodServicesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = FoodServicesApi()

    def tearDown(self) -> None:
        pass

    def test_v3_food_services_franchises_get(self) -> None:
        """Test case for v3_food_services_franchises_get

        Get all food service Franchise data
        """
        pass

    def test_v3_food_services_franchises_id_get(self) -> None:
        """Test case for v3_food_services_franchises_id_get

        Get specific food sercices Franchise data by Id
        """
        pass

    def test_v3_food_services_franchises_name_get(self) -> None:
        """Test case for v3_food_services_franchises_name_get

        Get specific food services Franchise data by Franchise name
        """
        pass

    def test_v3_food_services_outlets_get(self) -> None:
        """Test case for v3_food_services_outlets_get

        Get all food service Outlet data
        """
        pass

    def test_v3_food_services_outlets_id_get(self) -> None:
        """Test case for v3_food_services_outlets_id_get

        Get specific food services Outlet data by Id
        """
        pass

    def test_v3_food_services_outlets_name_get(self) -> None:
        """Test case for v3_food_services_outlets_name_get

        Get specific food services Outlet data by Outlet name
        """
        pass


if __name__ == '__main__':
    unittest.main()
