# ComboImage


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
from openapi_client.models.combo_image import ComboImage

# TODO update the JSON string below
json = "{}"
# create an instance of ComboImage from a JSON string
combo_image_instance = ComboImage.from_json(json)
# print the JSON string representation of the object
print ComboImage.to_json()

# convert the object into a dict
combo_image_dict = combo_image_instance.to_dict()
# create an instance of ComboImage from a dict
combo_image_form_dict = combo_image.from_dict(combo_image_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


