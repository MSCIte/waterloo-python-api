# openapi_client.LocationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v3_locations_geojson_get**](LocationsApi.md#v3_locations_geojson_get) | **GET** /v3/Locations/geojson | Get all building location data as GEO JSON
[**v3_locations_get**](LocationsApi.md#v3_locations_get) | **GET** /v3/Locations | Get all building location data
[**v3_locations_location_code_geojson_get**](LocationsApi.md#v3_locations_location_code_geojson_get) | **GET** /v3/Locations/{locationCode}/geojson | Gets building by matched building code, case insensitive, as GEO JSON
[**v3_locations_location_code_get**](LocationsApi.md#v3_locations_location_code_get) | **GET** /v3/Locations/{locationCode} | Gets building by matched building code, case insensitive
[**v3_locations_search_location_name_geojson_get**](LocationsApi.md#v3_locations_search_location_name_geojson_get) | **GET** /v3/Locations/search/{locationName}/geojson | Gets buildings by matched building name, contains, case insensitive, as GEO JSON
[**v3_locations_search_location_name_get**](LocationsApi.md#v3_locations_search_location_name_get) | **GET** /v3/Locations/search/{locationName} | Gets buildings by matched building name, contains, case insensitive


# **v3_locations_geojson_get**
> LocationGeo v3_locations_geojson_get()

Get all building location data as GEO JSON

### Example

* Api Key Authentication (apiKey):

```python
import time
import os
import openapi_client
from openapi_client.models.location_geo import LocationGeo
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
    api_instance = openapi_client.LocationsApi(api_client)

    try:
        # Get all building location data as GEO JSON
        api_response = api_instance.v3_locations_geojson_get()
        print("The response of LocationsApi->v3_locations_geojson_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocationsApi->v3_locations_geojson_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**LocationGeo**](LocationGeo.md)

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

# **v3_locations_get**
> List[Location] v3_locations_get()

Get all building location data

### Example

* Api Key Authentication (apiKey):

```python
import time
import os
import openapi_client
from openapi_client.models.location import Location
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
    api_instance = openapi_client.LocationsApi(api_client)

    try:
        # Get all building location data
        api_response = api_instance.v3_locations_get()
        print("The response of LocationsApi->v3_locations_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocationsApi->v3_locations_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Location]**](Location.md)

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

# **v3_locations_location_code_geojson_get**
> LocationGeo v3_locations_location_code_geojson_get(location_code)

Gets building by matched building code, case insensitive, as GEO JSON

### Example

* Api Key Authentication (apiKey):

```python
import time
import os
import openapi_client
from openapi_client.models.location_geo import LocationGeo
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
    api_instance = openapi_client.LocationsApi(api_client)
    location_code = 'location_code_example' # str | Building code to match

    try:
        # Gets building by matched building code, case insensitive, as GEO JSON
        api_response = api_instance.v3_locations_location_code_geojson_get(location_code)
        print("The response of LocationsApi->v3_locations_location_code_geojson_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocationsApi->v3_locations_location_code_geojson_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_code** | **str**| Building code to match | 

### Return type

[**LocationGeo**](LocationGeo.md)

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

# **v3_locations_location_code_get**
> Location v3_locations_location_code_get(location_code)

Gets building by matched building code, case insensitive

### Example

* Api Key Authentication (apiKey):

```python
import time
import os
import openapi_client
from openapi_client.models.location import Location
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
    api_instance = openapi_client.LocationsApi(api_client)
    location_code = 'location_code_example' # str | Building code to match

    try:
        # Gets building by matched building code, case insensitive
        api_response = api_instance.v3_locations_location_code_get(location_code)
        print("The response of LocationsApi->v3_locations_location_code_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocationsApi->v3_locations_location_code_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_code** | **str**| Building code to match | 

### Return type

[**Location**](Location.md)

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

# **v3_locations_search_location_name_geojson_get**
> LocationGeo v3_locations_search_location_name_geojson_get(location_name)

Gets buildings by matched building name, contains, case insensitive, as GEO JSON

### Example

* Api Key Authentication (apiKey):

```python
import time
import os
import openapi_client
from openapi_client.models.location_geo import LocationGeo
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
    api_instance = openapi_client.LocationsApi(api_client)
    location_name = 'location_name_example' # str | Text to match in building name

    try:
        # Gets buildings by matched building name, contains, case insensitive, as GEO JSON
        api_response = api_instance.v3_locations_search_location_name_geojson_get(location_name)
        print("The response of LocationsApi->v3_locations_search_location_name_geojson_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocationsApi->v3_locations_search_location_name_geojson_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_name** | **str**| Text to match in building name | 

### Return type

[**LocationGeo**](LocationGeo.md)

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

# **v3_locations_search_location_name_get**
> List[Location] v3_locations_search_location_name_get(location_name)

Gets buildings by matched building name, contains, case insensitive

### Example

* Api Key Authentication (apiKey):

```python
import time
import os
import openapi_client
from openapi_client.models.location import Location
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
    api_instance = openapi_client.LocationsApi(api_client)
    location_name = 'location_name_example' # str | Text to match in building name

    try:
        # Gets buildings by matched building name, contains, case insensitive
        api_response = api_instance.v3_locations_search_location_name_get(location_name)
        print("The response of LocationsApi->v3_locations_search_location_name_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocationsApi->v3_locations_search_location_name_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_name** | **str**| Text to match in building name | 

### Return type

[**List[Location]**](Location.md)

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

