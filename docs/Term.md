# Term

An academic Term at Waterloo, a defined period of time that is used by classes and similar

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**term_code** | **str** | Code that describes this Term | [optional] 
**name** | **str** | The Name for this Term, most often the displayed name | [optional] 
**name_short** | **str** | The short form name for this Term | [optional] 
**term_begin_date** | **datetime** | The date and time from which the Term begins, inclusive | [optional] 
**term_end_date** | **datetime** | The date and time on which the Term ends, inclusive | [optional] 
**sixty_percent_complete_date** | **datetime** | The date and time at which the term is 60% complete, used for standing, withdrawal, and penalties | [optional] 
**associated_academic_year** | **int** | The academic year to which this Term belongs | [optional] 

## Example

```python
from openapi_client.models.term import Term

# TODO update the JSON string below
json = "{}"
# create an instance of Term from a JSON string
term_instance = Term.from_json(json)
# print the JSON string representation of the object
print Term.to_json()

# convert the object into a dict
term_dict = term_instance.to_dict()
# create an instance of Term from a dict
term_form_dict = term.from_dict(term_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


