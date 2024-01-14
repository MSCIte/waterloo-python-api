# FoodServicesOutlet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**var_self** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**image** | [**List[FoodServicesOutletImage]**](FoodServicesOutletImage.md) |  | [optional] 
**photo** | [**FoodServicesOutletPhoto**](FoodServicesOutletPhoto.md) |  | [optional] 
**features** | **str** |  | [optional] 
**outlettype** | [**List[OutletType]**](OutletType.md) |  | [optional] 
**outletlocation** | **str** |  | [optional] 
**locationlink** | [**LocationLink**](LocationLink.md) |  | [optional] 
**description** | **str** |  | [optional] 
**location** | [**List[OutletLocation]**](OutletLocation.md) |  | [optional] 
**summary** | **str** |  | [optional] 
**cuisine** | [**List[Cuisine]**](Cuisine.md) |  | [optional] 
**openinghours** | [**List[OpeningHour]**](OpeningHour.md) |  | [optional] 
**paymentaccepted** | [**List[PaymentAccepted]**](PaymentAccepted.md) |  | [optional] 
**closed** | [**List[Closed]**](Closed.md) |  | [optional] 
**hourschange** | [**List[HoursChange]**](HoursChange.md) |  | [optional] 
**notice** | **str** |  | [optional] 
**franchisemenu** | [**List[FranchiseMenu]**](FranchiseMenu.md) |  | [optional] 
**sticky** | **str** |  | [optional] 
**created** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.food_services_outlet import FoodServicesOutlet

# TODO update the JSON string below
json = "{}"
# create an instance of FoodServicesOutlet from a JSON string
food_services_outlet_instance = FoodServicesOutlet.from_json(json)
# print the JSON string representation of the object
print FoodServicesOutlet.to_json()

# convert the object into a dict
food_services_outlet_dict = food_services_outlet_instance.to_dict()
# create an instance of FoodServicesOutlet from a dict
food_services_outlet_form_dict = food_services_outlet.from_dict(food_services_outlet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


