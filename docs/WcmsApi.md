# openapi_client.WcmsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v3_wcms_get**](WcmsApi.md#v3_wcms_get) | **GET** /v3/Wcms | Retrieves information about all active and published WCMS sites
[**v3_wcms_id_events_get**](WcmsApi.md#v3_wcms_id_events_get) | **GET** /v3/Wcms/{id}/events | Retrieves all event items for a specific WCMS site by Site Id
[**v3_wcms_id_get**](WcmsApi.md#v3_wcms_id_get) | **GET** /v3/Wcms/{id} | Retrieves information about a specific WCMS site by Site Id
[**v3_wcms_id_news_get**](WcmsApi.md#v3_wcms_id_news_get) | **GET** /v3/Wcms/{id}/news | Retrieves all news items for a specific WCMS site by Site Id
[**v3_wcms_id_opportunities_get**](WcmsApi.md#v3_wcms_id_opportunities_get) | **GET** /v3/Wcms/{id}/opportunities | Retrieves all opportunity items for a specific WCMS site by Site Id
[**v3_wcms_id_posts_get**](WcmsApi.md#v3_wcms_id_posts_get) | **GET** /v3/Wcms/{id}/posts | Retrieves all blog post items for a specific WCMS site by Site Id
[**v3_wcms_latestevents_max_items_get**](WcmsApi.md#v3_wcms_latestevents_max_items_get) | **GET** /v3/Wcms/latestevents/{maxItems} | Retrieves the latest events items across all WCMS sites, ordered by event start date
[**v3_wcms_latestnews_max_items_get**](WcmsApi.md#v3_wcms_latestnews_max_items_get) | **GET** /v3/Wcms/latestnews/{maxItems} | Retrieves the latest news items across all WCMS sites, ordered by posted date
[**v3_wcms_latestopportunities_max_items_get**](WcmsApi.md#v3_wcms_latestopportunities_max_items_get) | **GET** /v3/Wcms/latestopportunities/{maxItems} | Retrieves the latest opportunity items across all WCMS sites, ordered by posted/open date
[**v3_wcms_latestposts_max_items_get**](WcmsApi.md#v3_wcms_latestposts_max_items_get) | **GET** /v3/Wcms/latestposts/{maxItems} | Retrieves the latest blog post items across all WCMS sites, ordered by posted date


# **v3_wcms_get**
> List[Site] v3_wcms_get()

Retrieves information about all active and published WCMS sites

### Example

* Api Key Authentication (apiKey):

```python
import time
import os
import openapi_client
from openapi_client.models.site import Site
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.WcmsApi(api_client)

    try:
        # Retrieves information about all active and published WCMS sites
        api_response = api_instance.v3_wcms_get()
        print("The response of WcmsApi->v3_wcms_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WcmsApi->v3_wcms_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Site]**](Site.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_wcms_id_events_get**
> List[SiteEvent] v3_wcms_id_events_get(id, max_items=max_items, newest_first=newest_first)

Retrieves all event items for a specific WCMS site by Site Id

### Example

* Api Key Authentication (apiKey):

```python
import time
import os
import openapi_client
from openapi_client.models.site_event import SiteEvent
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.WcmsApi(api_client)
    id = 56 # int | Unique Id for the Site
    max_items = 56 # int | (Optional) Maximum amount of items to retrieve (optional)
    newest_first = True # bool | (Optional) Requires maxItems parameter, sorts items by created date, newest first (optional)

    try:
        # Retrieves all event items for a specific WCMS site by Site Id
        api_response = api_instance.v3_wcms_id_events_get(id, max_items=max_items, newest_first=newest_first)
        print("The response of WcmsApi->v3_wcms_id_events_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WcmsApi->v3_wcms_id_events_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Unique Id for the Site | 
 **max_items** | **int**| (Optional) Maximum amount of items to retrieve | [optional] 
 **newest_first** | **bool**| (Optional) Requires maxItems parameter, sorts items by created date, newest first | [optional] 

### Return type

[**List[SiteEvent]**](SiteEvent.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_wcms_id_get**
> Site v3_wcms_id_get(id)

Retrieves information about a specific WCMS site by Site Id

### Example

* Api Key Authentication (apiKey):

```python
import time
import os
import openapi_client
from openapi_client.models.site import Site
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.WcmsApi(api_client)
    id = 56 # int | Unique site Id

    try:
        # Retrieves information about a specific WCMS site by Site Id
        api_response = api_instance.v3_wcms_id_get(id)
        print("The response of WcmsApi->v3_wcms_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WcmsApi->v3_wcms_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Unique site Id | 

### Return type

[**Site**](Site.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_wcms_id_news_get**
> List[SiteNews] v3_wcms_id_news_get(id, max_items=max_items, newest_first=newest_first)

Retrieves all news items for a specific WCMS site by Site Id

### Example

* Api Key Authentication (apiKey):

```python
import time
import os
import openapi_client
from openapi_client.models.site_news import SiteNews
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.WcmsApi(api_client)
    id = 56 # int | Unique Id for the Site
    max_items = 56 # int | (Optional) Maximum amount of items to retrieve (optional)
    newest_first = True # bool | (Optional) Requires maxItems parameter, sorts items by created date, newest first (optional)

    try:
        # Retrieves all news items for a specific WCMS site by Site Id
        api_response = api_instance.v3_wcms_id_news_get(id, max_items=max_items, newest_first=newest_first)
        print("The response of WcmsApi->v3_wcms_id_news_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WcmsApi->v3_wcms_id_news_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Unique Id for the Site | 
 **max_items** | **int**| (Optional) Maximum amount of items to retrieve | [optional] 
 **newest_first** | **bool**| (Optional) Requires maxItems parameter, sorts items by created date, newest first | [optional] 

### Return type

[**List[SiteNews]**](SiteNews.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_wcms_id_opportunities_get**
> List[SiteOpportunity] v3_wcms_id_opportunities_get(id, max_items=max_items, newest_first=newest_first)

Retrieves all opportunity items for a specific WCMS site by Site Id

### Example

* Api Key Authentication (apiKey):

```python
import time
import os
import openapi_client
from openapi_client.models.site_opportunity import SiteOpportunity
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.WcmsApi(api_client)
    id = 56 # int | Unique Id for the Site
    max_items = 56 # int | (Optional) Maximum amount of items to retrieve (optional)
    newest_first = True # bool | (Optional) Requires maxItems parameter, sorts items by created date, newest first (optional)

    try:
        # Retrieves all opportunity items for a specific WCMS site by Site Id
        api_response = api_instance.v3_wcms_id_opportunities_get(id, max_items=max_items, newest_first=newest_first)
        print("The response of WcmsApi->v3_wcms_id_opportunities_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WcmsApi->v3_wcms_id_opportunities_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Unique Id for the Site | 
 **max_items** | **int**| (Optional) Maximum amount of items to retrieve | [optional] 
 **newest_first** | **bool**| (Optional) Requires maxItems parameter, sorts items by created date, newest first | [optional] 

### Return type

[**List[SiteOpportunity]**](SiteOpportunity.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_wcms_id_posts_get**
> List[SiteBlogPost] v3_wcms_id_posts_get(id, max_items=max_items, newest_first=newest_first)

Retrieves all blog post items for a specific WCMS site by Site Id

### Example

* Api Key Authentication (apiKey):

```python
import time
import os
import openapi_client
from openapi_client.models.site_blog_post import SiteBlogPost
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.WcmsApi(api_client)
    id = 56 # int | Unique Id for the Site
    max_items = 56 # int | (Optional) Maximum amount of items to retrieve (optional)
    newest_first = True # bool | (Optional) Requires maxItems parameter, sorts items by created date, newest first (optional)

    try:
        # Retrieves all blog post items for a specific WCMS site by Site Id
        api_response = api_instance.v3_wcms_id_posts_get(id, max_items=max_items, newest_first=newest_first)
        print("The response of WcmsApi->v3_wcms_id_posts_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WcmsApi->v3_wcms_id_posts_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Unique Id for the Site | 
 **max_items** | **int**| (Optional) Maximum amount of items to retrieve | [optional] 
 **newest_first** | **bool**| (Optional) Requires maxItems parameter, sorts items by created date, newest first | [optional] 

### Return type

[**List[SiteBlogPost]**](SiteBlogPost.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_wcms_latestevents_max_items_get**
> List[SiteEvent] v3_wcms_latestevents_max_items_get(max_items)

Retrieves the latest events items across all WCMS sites, ordered by event start date

### Example

* Api Key Authentication (apiKey):

```python
import time
import os
import openapi_client
from openapi_client.models.site_event import SiteEvent
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.WcmsApi(api_client)
    max_items = 15 # int | Number of items to retrieve, default 15, maximum 25 (default to 15)

    try:
        # Retrieves the latest events items across all WCMS sites, ordered by event start date
        api_response = api_instance.v3_wcms_latestevents_max_items_get(max_items)
        print("The response of WcmsApi->v3_wcms_latestevents_max_items_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WcmsApi->v3_wcms_latestevents_max_items_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **max_items** | **int**| Number of items to retrieve, default 15, maximum 25 | [default to 15]

### Return type

[**List[SiteEvent]**](SiteEvent.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_wcms_latestnews_max_items_get**
> List[SiteNews] v3_wcms_latestnews_max_items_get(max_items)

Retrieves the latest news items across all WCMS sites, ordered by posted date

### Example

* Api Key Authentication (apiKey):

```python
import time
import os
import openapi_client
from openapi_client.models.site_news import SiteNews
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.WcmsApi(api_client)
    max_items = 15 # int | Number of items to retrieve, default 15, maximum 25 (default to 15)

    try:
        # Retrieves the latest news items across all WCMS sites, ordered by posted date
        api_response = api_instance.v3_wcms_latestnews_max_items_get(max_items)
        print("The response of WcmsApi->v3_wcms_latestnews_max_items_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WcmsApi->v3_wcms_latestnews_max_items_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **max_items** | **int**| Number of items to retrieve, default 15, maximum 25 | [default to 15]

### Return type

[**List[SiteNews]**](SiteNews.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_wcms_latestopportunities_max_items_get**
> List[SiteOpportunity] v3_wcms_latestopportunities_max_items_get(max_items)

Retrieves the latest opportunity items across all WCMS sites, ordered by posted/open date

### Example

* Api Key Authentication (apiKey):

```python
import time
import os
import openapi_client
from openapi_client.models.site_opportunity import SiteOpportunity
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.WcmsApi(api_client)
    max_items = 15 # int | Number of items to retrieve, default 15, maximum 25 (default to 15)

    try:
        # Retrieves the latest opportunity items across all WCMS sites, ordered by posted/open date
        api_response = api_instance.v3_wcms_latestopportunities_max_items_get(max_items)
        print("The response of WcmsApi->v3_wcms_latestopportunities_max_items_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WcmsApi->v3_wcms_latestopportunities_max_items_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **max_items** | **int**| Number of items to retrieve, default 15, maximum 25 | [default to 15]

### Return type

[**List[SiteOpportunity]**](SiteOpportunity.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_wcms_latestposts_max_items_get**
> List[SiteBlogPost] v3_wcms_latestposts_max_items_get(max_items)

Retrieves the latest blog post items across all WCMS sites, ordered by posted date

### Example

* Api Key Authentication (apiKey):

```python
import time
import os
import openapi_client
from openapi_client.models.site_blog_post import SiteBlogPost
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.WcmsApi(api_client)
    max_items = 15 # int | Number of items to retrieve, default 15, maximum 25 (default to 15)

    try:
        # Retrieves the latest blog post items across all WCMS sites, ordered by posted date
        api_response = api_instance.v3_wcms_latestposts_max_items_get(max_items)
        print("The response of WcmsApi->v3_wcms_latestposts_max_items_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WcmsApi->v3_wcms_latestposts_max_items_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **max_items** | **int**| Number of items to retrieve, default 15, maximum 25 | [default to 15]

### Return type

[**List[SiteBlogPost]**](SiteBlogPost.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

