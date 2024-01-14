# Course

An academic Course at Waterloo, a Course can be scheduled to become a Class

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**course_id** | **str** | Course Id that identifies this Course, not unique across terms | [optional] 
**course_offer_number** | **int** | Course Offer Number identifies cross-listed and similar Courses that shared a Course Id in a Term | [optional] 
**term_code** | **str** | Waterloo Term code for which this Course data applies | [optional] 
**term_name** | **str** | Waterloo Term name for which this Course data applies | [optional] 
**associated_academic_career** | **str** | Academic Career code associated with Course | [optional] 
**associated_academic_group_code** | **str** | The Academic Group code that is assocaited to this Course | [optional] 
**associated_academic_org_code** | **str** | The Academic Organization code that is associated to this Course | [optional] 
**subject_code** | **str** | The Subject code for this Course | [optional] 
**catalog_number** | **str** | The Catalog Number for this Course | [optional] 
**title** | **str** | Course title, full name of course | [optional] 
**description_abbreviated** | **str** | Short description of the course, often an abbreviation of the title | [optional] 
**description** | **str** | Description of the Course content and topics | [optional] 
**grading_basis** | **str** | Code to describe the grading basis for this course, can be overriden at Class level | [optional] 
**course_component_code** | **str** | Course Component Code that describes if the course is a lecture, tutorial, etc. | [optional] 
**enroll_consent_code** | **str** | Code describing whether No, Instructor, or Department consent to enroll is required. Can be overwridden at Class level. | [optional] 
**enroll_consent_description** | **str** | Description of the enroll requirement. Can be overwridden at Class level. | [optional] [readonly] 
**drop_consent_code** | **str** | Code describing whether No, Instructor, or Department consent to drop is required. Can be overwridden at Class level. | [optional] 
**drop_consent_description** | **str** | Description of the drop requirement. Can be overwridden at Class level. | [optional] [readonly] 
**requirements_description** | **str** | Description of the Course requirements, such as pre-requisites, anti-requisites, and co-requisites | [optional] 

## Example

```python
from openapi_client.models.course import Course

# TODO update the JSON string below
json = "{}"
# create an instance of Course from a JSON string
course_instance = Course.from_json(json)
# print the JSON string representation of the object
print Course.to_json()

# convert the object into a dict
course_dict = course_instance.to_dict()
# create an instance of Course from a dict
course_form_dict = course.from_dict(course_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


