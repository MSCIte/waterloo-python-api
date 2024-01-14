# openapi_client.TermsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v3_terms_code_get**](TermsApi.md#v3_terms_code_get) | **GET** /v3/Terms/{code} | Gets Term data for a specific Term filtered by code
[**v3_terms_current_get**](TermsApi.md#v3_terms_current_get) | **GET** /v3/Terms/current | Gets the current Term data
[**v3_terms_foracademicyear_year_get**](TermsApi.md#v3_terms_foracademicyear_year_get) | **GET** /v3/Terms/foracademicyear/{year} | Gets Term data for terms that are part of a specific academic year
[**v3_terms_get**](TermsApi.md#v3_terms_get) | **GET** /v3/Terms | Gets all Term data that is effective at the current time


# **v3_terms_code_get**
> Term v3_terms_code_get(code)

Gets Term data for a specific Term filtered by code

### Example

* Api Key Authentication (apiKey):

```python
import time
import os
import openapi_client
from openapi_client.models.term import Term
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
    api_instance = openapi_client.TermsApi(api_client)
    code = 'code_example' # str | Term 4 digit Code

    try:
        # Gets Term data for a specific Term filtered by code
        api_response = api_instance.v3_terms_code_get(code)
        print("The response of TermsApi->v3_terms_code_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TermsApi->v3_terms_code_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| Term 4 digit Code | 

### Return type

[**Term**](Term.md)

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

# **v3_terms_current_get**
> Term v3_terms_current_get()

Gets the current Term data

### Example

* Api Key Authentication (apiKey):

```python
import time
import os
import openapi_client
from openapi_client.models.term import Term
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
    api_instance = openapi_client.TermsApi(api_client)

    try:
        # Gets the current Term data
        api_response = api_instance.v3_terms_current_get()
        print("The response of TermsApi->v3_terms_current_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TermsApi->v3_terms_current_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Term**](Term.md)

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

# **v3_terms_foracademicyear_year_get**
> List[Term] v3_terms_foracademicyear_year_get(year)

Gets Term data for terms that are part of a specific academic year

### Example

* Api Key Authentication (apiKey):

```python
import time
import os
import openapi_client
from openapi_client.models.term import Term
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
    api_instance = openapi_client.TermsApi(api_client)
    year = 56 # int | Academic year associated to Terms

    try:
        # Gets Term data for terms that are part of a specific academic year
        api_response = api_instance.v3_terms_foracademicyear_year_get(year)
        print("The response of TermsApi->v3_terms_foracademicyear_year_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TermsApi->v3_terms_foracademicyear_year_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Academic year associated to Terms | 

### Return type

[**List[Term]**](Term.md)

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

# **v3_terms_get**
> List[Term] v3_terms_get()

Gets all Term data that is effective at the current time

### Example

* Api Key Authentication (apiKey):

```python
import time
import os
import openapi_client
from openapi_client.models.term import Term
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
    api_instance = openapi_client.TermsApi(api_client)

    try:
        # Gets all Term data that is effective at the current time
        api_response = api_instance.v3_terms_get()
        print("The response of TermsApi->v3_terms_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TermsApi->v3_terms_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Term]**](Term.md)

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

