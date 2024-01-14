# openapi_client.HolidayDatesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v3_holiday_dates_paidholidays_get**](HolidayDatesApi.md#v3_holiday_dates_paidholidays_get) | **GET** /v3/HolidayDates/paidholidays | Retrieves data for all paid holidays as published by Human Resources
[**v3_holiday_dates_paidholidays_ics_get**](HolidayDatesApi.md#v3_holiday_dates_paidholidays_ics_get) | **GET** /v3/HolidayDates/paidholidays/ics | Retrieves data for all paid holidays as published by Human Resources, as an ICS format feed. Allows anonymous access.
[**v3_holiday_dates_paidholidays_year_get**](HolidayDatesApi.md#v3_holiday_dates_paidholidays_year_get) | **GET** /v3/HolidayDates/paidholidays/{year} | Retrieves data for paid holidays associated to the given year as published by Human Resources


# **v3_holiday_dates_paidholidays_get**
> List[PaidHoliday] v3_holiday_dates_paidholidays_get()

Retrieves data for all paid holidays as published by Human Resources

### Example

* Api Key Authentication (apiKey):

```python
import time
import os
import openapi_client
from openapi_client.models.paid_holiday import PaidHoliday
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
    api_instance = openapi_client.HolidayDatesApi(api_client)

    try:
        # Retrieves data for all paid holidays as published by Human Resources
        api_response = api_instance.v3_holiday_dates_paidholidays_get()
        print("The response of HolidayDatesApi->v3_holiday_dates_paidholidays_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HolidayDatesApi->v3_holiday_dates_paidholidays_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[PaidHoliday]**](PaidHoliday.md)

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

# **v3_holiday_dates_paidholidays_ics_get**
> v3_holiday_dates_paidholidays_ics_get()

Retrieves data for all paid holidays as published by Human Resources, as an ICS format feed. Allows anonymous access.

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
    api_instance = openapi_client.HolidayDatesApi(api_client)

    try:
        # Retrieves data for all paid holidays as published by Human Resources, as an ICS format feed. Allows anonymous access.
        api_instance.v3_holiday_dates_paidholidays_ics_get()
    except Exception as e:
        print("Exception when calling HolidayDatesApi->v3_holiday_dates_paidholidays_ics_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_holiday_dates_paidholidays_year_get**
> List[PaidHoliday] v3_holiday_dates_paidholidays_year_get(year)

Retrieves data for paid holidays associated to the given year as published by Human Resources

### Example

* Api Key Authentication (apiKey):

```python
import time
import os
import openapi_client
from openapi_client.models.paid_holiday import PaidHoliday
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
    api_instance = openapi_client.HolidayDatesApi(api_client)
    year = 56 # int | 

    try:
        # Retrieves data for paid holidays associated to the given year as published by Human Resources
        api_response = api_instance.v3_holiday_dates_paidholidays_year_get(year)
        print("The response of HolidayDatesApi->v3_holiday_dates_paidholidays_year_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HolidayDatesApi->v3_holiday_dates_paidholidays_year_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**|  | 

### Return type

[**List[PaidHoliday]**](PaidHoliday.md)

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

