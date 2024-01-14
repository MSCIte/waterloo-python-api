# ModelClass

Represents an Academic class, which is a scheduled instance of a Course

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**course_id** | **str** | Course identifier number, not unique | [optional] 
**course_offer_number** | **int** | Course offer number identifier for this class | [optional] 
**session_code** | **str** | Session code for this class | [optional] 
**class_section** | **int** | Number identifying the section of this class | [optional] 
**term_code** | **str** | Waterloo academic term code | [optional] 
**class_number** | **int** | Class number identifier for this class | [optional] 
**course_component** | **str** | Course component code for this class | [optional] 
**associated_class_code** | **int** | Associated class code for this class | [optional] 
**max_enrollment_capacity** | **int** | Indicates the maximum number of students that can enroll in this class | [optional] 
**enrolled_students** | **int** | Indicates the current number of students enrolled in this class | [optional] 
**enroll_consent_code** | **str** | Code describing whether No, Instructor, or Department consent to enroll is required. Overrides Course level information if different. | [optional] 
**enroll_consent_description** | **str** | Description of the enroll requirement. Overrides Course level information if different. | [optional] [readonly] 
**drop_consent_code** | **str** | Code describing whether No, Instructor, or Department consent to drop is required. Overrides Course level information if different. | [optional] 
**drop_consent_description** | **str** | Description of the drop requirement. Overrides Course level information if different. | [optional] [readonly] 
**schedule_data** | [**List[ClassSchedule]**](ClassSchedule.md) | Schedule data for this class | [optional] 
**instructor_data** | [**List[ClassInstructor]**](ClassInstructor.md) | Instructor data for this class | [optional] 

## Example

```python
from openapi_client.models.model_class import ModelClass

# TODO update the JSON string below
json = "{}"
# create an instance of ModelClass from a JSON string
model_class_instance = ModelClass.from_json(json)
# print the JSON string representation of the object
print ModelClass.to_json()

# convert the object into a dict
model_class_dict = model_class_instance.to_dict()
# create an instance of ModelClass from a dict
model_class_form_dict = model_class.from_dict(model_class_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


