# FoodServicesFranchise


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**var_self** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**logo** | [**Logo**](Logo.md) |  | [optional] 
**combos** | [**List[Combo]**](Combo.md) |  | [optional] 
**individualitems** | [**List[IndividualItem]**](IndividualItem.md) |  | [optional] 
**addons** | [**List[Addon]**](Addon.md) |  | [optional] 

## Example

```python
from openapi_client.models.food_services_franchise import FoodServicesFranchise

# TODO update the JSON string below
json = "{}"
# create an instance of FoodServicesFranchise from a JSON string
food_services_franchise_instance = FoodServicesFranchise.from_json(json)
# print the JSON string representation of the object
print FoodServicesFranchise.to_json()

# convert the object into a dict
food_services_franchise_dict = food_services_franchise_instance.to_dict()
# create an instance of FoodServicesFranchise from a dict
food_services_franchise_form_dict = food_services_franchise.from_dict(food_services_franchise_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


