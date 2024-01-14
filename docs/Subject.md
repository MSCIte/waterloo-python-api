# Subject

An academic Subject at Waterloo describes an area that a Course can be in

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Code that identifies this Subject | [optional] 
**name** | **str** | The Name for this Subject, most often the displayed name | [optional] 
**description_abbreviated** | **str** | The short description of this subject, often same as Code | [optional] 
**description** | **str** | Description of the Subject | [optional] 
**associated_academic_org_code** | **str** | Code for the Academic Organization that is associated to this Subject | [optional] 

## Example

```python
from openapi_client.models.subject import Subject

# TODO update the JSON string below
json = "{}"
# create an instance of Subject from a JSON string
subject_instance = Subject.from_json(json)
# print the JSON string representation of the object
print Subject.to_json()

# convert the object into a dict
subject_dict = subject_instance.to_dict()
# create an instance of Subject from a dict
subject_form_dict = subject.from_dict(subject_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


