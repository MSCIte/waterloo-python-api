# LocationGeo

Model representing a Location for the Buildings dataset in GEO JSON format

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type property of GEO JSON collection | [optional] [readonly] 
**features** | [**List[Feature]**](Feature.md) | Features of this collection | [optional] 

## Example

```python
from openapi_client.models.location_geo import LocationGeo

# TODO update the JSON string below
json = "{}"
# create an instance of LocationGeo from a JSON string
location_geo_instance = LocationGeo.from_json(json)
# print the JSON string representation of the object
print LocationGeo.to_json()

# convert the object into a dict
location_geo_dict = location_geo_instance.to_dict()
# create an instance of LocationGeo from a dict
location_geo_form_dict = location_geo.from_dict(location_geo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


