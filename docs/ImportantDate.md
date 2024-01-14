# ImportantDate

An Important Date is an event at a time that has significance to the Waterloo community

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique, non-persistent Api Id for this resource | [optional] 
**name** | **str** | Name/Title of the Important Date | [optional] 
**description** | **str** | Optional description of the Important Date, can contain markup | [optional] 
**important_date_type** | **str** | The type category this Important Date belongs to | [optional] 
**details** | [**List[ImportantDateDetails]**](ImportantDateDetails.md) | Details about terms, dates, and special notes | [optional] 
**keywords** | **List[str]** | Keywords associated with the Important Date | [optional] 
**audiences** | **List[str]** | Audiences associated with the Important Date | [optional] 

## Example

```python
from openapi_client.models.important_date import ImportantDate

# TODO update the JSON string below
json = "{}"
# create an instance of ImportantDate from a JSON string
important_date_instance = ImportantDate.from_json(json)
# print the JSON string representation of the object
print ImportantDate.to_json()

# convert the object into a dict
important_date_dict = important_date_instance.to_dict()
# create an instance of ImportantDate from a dict
important_date_form_dict = important_date.from_dict(important_date_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


