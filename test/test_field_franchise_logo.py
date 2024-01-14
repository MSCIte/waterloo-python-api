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

from openapi_client.models.field_franchise_logo import FieldFranchiseLogo

class TestFieldFranchiseLogo(unittest.TestCase):
    """FieldFranchiseLogo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FieldFranchiseLogo:
        """Test FieldFranchiseLogo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FieldFranchiseLogo`
        """
        model = FieldFranchiseLogo()
        if include_optional:
            return FieldFranchiseLogo(
                und = [
                    openapi_client.models.und1.Und1(
                        fid = '', 
                        uid = '', 
                        filename = '', 
                        uri = '', 
                        filemime = '', 
                        filesize = '', 
                        status = '', 
                        timestamp = '', 
                        uuid = '', 
                        rdf_mapping = [
                            null
                            ], 
                        focal_point = '', 
                        alt = '', 
                        title = '', 
                        width = '', 
                        height = '', )
                    ]
            )
        else:
            return FieldFranchiseLogo(
        )
        """

    def testFieldFranchiseLogo(self):
        """Test FieldFranchiseLogo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()