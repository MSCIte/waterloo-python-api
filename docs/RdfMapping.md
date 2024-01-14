# RdfMapping


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rdftype** | **List[str]** |  | [optional] 
**title** | [**Title**](Title.md) |  | [optional] 
**created** | [**Created**](Created.md) |  | [optional] 
**changed** | [**Changed**](Changed.md) |  | [optional] 
**body** | [**Body**](Body.md) |  | [optional] 
**uid** | [**Uid**](Uid.md) |  | [optional] 
**name** | [**Name**](Name.md) |  | [optional] 
**comment_count** | [**CommentCount**](CommentCount.md) |  | [optional] 
**last_activity** | [**LastActivity**](LastActivity.md) |  | [optional] 

## Example

```python
from openapi_client.models.rdf_mapping import RdfMapping

# TODO update the JSON string below
json = "{}"
# create an instance of RdfMapping from a JSON string
rdf_mapping_instance = RdfMapping.from_json(json)
# print the JSON string representation of the object
print RdfMapping.to_json()

# convert the object into a dict
rdf_mapping_dict = rdf_mapping_instance.to_dict()
# create an instance of RdfMapping from a dict
rdf_mapping_form_dict = rdf_mapping.from_dict(rdf_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


