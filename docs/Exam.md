# Exam

Represents a scheduled Exam for a Class

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exam_display_name** | **str** | The name of the Exam, representative of the Course name | [optional] 
**sections** | **str** | Sections of the Class this Exam schedule is applicable to | [optional] 
**is_online_description** | **str** | Indicates whether this Exam is held online, or provides an alternate description | [optional] 
**day** | **str** | Day name on which this Exam is scheduled to take place | [optional] 
**location** | **str** | Description of the location of the Exam | [optional] 
**exam_window_start_date** | **str** | The date the Exam is scheduled for | [optional] 
**exam_window_start_time** | **str** | The time the Exam is scheduled to start | [optional] 
**exam_duration** | **str** | The scheduled duration of the Exam | [optional] 
**notes** | **str** | Additional notes about this Exam schedule | [optional] 
**term_code** | **str** | Term Code for the Term this Exam is associated with | [optional] 

## Example

```python
from openapi_client.models.exam import Exam

# TODO update the JSON string below
json = "{}"
# create an instance of Exam from a JSON string
exam_instance = Exam.from_json(json)
# print the JSON string representation of the object
print Exam.to_json()

# convert the object into a dict
exam_dict = exam_instance.to_dict()
# create an instance of Exam from a dict
exam_form_dict = exam.from_dict(exam_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


