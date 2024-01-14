# Closed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **datetime** |  | [optional] 
**value2** | **datetime** |  | [optional] 
**timezone_db** | **str** |  | [optional] 
**date_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.closed import Closed

# TODO update the JSON string below
json = "{}"
# create an instance of Closed from a JSON string
closed_instance = Closed.from_json(json)
# print the JSON string representation of the object
print Closed.to_json()

# convert the object into a dict
closed_dict = closed_instance.to_dict()
# create an instance of Closed from a dict
closed_form_dict = closed.from_dict(closed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


