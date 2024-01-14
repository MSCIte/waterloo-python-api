# Site

Model representing a Site on the Waterloo CMS

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**site_id** | **int** | Unique, numeric site ID | [optional] 
**relative_uri** | **str** | Relative URI of the site from the root uWaterloo CMS domain | [optional] 
**name** | **str** | Display name of the Site | [optional] 
**owner_unit_code** | **str** | If available, the department owner code for this Site. Can loosely map to Academic Groups. | [optional] 
**owner_unit_name_short** | **str** | Short name of the department owner for this Site. See OwnerUnitCode for more. | [optional] 
**owner_unit_name_full** | **str** | Full name of the department owner for this Site. See OwnerUnitCode for more. | [optional] 
**owner_group_code** | **str** | If available, the faculty owner code for this Site. Can loosely map to Academic Organization. | [optional] 
**owner_type** | **str** | The tag describing the association of the owner department, such as academic, research, and more. | [optional] 

## Example

```python
from openapi_client.models.site import Site

# TODO update the JSON string below
json = "{}"
# create an instance of Site from a JSON string
site_instance = Site.from_json(json)
# print the JSON string representation of the object
print Site.to_json()

# convert the object into a dict
site_dict = site_instance.to_dict()
# create an instance of Site from a dict
site_form_dict = site.from_dict(site_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


