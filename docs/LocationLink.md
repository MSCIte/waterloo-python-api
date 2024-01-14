# LocationLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 
**title** | **object** |  | [optional] 
**attributes** | **List[object]** |  | [optional] 
**original_title** | **object** |  | [optional] 
**original_url** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.location_link import LocationLink

# TODO update the JSON string below
json = "{}"
# create an instance of LocationLink from a JSON string
location_link_instance = LocationLink.from_json(json)
# print the JSON string representation of the object
print LocationLink.to_json()

# convert the object into a dict
location_link_dict = location_link_instance.to_dict()
# create an instance of LocationLink from a dict
location_link_form_dict = location_link.from_dict(location_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


