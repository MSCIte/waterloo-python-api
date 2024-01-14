# OpeningHour


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day** | **str** |  | [optional] 
**starthours** | **str** |  | [optional] 
**endhours** | **str** |  | [optional] 
**comment** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.opening_hour import OpeningHour

# TODO update the JSON string below
json = "{}"
# create an instance of OpeningHour from a JSON string
opening_hour_instance = OpeningHour.from_json(json)
# print the JSON string representation of the object
print OpeningHour.to_json()

# convert the object into a dict
opening_hour_dict = opening_hour_instance.to_dict()
# create an instance of OpeningHour from a dict
opening_hour_form_dict = opening_hour.from_dict(opening_hour_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


