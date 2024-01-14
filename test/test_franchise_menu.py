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

from openapi_client.models.franchise_menu import FranchiseMenu

class TestFranchiseMenu(unittest.TestCase):
    """FranchiseMenu unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FranchiseMenu:
        """Test FranchiseMenu
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FranchiseMenu`
        """
        model = FranchiseMenu()
        if include_optional:
            return FranchiseMenu(
                vid = '',
                uid = '',
                title = '',
                log = '',
                status = '',
                comment = '',
                promote = '',
                sticky = '',
                vuuid = '',
                nid = '',
                type = '',
                language = '',
                created = '',
                changed = '',
                tnid = '',
                translate = '',
                uuid = '',
                revision_timestamp = '',
                revision_uid = '',
                field_addons = None,
                field_combos = openapi_client.models.field_combos.Field_Combos(
                    und = [
                        openapi_client.models.und.Und(
                            value = '', 
                            revision_id = '', )
                        ], ),
                field_franchise_logo = openapi_client.models.field_franchise_logo.Field_Franchise_Logo(
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
                        ], ),
                field_individual_items = None,
                title_field = openapi_client.models.title_field.Title_Field(
                    en = [
                        openapi_client.models.en.En(
                            value = '', 
                            format = null, 
                            safe_value = '', )
                        ], ),
                metatags = openapi_client.models.metatags.Metatags(
                    en = openapi_client.models.en1.En1(
                        robots = openapi_client.models.robots.Robots(
                            value = openapi_client.models.value.Value(
                                index = 56, 
                                follow = 56, 
                                noindex = 56, 
                                nofollow = 56, 
                                noarchive = 56, 
                                nosnippet = 56, 
                                noodp = 56, 
                                noydir = 56, 
                                noimageindex = 56, 
                                notranslate = 56, ), ), ), ),
                rdf_mapping = openapi_client.models.rdf_mapping.Rdf_Mapping(
                    rdftype = [
                        ''
                        ], 
                    title = openapi_client.models.title.Title(
                        predicates = [
                            ''
                            ], ), 
                    created = openapi_client.models.created.Created(
                        datatype = '', 
                        callback = '', ), 
                    changed = openapi_client.models.changed.Changed(
                        datatype = '', 
                        callback = '', ), 
                    body = openapi_client.models.body.Body(), 
                    uid = openapi_client.models.uid.Uid(
                        type = '', ), 
                    name = openapi_client.models.name.Name(), 
                    comment_count = openapi_client.models.comment_count.Comment_Count(
                        datatype = '', ), 
                    last_activity = openapi_client.models.last_activity.Last_Activity(
                        datatype = '', 
                        callback = '', ), ),
                path = openapi_client.models.path.Path(
                    pid = '', 
                    source = '', 
                    alias = '', 
                    language = '', 
                    pathauto = '', ),
                translations = openapi_client.models.translations.Translations(
                    original = '', 
                    data = openapi_client.models.data.Data(
                        en = openapi_client.models.en2.En2(
                            entity_type = '', 
                            entity_id = '', 
                            revision_id = '', 
                            language = '', 
                            source = '', 
                            uid = '', 
                            status = '', 
                            translate = '', 
                            created = '', 
                            changed = '', ), ), ),
                title_original = '',
                entity_translation_handler_id = '',
                title_language = '',
                cid = '',
                last_comment_timestamp = '',
                last_comment_name = None,
                last_comment_uid = '',
                comment_count = '',
                name = '',
                picture = '',
                data = '',
                uw_page_settings_node_enable = '',
                workbench_moderation = openapi_client.models.workbench_moderation.Workbench_Moderation(
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
                        is_current = 56, 
                        title = '', 
                        timestamp = '', ), )
            )
        else:
            return FranchiseMenu(
        )
        """

    def testFranchiseMenu(self):
        """Test FranchiseMenu"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()