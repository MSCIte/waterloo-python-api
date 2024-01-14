# openapi_client.ImportantDatesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v3_important_dates_get**](ImportantDatesApi.md#v3_important_dates_get) | **GET** /v3/ImportantDates | Returns all current data for Important Dates


# **v3_important_dates_get**
> List[ImportantDate] v3_important_dates_get()

Returns all current data for Important Dates

### Example

* Api Key Authentication (apiKey):

```python
import time
import os
import openapi_client
from openapi_client.models.important_date import ImportantDate
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
    api_instance = openapi_client.ImportantDatesApi(api_client)

    try:
        # Returns all current data for Important Dates
        api_response = api_instance.v3_important_dates_get()
        print("The response of ImportantDatesApi->v3_important_dates_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportantDatesApi->v3_important_dates_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ImportantDate]**](ImportantDate.md)

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

