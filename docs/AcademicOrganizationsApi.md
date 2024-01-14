# openapi_client.AcademicOrganizationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v3_academic_organizations_get**](AcademicOrganizationsApi.md#v3_academic_organizations_get) | **GET** /v3/AcademicOrganizations | Gets all Academic Organization data
[**v3_academic_organizations_organization_code_get**](AcademicOrganizationsApi.md#v3_academic_organizations_organization_code_get) | **GET** /v3/AcademicOrganizations/{organizationCode} | Gets Academic Organization data for a specific entry by the Organization code


# **v3_academic_organizations_get**
> List[AcademicOrganization] v3_academic_organizations_get()

Gets all Academic Organization data

### Example

* Api Key Authentication (apiKey):

```python
import time
import os
import openapi_client
from openapi_client.models.academic_organization import AcademicOrganization
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
    api_instance = openapi_client.AcademicOrganizationsApi(api_client)

    try:
        # Gets all Academic Organization data
        api_response = api_instance.v3_academic_organizations_get()
        print("The response of AcademicOrganizationsApi->v3_academic_organizations_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AcademicOrganizationsApi->v3_academic_organizations_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[AcademicOrganization]**](AcademicOrganization.md)

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

# **v3_academic_organizations_organization_code_get**
> AcademicOrganization v3_academic_organizations_organization_code_get(organization_code)

Gets Academic Organization data for a specific entry by the Organization code

### Example

* Api Key Authentication (apiKey):

```python
import time
import os
import openapi_client
from openapi_client.models.academic_organization import AcademicOrganization
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
    api_instance = openapi_client.AcademicOrganizationsApi(api_client)
    organization_code = 'organization_code_example' # str | Unique Academic Organization code

    try:
        # Gets Academic Organization data for a specific entry by the Organization code
        api_response = api_instance.v3_academic_organizations_organization_code_get(organization_code)
        print("The response of AcademicOrganizationsApi->v3_academic_organizations_organization_code_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AcademicOrganizationsApi->v3_academic_organizations_organization_code_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_code** | **str**| Unique Academic Organization code | 

### Return type

[**AcademicOrganization**](AcademicOrganization.md)

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

