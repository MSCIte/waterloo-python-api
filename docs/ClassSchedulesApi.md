# openapi_client.ClassSchedulesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v3_class_schedules_term_code_course_id_get**](ClassSchedulesApi.md#v3_class_schedules_term_code_course_id_get) | **GET** /v3/ClassSchedules/{termCode}/{courseId} | Get Class data for a scheduled Course by Course ID, in a specific Term
[**v3_class_schedules_term_code_get**](ClassSchedulesApi.md#v3_class_schedules_term_code_get) | **GET** /v3/ClassSchedules/{termCode} | Get the Course IDs that have one or more active and associated schedules in the given Term
[**v3_class_schedules_term_code_subject_catalog_number_get**](ClassSchedulesApi.md#v3_class_schedules_term_code_subject_catalog_number_get) | **GET** /v3/ClassSchedules/{termCode}/{subject}/{catalogNumber} | Get Class data for a scheduled Course by Subject and catalog number, in a specific Term


# **v3_class_schedules_term_code_course_id_get**
> List[ModelClass] v3_class_schedules_term_code_course_id_get(term_code, course_id)

Get Class data for a scheduled Course by Course ID, in a specific Term

### Example

* Api Key Authentication (apiKey):

```python
import time
import os
import openapi_client
from openapi_client.models.model_class import ModelClass
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
    api_instance = openapi_client.ClassSchedulesApi(api_client)
    term_code = 'term_code_example' # str | Waterloo Term code to filter on
    course_id = 56 # int | Course ID to filter on

    try:
        # Get Class data for a scheduled Course by Course ID, in a specific Term
        api_response = api_instance.v3_class_schedules_term_code_course_id_get(term_code, course_id)
        print("The response of ClassSchedulesApi->v3_class_schedules_term_code_course_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClassSchedulesApi->v3_class_schedules_term_code_course_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term_code** | **str**| Waterloo Term code to filter on | 
 **course_id** | **int**| Course ID to filter on | 

### Return type

[**List[ModelClass]**](ModelClass.md)

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

# **v3_class_schedules_term_code_get**
> List[str] v3_class_schedules_term_code_get(term_code)

Get the Course IDs that have one or more active and associated schedules in the given Term

### Example

* Api Key Authentication (apiKey):

```python
import time
import os
import openapi_client
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
    api_instance = openapi_client.ClassSchedulesApi(api_client)
    term_code = 'term_code_example' # str | Waterloo Term code to filter on

    try:
        # Get the Course IDs that have one or more active and associated schedules in the given Term
        api_response = api_instance.v3_class_schedules_term_code_get(term_code)
        print("The response of ClassSchedulesApi->v3_class_schedules_term_code_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClassSchedulesApi->v3_class_schedules_term_code_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term_code** | **str**| Waterloo Term code to filter on | 

### Return type

**List[str]**

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

# **v3_class_schedules_term_code_subject_catalog_number_get**
> List[ModelClass] v3_class_schedules_term_code_subject_catalog_number_get(term_code, subject, catalog_number)

Get Class data for a scheduled Course by Subject and catalog number, in a specific Term

### Example

* Api Key Authentication (apiKey):

```python
import time
import os
import openapi_client
from openapi_client.models.model_class import ModelClass
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
    api_instance = openapi_client.ClassSchedulesApi(api_client)
    term_code = 'term_code_example' # str | Waterloo Term code to filter on
    subject = 'subject_example' # str | Academic Subject code to filter ron
    catalog_number = 'catalog_number_example' # str | Catalog number to filter on

    try:
        # Get Class data for a scheduled Course by Subject and catalog number, in a specific Term
        api_response = api_instance.v3_class_schedules_term_code_subject_catalog_number_get(term_code, subject, catalog_number)
        print("The response of ClassSchedulesApi->v3_class_schedules_term_code_subject_catalog_number_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClassSchedulesApi->v3_class_schedules_term_code_subject_catalog_number_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term_code** | **str**| Waterloo Term code to filter on | 
 **subject** | **str**| Academic Subject code to filter ron | 
 **catalog_number** | **str**| Catalog number to filter on | 

### Return type

[**List[ModelClass]**](ModelClass.md)

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

