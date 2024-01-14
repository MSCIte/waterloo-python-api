# HoursChange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **datetime** |  | [optional] 
**value2** | **datetime** |  | [optional] 
**timezone_db** | **str** |  | [optional] 
**date_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.hours_change import HoursChange

# TODO update the JSON string below
json = "{}"
# create an instance of HoursChange from a JSON string
hours_change_instance = HoursChange.from_json(json)
# print the JSON string representation of the object
print HoursChange.to_json()

# convert the object into a dict
hours_change_dict = hours_change_instance.to_dict()
# create an instance of HoursChange from a dict
hours_change_form_dict = hours_change.from_dict(hours_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


