# Published


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
from openapi_client.models.published import Published

# TODO update the JSON string below
json = "{}"
# create an instance of Published from a JSON string
published_instance = Published.from_json(json)
# print the JSON string representation of the object
print Published.to_json()

# convert the object into a dict
published_dict = published_instance.to_dict()
# create an instance of Published from a dict
published_form_dict = published.from_dict(published_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


