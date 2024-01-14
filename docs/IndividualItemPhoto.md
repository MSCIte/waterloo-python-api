# IndividualItemPhoto


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
from openapi_client.models.individual_item_photo import IndividualItemPhoto

# TODO update the JSON string below
json = "{}"
# create an instance of IndividualItemPhoto from a JSON string
individual_item_photo_instance = IndividualItemPhoto.from_json(json)
# print the JSON string representation of the object
print IndividualItemPhoto.to_json()

# convert the object into a dict
individual_item_photo_dict = individual_item_photo_instance.to_dict()
# create an instance of IndividualItemPhoto from a dict
individual_item_photo_form_dict = individual_item_photo.from_dict(individual_item_photo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


