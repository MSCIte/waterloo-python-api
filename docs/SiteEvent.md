# SiteEvent

Model representing a WCMS Event item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**site_id** | **int** | Unique, numeric site ID | [optional] 
**unique_key** | **str** | Unique Id of this evevnt item | [optional] 
**title** | **str** | Title of the event | [optional] 
**event_start_date** | **datetime** | Start date of the event | [optional] 
**event_end_date** | **datetime** | End date of the event | [optional] 
**recur_rule** | **str** | Description of the event recurrence rule | [optional] 
**event_timezone** | **str** | Time zone description of the event dates | [optional] 
**item_uri** | **str** | Link to the Event | [optional] 
**event_tags** | **str** | Tag(s) representing the event | [optional] 
**event_type** | **str** | Type of the event | [optional] 
**event_website** | **str** | Supplemental URI for the event | [optional] 
**audience** | **str** | Tag(s) representing the intended audience for the event | [optional] 
**cost** | **str** | Cost of the event | [optional] 
**host** | **str** | Event host information | [optional] 
**location_id** | **int** | Unique Id of the location hosting the event | [optional] 
**location_name** | **str** | Display name of the location hosting the event | [optional] 
**updated_date** | **datetime** | Date item last updated | [optional] 
**content** | **str** | Description content for the event, often includes HTML markup | [optional] 

## Example

```python
from openapi_client.models.site_event import SiteEvent

# TODO update the JSON string below
json = "{}"
# create an instance of SiteEvent from a JSON string
site_event_instance = SiteEvent.from_json(json)
# print the JSON string representation of the object
print SiteEvent.to_json()

# convert the object into a dict
site_event_dict = site_event_instance.to_dict()
# create an instance of SiteEvent from a dict
site_event_form_dict = site_event.from_dict(site_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


