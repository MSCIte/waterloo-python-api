# En2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_type** | **str** |  | [optional] 
**entity_id** | **str** |  | [optional] 
**revision_id** | **str** |  | [optional] 
**language** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**uid** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**translate** | **str** |  | [optional] 
**created** | **str** |  | [optional] 
**changed** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.en2 import En2

# TODO update the JSON string below
json = "{}"
# create an instance of En2 from a JSON string
en2_instance = En2.from_json(json)
# print the JSON string representation of the object
print En2.to_json()

# convert the object into a dict
en2_dict = en2_instance.to_dict()
# create an instance of En2 from a dict
en2_form_dict = en2.from_dict(en2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


