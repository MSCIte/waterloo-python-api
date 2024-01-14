# Combo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**image** | [**ComboImage**](ComboImage.md) |  | [optional] 
**options** | **str** |  | [optional] 
**item** | **str** |  | [optional] 
**price** | **str** |  | [optional] 
**calories** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.combo import Combo

# TODO update the JSON string below
json = "{}"
# create an instance of Combo from a JSON string
combo_instance = Combo.from_json(json)
# print the JSON string representation of the object
print Combo.to_json()

# convert the object into a dict
combo_dict = combo_instance.to_dict()
# create an instance of Combo from a dict
combo_form_dict = combo.from_dict(combo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


