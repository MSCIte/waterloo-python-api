# FoodServicesOutletImage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**filemime** | **str** |  | [optional] 
**filesize** | **str** |  | [optional] 
**width** | **str** |  | [optional] 
**height** | **str** |  | [optional] 
**alt** | **str** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.food_services_outlet_image import FoodServicesOutletImage

# TODO update the JSON string below
json = "{}"
# create an instance of FoodServicesOutletImage from a JSON string
food_services_outlet_image_instance = FoodServicesOutletImage.from_json(json)
# print the JSON string representation of the object
print FoodServicesOutletImage.to_json()

# convert the object into a dict
food_services_outlet_image_dict = food_services_outlet_image_instance.to_dict()
# create an instance of FoodServicesOutletImage from a dict
food_services_outlet_image_form_dict = food_services_outlet_image.from_dict(food_services_outlet_image_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


