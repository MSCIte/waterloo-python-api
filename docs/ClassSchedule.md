# ClassSchedule

Data describing scheduling and availability data for a Class

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**course_id** | **str** | Course identifier number, not unique | [optional] 
**course_offer_number** | **int** | Course offer number identifier for this class | [optional] 
**session_code** | **str** | Session code number for this class | [optional] 
**class_section** | **int** | Number identifying the section of this class | [optional] 
**term_code** | **str** | Waterloo academic term code | [optional] 
**class_meeting_number** | **int** | Identifier for the class meeting this schedule data relates to | [optional] 
**schedule_start_date** | **datetime** | The date this schedule begins | [optional] 
**schedule_end_date** | **datetime** | The date this schedule ends | [optional] 
**class_meeting_start_time** | **datetime** | The start time of this class | [optional] 
**class_meeting_end_time** | **datetime** | The end time of this class | [optional] 
**class_meeting_day_pattern_code** | **str** | A code representing the days the class schedule takes place during the week | [optional] 
**class_meeting_week_pattern_code** | **str** | A Y|N per day representation of the class schedule taking place during the week | [optional] 
**location_name** | **str** | REMOVED for privacy. Building and room name for the location of this class schedule | [optional] 

## Example

```python
from openapi_client.models.class_schedule import ClassSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of ClassSchedule from a JSON string
class_schedule_instance = ClassSchedule.from_json(json)
# print the JSON string representation of the object
print ClassSchedule.to_json()

# convert the object into a dict
class_schedule_dict = class_schedule_instance.to_dict()
# create an instance of ClassSchedule from a dict
class_schedule_form_dict = class_schedule.from_dict(class_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


