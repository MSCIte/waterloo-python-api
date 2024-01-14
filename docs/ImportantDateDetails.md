# ImportantDateDetails

Details about terms, dates, and special notes for an Important Date

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**important_date_id** | **int** | Id link to associated Important Date, internal | [optional] 
**term_id** | **int** | Id to the associated Term | [optional] 
**term_name** | **str** | Name of the associated Term when the Important Date takes place | [optional] 
**start_date** | **datetime** | Start or event date for the Important Date | [optional] 
**end_date** | **datetime** | Optional end date for the Important Date | [optional] 
**notes** | **str** | Any special notes for this occurance of the Important Date, can contain markup | [optional] 

## Example

```python
from openapi_client.models.important_date_details import ImportantDateDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ImportantDateDetails from a JSON string
important_date_details_instance = ImportantDateDetails.from_json(json)
# print the JSON string representation of the object
print ImportantDateDetails.to_json()

# convert the object into a dict
important_date_details_dict = important_date_details_instance.to_dict()
# create an instance of ImportantDateDetails from a dict
important_date_details_form_dict = important_date_details.from_dict(important_date_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


