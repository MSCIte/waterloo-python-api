# FranchiseMenu


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vid** | **str** |  | [optional] 
**uid** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**log** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**comment** | **str** |  | [optional] 
**promote** | **str** |  | [optional] 
**sticky** | **str** |  | [optional] 
**vuuid** | **str** |  | [optional] 
**nid** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**language** | **str** |  | [optional] 
**created** | **str** |  | [optional] 
**changed** | **str** |  | [optional] 
**tnid** | **str** |  | [optional] 
**translate** | **str** |  | [optional] 
**uuid** | **str** |  | [optional] 
**revision_timestamp** | **str** |  | [optional] 
**revision_uid** | **str** |  | [optional] 
**field_addons** | **object** |  | [optional] 
**field_combos** | [**FieldCombos**](FieldCombos.md) |  | [optional] 
**field_franchise_logo** | [**FieldFranchiseLogo**](FieldFranchiseLogo.md) |  | [optional] 
**field_individual_items** | **object** |  | [optional] 
**title_field** | [**TitleField**](TitleField.md) |  | [optional] 
**metatags** | [**Metatags**](Metatags.md) |  | [optional] 
**rdf_mapping** | [**RdfMapping**](RdfMapping.md) |  | [optional] 
**path** | [**Path**](Path.md) |  | [optional] 
**translations** | [**Translations**](Translations.md) |  | [optional] 
**title_original** | **str** |  | [optional] 
**entity_translation_handler_id** | **str** |  | [optional] 
**title_language** | **str** |  | [optional] 
**cid** | **str** |  | [optional] 
**last_comment_timestamp** | **str** |  | [optional] 
**last_comment_name** | **object** |  | [optional] 
**last_comment_uid** | **str** |  | [optional] 
**comment_count** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**picture** | **str** |  | [optional] 
**data** | **str** |  | [optional] 
**uw_page_settings_node_enable** | **str** |  | [optional] 
**workbench_moderation** | [**WorkbenchModeration**](WorkbenchModeration.md) |  | [optional] 

## Example

```python
from openapi_client.models.franchise_menu import FranchiseMenu

# TODO update the JSON string below
json = "{}"
# create an instance of FranchiseMenu from a JSON string
franchise_menu_instance = FranchiseMenu.from_json(json)
# print the JSON string representation of the object
print FranchiseMenu.to_json()

# convert the object into a dict
franchise_menu_dict = franchise_menu_instance.to_dict()
# create an instance of FranchiseMenu from a dict
franchise_menu_form_dict = franchise_menu.from_dict(franchise_menu_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


