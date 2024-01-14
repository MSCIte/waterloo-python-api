# OutletType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tid** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.outlet_type import OutletType

# TODO update the JSON string below
json = "{}"
# create an instance of OutletType from a JSON string
outlet_type_instance = OutletType.from_json(json)
# print the JSON string representation of the object
print OutletType.to_json()

# convert the object into a dict
outlet_type_dict = outlet_type_instance.to_dict()
# create an instance of OutletType from a dict
outlet_type_form_dict = outlet_type.from_dict(outlet_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


