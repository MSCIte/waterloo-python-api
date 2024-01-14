# Body


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**predicates** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.body import Body

# TODO update the JSON string below
json = "{}"
# create an instance of Body from a JSON string
body_instance = Body.from_json(json)
# print the JSON string representation of the object
print Body.to_json()

# convert the object into a dict
body_dict = body_instance.to_dict()
# create an instance of Body from a dict
body_form_dict = body.from_dict(body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


