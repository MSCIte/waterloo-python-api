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

from openapi_client.models.course import Course

class TestCourse(unittest.TestCase):
    """Course unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Course:
        """Test Course
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Course`
        """
        model = Course()
        if include_optional:
            return Course(
                course_id = '',
                course_offer_number = 56,
                term_code = '',
                term_name = '',
                associated_academic_career = '',
                associated_academic_group_code = '',
                associated_academic_org_code = '',
                subject_code = '',
                catalog_number = '',
                title = '',
                description_abbreviated = '',
                description = '',
                grading_basis = '',
                course_component_code = '',
                enroll_consent_code = '',
                enroll_consent_description = '',
                drop_consent_code = '',
                drop_consent_description = '',
                requirements_description = ''
            )
        else:
            return Course(
        )
        """

    def testCourse(self):
        """Test Course"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
