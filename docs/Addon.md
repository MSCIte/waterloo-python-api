# Addon


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**photo** | **object** |  | [optional] 
**price** | **str** |  | [optional] 
**calories** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.addon import Addon

# TODO update the JSON string below
json = "{}"
# create an instance of Addon from a JSON string
addon_instance = Addon.from_json(json)
# print the JSON string representation of the object
print Addon.to_json()

# convert the object into a dict
addon_dict = addon_instance.to_dict()
# create an instance of Addon from a dict
addon_form_dict = addon.from_dict(addon_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


