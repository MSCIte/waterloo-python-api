# FoodServicesOutlets


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[FoodServicesOutlet]**](FoodServicesOutlet.md) |  | [optional] 
**count** | **int** |  | [optional] 
**var_self** | [**FoodServicesOutletsSelf**](FoodServicesOutletsSelf.md) |  | [optional] 

## Example

```python
from openapi_client.models.food_services_outlets import FoodServicesOutlets

# TODO update the JSON string below
json = "{}"
# create an instance of FoodServicesOutlets from a JSON string
food_services_outlets_instance = FoodServicesOutlets.from_json(json)
# print the JSON string representation of the object
print FoodServicesOutlets.to_json()

# convert the object into a dict
food_services_outlets_dict = food_services_outlets_instance.to_dict()
# create an instance of FoodServicesOutlets from a dict
food_services_outlets_form_dict = food_services_outlets.from_dict(food_services_outlets_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


