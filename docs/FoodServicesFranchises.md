# FoodServicesFranchises


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[FoodServicesFranchise]**](FoodServicesFranchise.md) |  | [optional] 
**count** | **int** |  | [optional] 
**var_self** | [**FoodServicesFranchisesSelf**](FoodServicesFranchisesSelf.md) |  | [optional] 

## Example

```python
from openapi_client.models.food_services_franchises import FoodServicesFranchises

# TODO update the JSON string below
json = "{}"
# create an instance of FoodServicesFranchises from a JSON string
food_services_franchises_instance = FoodServicesFranchises.from_json(json)
# print the JSON string representation of the object
print FoodServicesFranchises.to_json()

# convert the object into a dict
food_services_franchises_dict = food_services_franchises_instance.to_dict()
# create an instance of FoodServicesFranchises from a dict
food_services_franchises_form_dict = food_services_franchises.from_dict(food_services_franchises_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


