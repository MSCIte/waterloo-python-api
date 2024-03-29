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

from openapi_client.models.workbench_moderation import WorkbenchModeration

class TestWorkbenchModeration(unittest.TestCase):
    """WorkbenchModeration unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WorkbenchModeration:
        """Test WorkbenchModeration
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WorkbenchModeration`
        """
        model = WorkbenchModeration()
        if include_optional:
            return WorkbenchModeration(
                current = openapi_client.models.current.Current(
                    hid = '', 
                    vid = '', 
                    nid = '', 
                    from_state = '', 
                    state = '', 
                    uid = '', 
                    stamp = '', 
                    published = '', 
                    is_current = 56, 
                    title = '', 
                    timestamp = '', ),
                published = openapi_client.models.published.Published(
                    hid = '', 
                    vid = '', 
                    nid = '', 
                    from_state = '', 
                    state = '', 
                    uid = '', 
                    stamp = '', 
                    is_current = 56, 
                    title = '', 
                    timestamp = '', ),
                my_revision = openapi_client.models.my_revision.My_Revision(
                    hid = '', 
                    vid = '', 
                    nid = '', 
                    from_state = '', 
                    state = '', 
                    uid = '', 
                    stamp = '', 
                    published = '', 
                    is_current = 56, 
                    title = '', 
                    timestamp = '', )
            )
        else:
            return WorkbenchModeration(
        )
        """

    def testWorkbenchModeration(self):
        """Test WorkbenchModeration"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
