# openapi_client.ExamSchedulesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v3_exam_schedules_code_get**](ExamSchedulesApi.md#v3_exam_schedules_code_get) | **GET** /v3/ExamSchedules/{code} | Returns Exam Schedule data for the requested Term
[**v3_exam_schedules_get**](ExamSchedulesApi.md#v3_exam_schedules_get) | **GET** /v3/ExamSchedules | Returns Exam Schedule data for the current Term


# **v3_exam_schedules_code_get**
> List[Exam] v3_exam_schedules_code_get(code)

Returns Exam Schedule data for the requested Term

### Example

* Api Key Authentication (apiKey):

```python
import time
import os
import openapi_client
from openapi_client.models.exam import Exam
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
    api_instance = openapi_client.ExamSchedulesApi(api_client)
    code = 'code_example' # str | Waterloo Term code

    try:
        # Returns Exam Schedule data for the requested Term
        api_response = api_instance.v3_exam_schedules_code_get(code)
        print("The response of ExamSchedulesApi->v3_exam_schedules_code_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExamSchedulesApi->v3_exam_schedules_code_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| Waterloo Term code | 

### Return type

[**List[Exam]**](Exam.md)

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

# **v3_exam_schedules_get**
> List[Exam] v3_exam_schedules_get()

Returns Exam Schedule data for the current Term

### Example

* Api Key Authentication (apiKey):

```python
import time
import os
import openapi_client
from openapi_client.models.exam import Exam
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
    api_instance = openapi_client.ExamSchedulesApi(api_client)

    try:
        # Returns Exam Schedule data for the current Term
        api_response = api_instance.v3_exam_schedules_get()
        print("The response of ExamSchedulesApi->v3_exam_schedules_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExamSchedulesApi->v3_exam_schedules_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Exam]**](Exam.md)

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

