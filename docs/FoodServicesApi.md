# openapi_client.FoodServicesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v3_food_services_franchises_get**](FoodServicesApi.md#v3_food_services_franchises_get) | **GET** /v3/FoodServices/franchises | Get all food service Franchise data
[**v3_food_services_franchises_id_get**](FoodServicesApi.md#v3_food_services_franchises_id_get) | **GET** /v3/FoodServices/franchises/{id} | Get specific food sercices Franchise data by Id
[**v3_food_services_franchises_name_get**](FoodServicesApi.md#v3_food_services_franchises_name_get) | **GET** /v3/FoodServices/franchises/{name} | Get specific food services Franchise data by Franchise name
[**v3_food_services_outlets_get**](FoodServicesApi.md#v3_food_services_outlets_get) | **GET** /v3/FoodServices/outlets | Get all food service Outlet data
[**v3_food_services_outlets_id_get**](FoodServicesApi.md#v3_food_services_outlets_id_get) | **GET** /v3/FoodServices/outlets/{id} | Get specific food services Outlet data by Id
[**v3_food_services_outlets_name_get**](FoodServicesApi.md#v3_food_services_outlets_name_get) | **GET** /v3/FoodServices/outlets/{name} | Get specific food services Outlet data by Outlet name


# **v3_food_services_franchises_get**
> FoodServicesFranchises v3_food_services_franchises_get()

Get all food service Franchise data

### Example

* Api Key Authentication (apiKey):

```python
import time
import os
import openapi_client
from openapi_client.models.food_services_franchises import FoodServicesFranchises
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
    api_instance = openapi_client.FoodServicesApi(api_client)

    try:
        # Get all food service Franchise data
        api_response = api_instance.v3_food_services_franchises_get()
        print("The response of FoodServicesApi->v3_food_services_franchises_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoodServicesApi->v3_food_services_franchises_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**FoodServicesFranchises**](FoodServicesFranchises.md)

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

# **v3_food_services_franchises_id_get**
> FoodServicesFranchise v3_food_services_franchises_id_get(id)

Get specific food sercices Franchise data by Id

### Example

* Api Key Authentication (apiKey):

```python
import time
import os
import openapi_client
from openapi_client.models.food_services_franchise import FoodServicesFranchise
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
    api_instance = openapi_client.FoodServicesApi(api_client)
    id = 56 # int | WCMS object ID representing the Franchise

    try:
        # Get specific food sercices Franchise data by Id
        api_response = api_instance.v3_food_services_franchises_id_get(id)
        print("The response of FoodServicesApi->v3_food_services_franchises_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoodServicesApi->v3_food_services_franchises_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| WCMS object ID representing the Franchise | 

### Return type

[**FoodServicesFranchise**](FoodServicesFranchise.md)

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

# **v3_food_services_franchises_name_get**
> FoodServicesFranchise v3_food_services_franchises_name_get(name)

Get specific food services Franchise data by Franchise name

### Example

* Api Key Authentication (apiKey):

```python
import time
import os
import openapi_client
from openapi_client.models.food_services_franchise import FoodServicesFranchise
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
    api_instance = openapi_client.FoodServicesApi(api_client)
    name = 'name_example' # str | Name to filter Franchise by

    try:
        # Get specific food services Franchise data by Franchise name
        api_response = api_instance.v3_food_services_franchises_name_get(name)
        print("The response of FoodServicesApi->v3_food_services_franchises_name_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoodServicesApi->v3_food_services_franchises_name_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name to filter Franchise by | 

### Return type

[**FoodServicesFranchise**](FoodServicesFranchise.md)

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

# **v3_food_services_outlets_get**
> FoodServicesOutlets v3_food_services_outlets_get()

Get all food service Outlet data

### Example

* Api Key Authentication (apiKey):

```python
import time
import os
import openapi_client
from openapi_client.models.food_services_outlets import FoodServicesOutlets
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
    api_instance = openapi_client.FoodServicesApi(api_client)

    try:
        # Get all food service Outlet data
        api_response = api_instance.v3_food_services_outlets_get()
        print("The response of FoodServicesApi->v3_food_services_outlets_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoodServicesApi->v3_food_services_outlets_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**FoodServicesOutlets**](FoodServicesOutlets.md)

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

# **v3_food_services_outlets_id_get**
> FoodServicesOutlet v3_food_services_outlets_id_get(id)

Get specific food services Outlet data by Id

### Example

* Api Key Authentication (apiKey):

```python
import time
import os
import openapi_client
from openapi_client.models.food_services_outlet import FoodServicesOutlet
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
    api_instance = openapi_client.FoodServicesApi(api_client)
    id = 56 # int | WCMS object ID representing the Outlet

    try:
        # Get specific food services Outlet data by Id
        api_response = api_instance.v3_food_services_outlets_id_get(id)
        print("The response of FoodServicesApi->v3_food_services_outlets_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoodServicesApi->v3_food_services_outlets_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| WCMS object ID representing the Outlet | 

### Return type

[**FoodServicesOutlet**](FoodServicesOutlet.md)

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

# **v3_food_services_outlets_name_get**
> FoodServicesOutlet v3_food_services_outlets_name_get(name)

Get specific food services Outlet data by Outlet name

### Example

* Api Key Authentication (apiKey):

```python
import time
import os
import openapi_client
from openapi_client.models.food_services_outlet import FoodServicesOutlet
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
    api_instance = openapi_client.FoodServicesApi(api_client)
    name = 'name_example' # str | Name to filter Outlet by

    try:
        # Get specific food services Outlet data by Outlet name
        api_response = api_instance.v3_food_services_outlets_name_get(name)
        print("The response of FoodServicesApi->v3_food_services_outlets_name_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoodServicesApi->v3_food_services_outlets_name_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name to filter Outlet by | 

### Return type

[**FoodServicesOutlet**](FoodServicesOutlet.md)

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

