# SiteOpportunity

Model representing a WCMS Opportunity (Job)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**site_id** | **int** | Unique, numeric site ID | [optional] 
**unique_key** | **str** | Unique Id of this opportunity item | [optional] 
**title** | **str** | Title of the opportunity | [optional] 
**publisher_username** | **str** | Username of the user that published this item | [optional] 
**updated_date** | **datetime** | Last updated date | [optional] 
**opportunity_type** | **str** | Type of opportunity (ie: volunteer, paid) | [optional] 
**employment_type** | **str** | Employment type (ie: part, full, other) | [optional] 
**rate_of_pay** | **str** | Rate of paay description | [optional] 
**rate_of_pay_type** | **str** | Rate of pay type | [optional] 
**content** | **str** | Opportunity description/content, usually includes HTML markup | [optional] 
**posted_or_open_date** | **datetime** | Posted or open for application date | [optional] 
**posted_or_open_date_time_zone** | **str** | Posted or open date time zone | [optional] 
**application_deadline_date** | **datetime** | Opportunity application deadline date | [optional] 
**start_date** | **datetime** | Start date for the opportunity | [optional] 
**end_date** | **datetime** | End date for the opportunity | [optional] 
**number_of_positions** | **str** | Number of positions available for this opportunity | [optional] 
**application_uri** | **str** | URI for an external applicaton website | [optional] 

## Example

```python
from openapi_client.models.site_opportunity import SiteOpportunity

# TODO update the JSON string below
json = "{}"
# create an instance of SiteOpportunity from a JSON string
site_opportunity_instance = SiteOpportunity.from_json(json)
# print the JSON string representation of the object
print SiteOpportunity.to_json()

# convert the object into a dict
site_opportunity_dict = site_opportunity_instance.to_dict()
# create an instance of SiteOpportunity from a dict
site_opportunity_form_dict = site_opportunity.from_dict(site_opportunity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


