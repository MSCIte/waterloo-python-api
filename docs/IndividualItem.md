# IndividualItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**photo** | [**IndividualItemPhoto**](IndividualItemPhoto.md) |  | [optional] 
**price** | **str** |  | [optional] 
**calories** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.individual_item import IndividualItem

# TODO update the JSON string below
json = "{}"
# create an instance of IndividualItem from a JSON string
individual_item_instance = IndividualItem.from_json(json)
# print the JSON string representation of the object
print IndividualItem.to_json()

# convert the object into a dict
individual_item_dict = individual_item_instance.to_dict()
# create an instance of IndividualItem from a dict
individual_item_form_dict = individual_item.from_dict(individual_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


