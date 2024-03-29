# coding: utf-8

"""
    Waterloo OpenData API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.combo import Combo

class TestCombo(unittest.TestCase):
    """Combo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Combo:
        """Test Combo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Combo`
        """
        model = Combo()
        if include_optional:
            return Combo(
                name = '',
                image = openapi_client.models.combo_image.ComboImage(
                    id = '', 
                    url = '', 
                    filemime = '', 
                    filesize = '', 
                    width = '', 
                    height = '', 
                    alt = '', 
                    title = '', ),
                options = '',
                item = '',
                price = '',
                calories = None
            )
        else:
            return Combo(
        )
        """

    def testCombo(self):
        """Test Combo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
