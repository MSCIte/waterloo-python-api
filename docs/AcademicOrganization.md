# AcademicOrganization

An Academic Organization at Waterloo is similar to a department

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Unique Code of this Academic Organization | [optional] 
**name** | **str** | The Name for this Academic Organization, most often the display name | [optional] 
**description** | **str** | The short description for this Academic Organization | [optional] 
**description_formal** | **str** | The formal description for this Academic Organization, most often used in official capacity | [optional] 
**associated_campus_code** | **str** | The Code for the Campus that this Academic Organization is assigned to | [optional] 

## Example

```python
from openapi_client.models.academic_organization import AcademicOrganization

# TODO update the JSON string below
json = "{}"
# create an instance of AcademicOrganization from a JSON string
academic_organization_instance = AcademicOrganization.from_json(json)
# print the JSON string representation of the object
print AcademicOrganization.to_json()

# convert the object into a dict
academic_organization_dict = academic_organization_instance.to_dict()
# create an instance of AcademicOrganization from a dict
academic_organization_form_dict = academic_organization.from_dict(academic_organization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


