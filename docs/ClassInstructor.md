# ClassInstructor

A person instructing a Class

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**course_id** | **str** | Course identifier number, not unique | [optional] 
**course_offer_number** | **int** | Course offer number identifier for this class | [optional] 
**session_code** | **str** | Session code number for this class | [optional] 
**class_section** | **int** | Number identifying the section of this class | [optional] 
**term_code** | **str** | Waterloo academic term code | [optional] 
**instructor_role_code** | **str** | REMOVED for privacy. The code designation for the instructor&#39;s role in this class | [optional] 
**instructor_first_name** | **str** | REMOVED for privacy. The Instructors preferred first name | [optional] 
**instructor_last_name** | **str** | REMOVED for privacy. The Instructors preferred last name | [optional] 
**instructor_unique_identifier** | **str** | REMOVED for privacy. A unique identifier that persists through name changes. Not guaranteed, but likely to be immutable for instructor. | [optional] 
**class_meeting_number** | **int** | Identifier for the class meeting this instructor is for | [optional] 

## Example

```python
from openapi_client.models.class_instructor import ClassInstructor

# TODO update the JSON string below
json = "{}"
# create an instance of ClassInstructor from a JSON string
class_instructor_instance = ClassInstructor.from_json(json)
# print the JSON string representation of the object
print ClassInstructor.to_json()

# convert the object into a dict
class_instructor_dict = class_instructor_instance.to_dict()
# create an instance of ClassInstructor from a dict
class_instructor_form_dict = class_instructor.from_dict(class_instructor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


