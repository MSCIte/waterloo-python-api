# WorkbenchModeration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current** | [**Current**](Current.md) |  | [optional] 
**published** | [**Published**](Published.md) |  | [optional] 
**my_revision** | [**MyRevision**](MyRevision.md) |  | [optional] 

## Example

```python
from openapi_client.models.workbench_moderation import WorkbenchModeration

# TODO update the JSON string below
json = "{}"
# create an instance of WorkbenchModeration from a JSON string
workbench_moderation_instance = WorkbenchModeration.from_json(json)
# print the JSON string representation of the object
print WorkbenchModeration.to_json()

# convert the object into a dict
workbench_moderation_dict = workbench_moderation_instance.to_dict()
# create an instance of WorkbenchModeration from a dict
workbench_moderation_form_dict = workbench_moderation.from_dict(workbench_moderation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


