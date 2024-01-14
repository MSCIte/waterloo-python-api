# SiteNews

Model representing News data associated to a Site in the WCMS

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**site_id** | **int** | Unique, numeric site ID of the Site this news originates from | [optional] 
**unique_key** | **str** | Unique Id of this news item | [optional] 
**title** | **str** | Title of the news item | [optional] 
**posted_date** | **datetime** | Content created or posted date | [optional] 
**updated_date** | **datetime** | Content updated date | [optional] 
**item_uri** | **str** | URI to the news item in WCMS | [optional] 
**audience** | **str** | Intended audience tag(s) | [optional] 
**content** | **str** | News item content, often with HTML markup | [optional] 

## Example

```python
from openapi_client.models.site_news import SiteNews

# TODO update the JSON string below
json = "{}"
# create an instance of SiteNews from a JSON string
site_news_instance = SiteNews.from_json(json)
# print the JSON string representation of the object
print SiteNews.to_json()

# convert the object into a dict
site_news_dict = site_news_instance.to_dict()
# create an instance of SiteNews from a dict
site_news_form_dict = site_news.from_dict(site_news_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


