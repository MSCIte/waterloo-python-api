# Current


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hid** | **str** |  | [optional] 
**vid** | **str** |  | [optional] 
**nid** | **str** |  | [optional] 
**from_state** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**uid** | **str** |  | [optional] 
**stamp** | **str** |  | [optional] 
**published** | **str** |  | [optional] 
**is_current** | **int** |  | [optional] 
**title** | **str** |  | [optional] 
**timestamp** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.current import Current

# TODO update the JSON string below
json = "{}"
# create an instance of Current from a JSON string
current_instance = Current.from_json(json)
# print the JSON string representation of the object
print Current.to_json()

# convert the object into a dict
current_dict = current_instance.to_dict()
# create an instance of Current from a dict
current_form_dict = current.from_dict(current_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


