# openapi_client.CoursesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v3_courses_term_code_course_id_get**](CoursesApi.md#v3_courses_term_code_course_id_get) | **GET** /v3/Courses/{termCode}/{courseId} | Get Course catalog data filtered by Term and Course ID, multiple Courses are usually cross listed
[**v3_courses_term_code_course_id_offer_number_get**](CoursesApi.md#v3_courses_term_code_course_id_offer_number_get) | **GET** /v3/Courses/{termCode}/{courseId}/{offerNumber} | Get Course catalog data filtered by Term, Course ID, and offer number
[**v3_courses_term_code_get**](CoursesApi.md#v3_courses_term_code_get) | **GET** /v3/Courses/{termCode} | Get all Course data for a Term
[**v3_courses_term_code_subject_catalog_number_get**](CoursesApi.md#v3_courses_term_code_subject_catalog_number_get) | **GET** /v3/Courses/{termCode}/{subject}/{catalogNumber} | Get Course catalog data filtered by Term, Subject, and catalog number
[**v3_courses_term_code_subject_get**](CoursesApi.md#v3_courses_term_code_subject_get) | **GET** /v3/Courses/{termCode}/{subject} | Get Course catalog data filtered by Term and Subject code


# **v3_courses_term_code_course_id_get**
> List[Course] v3_courses_term_code_course_id_get(term_code, course_id)

Get Course catalog data filtered by Term and Course ID, multiple Courses are usually cross listed

### Example

* Api Key Authentication (apiKey):

```python
import time
import os
import openapi_client
from openapi_client.models.course import Course
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
    api_instance = openapi_client.CoursesApi(api_client)
    term_code = 'term_code_example' # str | Term code to filter on
    course_id = 56 # int | Course ID to filter on

    try:
        # Get Course catalog data filtered by Term and Course ID, multiple Courses are usually cross listed
        api_response = api_instance.v3_courses_term_code_course_id_get(term_code, course_id)
        print("The response of CoursesApi->v3_courses_term_code_course_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoursesApi->v3_courses_term_code_course_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term_code** | **str**| Term code to filter on | 
 **course_id** | **int**| Course ID to filter on | 

### Return type

[**List[Course]**](Course.md)

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

# **v3_courses_term_code_course_id_offer_number_get**
> Course v3_courses_term_code_course_id_offer_number_get(term_code, course_id, offer_number)

Get Course catalog data filtered by Term, Course ID, and offer number

### Example

* Api Key Authentication (apiKey):

```python
import time
import os
import openapi_client
from openapi_client.models.course import Course
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
    api_instance = openapi_client.CoursesApi(api_client)
    term_code = 'term_code_example' # str | Term code to filter on
    course_id = 56 # int | Course ID to filter on
    offer_number = 56 # int | Offer number to filter on

    try:
        # Get Course catalog data filtered by Term, Course ID, and offer number
        api_response = api_instance.v3_courses_term_code_course_id_offer_number_get(term_code, course_id, offer_number)
        print("The response of CoursesApi->v3_courses_term_code_course_id_offer_number_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoursesApi->v3_courses_term_code_course_id_offer_number_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term_code** | **str**| Term code to filter on | 
 **course_id** | **int**| Course ID to filter on | 
 **offer_number** | **int**| Offer number to filter on | 

### Return type

[**Course**](Course.md)

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

# **v3_courses_term_code_get**
> List[Course] v3_courses_term_code_get(term_code)

Get all Course data for a Term

### Example

* Api Key Authentication (apiKey):

```python
import time
import os
import openapi_client
from openapi_client.models.course import Course
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
    api_instance = openapi_client.CoursesApi(api_client)
    term_code = 'term_code_example' # str | 

    try:
        # Get all Course data for a Term
        api_response = api_instance.v3_courses_term_code_get(term_code)
        print("The response of CoursesApi->v3_courses_term_code_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoursesApi->v3_courses_term_code_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term_code** | **str**|  | 

### Return type

[**List[Course]**](Course.md)

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

# **v3_courses_term_code_subject_catalog_number_get**
> Course v3_courses_term_code_subject_catalog_number_get(term_code, subject, catalog_number)

Get Course catalog data filtered by Term, Subject, and catalog number

### Example

* Api Key Authentication (apiKey):

```python
import time
import os
import openapi_client
from openapi_client.models.course import Course
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
    api_instance = openapi_client.CoursesApi(api_client)
    term_code = 'term_code_example' # str | Term code to filter on
    subject = 'subject_example' # str | Academic Subject code to filter on
    catalog_number = 'catalog_number_example' # str | Course catalog number to filter on, ie: 101, 111W, 239

    try:
        # Get Course catalog data filtered by Term, Subject, and catalog number
        api_response = api_instance.v3_courses_term_code_subject_catalog_number_get(term_code, subject, catalog_number)
        print("The response of CoursesApi->v3_courses_term_code_subject_catalog_number_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoursesApi->v3_courses_term_code_subject_catalog_number_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term_code** | **str**| Term code to filter on | 
 **subject** | **str**| Academic Subject code to filter on | 
 **catalog_number** | **str**| Course catalog number to filter on, ie: 101, 111W, 239 | 

### Return type

[**Course**](Course.md)

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

# **v3_courses_term_code_subject_get**
> List[Course] v3_courses_term_code_subject_get(term_code, subject)

Get Course catalog data filtered by Term and Subject code

### Example

* Api Key Authentication (apiKey):

```python
import time
import os
import openapi_client
from openapi_client.models.course import Course
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
    api_instance = openapi_client.CoursesApi(api_client)
    term_code = 'term_code_example' # str | Term code to filter on
    subject = 'subject_example' # str | Academic Subject code to filter on

    try:
        # Get Course catalog data filtered by Term and Subject code
        api_response = api_instance.v3_courses_term_code_subject_get(term_code, subject)
        print("The response of CoursesApi->v3_courses_term_code_subject_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoursesApi->v3_courses_term_code_subject_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term_code** | **str**| Term code to filter on | 
 **subject** | **str**| Academic Subject code to filter on | 

### Return type

[**List[Course]**](Course.md)

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

