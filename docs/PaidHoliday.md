# PaidHoliday

Data object representing a University of Waterloo paid holiday

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**holiday_date** | **datetime** | Date of the paid holiday event | [optional] 
**name** | **str** | Name of the paid holiday | [optional] 

## Example

```python
from openapi_client.models.paid_holiday import PaidHoliday

# TODO update the JSON string below
json = "{}"
# create an instance of PaidHoliday from a JSON string
paid_holiday_instance = PaidHoliday.from_json(json)
# print the JSON string representation of the object
print PaidHoliday.to_json()

# convert the object into a dict
paid_holiday_dict = paid_holiday_instance.to_dict()
# create an instance of PaidHoliday from a dict
paid_holiday_form_dict = paid_holiday.from_dict(paid_holiday_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


