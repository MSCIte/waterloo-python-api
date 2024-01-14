# OutletLocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lid** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**street** | **str** |  | [optional] 
**additional** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**province** | **str** |  | [optional] 
**postal_code** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**latitude** | **str** |  | [optional] 
**longitude** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**is_primary** | **str** |  | [optional] 
**locpick** | [**Locpick**](Locpick.md) |  | [optional] 
**province_name** | **str** |  | [optional] 
**country_name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.outlet_location import OutletLocation

# TODO update the JSON string below
json = "{}"
# create an instance of OutletLocation from a JSON string
outlet_location_instance = OutletLocation.from_json(json)
# print the JSON string representation of the object
print OutletLocation.to_json()

# convert the object into a dict
outlet_location_dict = outlet_location_instance.to_dict()
# create an instance of OutletLocation from a dict
outlet_location_form_dict = outlet_location.from_dict(outlet_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


