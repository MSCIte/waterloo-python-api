# Location

Model representing a Location for the Buildings dataset

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**building_id** | **str** | Unique identifier for this building | [optional] 
**building_code** | **str** | Alpha-numeric building code | [optional] 
**parent_building_code** | **str** | Unofficial, alpha-numeric building code that represents the parent location | [optional] 
**building_name** | **str** | Display name of the building | [optional] 
**alternate_building_names** | **List[str]** | Unofficial, collection of alternate building display names | [optional] 
**latitude** | **float** | Latitude co-ordinate of this location | [optional] 
**longitude** | **float** | Longitude co-ordinate of this location | [optional] 

## Example

```python
from openapi_client.models.location import Location

# TODO update the JSON string below
json = "{}"
# create an instance of Location from a JSON string
location_instance = Location.from_json(json)
# print the JSON string representation of the object
print Location.to_json()

# convert the object into a dict
location_dict = location_instance.to_dict()
# create an instance of Location from a dict
location_form_dict = location.from_dict(location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


