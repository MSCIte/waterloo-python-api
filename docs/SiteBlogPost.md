# SiteBlogPost

Model representing a WCMS blog post item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**site_id** | **int** | Unique, numeric site ID | [optional] 
**unique_key** | **str** | Unique Id of this post item | [optional] 
**title** | **str** | Title of the blog post | [optional] 
**posted_date** | **datetime** | Content created or posted date | [optional] 
**updated_date** | **datetime** | Content updated date | [optional] 
**item_uri** | **str** | URI to the item in WCMS | [optional] 
**audience** | **str** | Intended audience tag(s) | [optional] 
**content** | **str** | Blog post content, often with HTML markup | [optional] 
**delegated_author_name** | **str** | Display name of the delegated author for this blog post | [optional] 
**delegated_author_uri** | **str** | Link to the WCMS profiel of the delegated author | [optional] 
**publisher_username** | **str** | Username of the person publishing the content, not necessarily the author | [optional] 

## Example

```python
from openapi_client.models.site_blog_post import SiteBlogPost

# TODO update the JSON string below
json = "{}"
# create an instance of SiteBlogPost from a JSON string
site_blog_post_instance = SiteBlogPost.from_json(json)
# print the JSON string representation of the object
print SiteBlogPost.to_json()

# convert the object into a dict
site_blog_post_dict = site_blog_post_instance.to_dict()
# create an instance of SiteBlogPost from a dict
site_blog_post_form_dict = site_blog_post.from_dict(site_blog_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


