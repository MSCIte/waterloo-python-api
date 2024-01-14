# openapi_client.SubjectsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v3_subjects_associatedto_organization_code_get**](SubjectsApi.md#v3_subjects_associatedto_organization_code_get) | **GET** /v3/Subjects/associatedto/{organizationCode} | Gets Subject data for Subjects associated to an Academic Organization by Organization code
[**v3_subjects_code_get**](SubjectsApi.md#v3_subjects_code_get) | **GET** /v3/Subjects/{code} | Gets Subject data filtered by Subject code
[**v3_subjects_get**](SubjectsApi.md#v3_subjects_get) | **GET** /v3/Subjects | Gets all Subject data


# **v3_subjects_associatedto_organization_code_get**
> List[Subject] v3_subjects_associatedto_organization_code_get(organization_code)

Gets Subject data for Subjects associated to an Academic Organization by Organization code

### Example

* Api Key Authentication (apiKey):

```python
import time
import os
import openapi_client
from openapi_client.models.subject import Subject
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
    api_instance = openapi_client.SubjectsApi(api_client)
    organization_code = 'organization_code_example' # str | Academic Organization Code that associates to the Subjects

    try:
        # Gets Subject data for Subjects associated to an Academic Organization by Organization code
        api_response = api_instance.v3_subjects_associatedto_organization_code_get(organization_code)
        print("The response of SubjectsApi->v3_subjects_associatedto_organization_code_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubjectsApi->v3_subjects_associatedto_organization_code_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_code** | **str**| Academic Organization Code that associates to the Subjects | 

### Return type

[**List[Subject]**](Subject.md)

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

# **v3_subjects_code_get**
> Subject v3_subjects_code_get(code)

Gets Subject data filtered by Subject code

### Example

* Api Key Authentication (apiKey):

```python
import time
import os
import openapi_client
from openapi_client.models.subject import Subject
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
    api_instance = openapi_client.SubjectsApi(api_client)
    code = 'code_example' # str | Specific Subject code

    try:
        # Gets Subject data filtered by Subject code
        api_response = api_instance.v3_subjects_code_get(code)
        print("The response of SubjectsApi->v3_subjects_code_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubjectsApi->v3_subjects_code_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| Specific Subject code | 

### Return type

[**Subject**](Subject.md)

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

# **v3_subjects_get**
> List[Subject] v3_subjects_get()

Gets all Subject data

### Example

* Api Key Authentication (apiKey):

```python
import time
import os
import openapi_client
from openapi_client.models.subject import Subject
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
    api_instance = openapi_client.SubjectsApi(api_client)

    try:
        # Gets all Subject data
        api_response = api_instance.v3_subjects_get()
        print("The response of SubjectsApi->v3_subjects_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubjectsApi->v3_subjects_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Subject]**](Subject.md)

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

