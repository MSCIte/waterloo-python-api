# openapi_client.AccountApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v3_account_confirm_post**](AccountApi.md#v3_account_confirm_post) | **POST** /v3/Account/Confirm | Use this method to confirm your email and activate your account
[**v3_account_email_api_key_reset_get**](AccountApi.md#v3_account_email_api_key_reset_get) | **GET** /v3/Account/{email}/{apiKey}/reset | User this method to put your account in pending confirmation status and generate a new API key. Your old key will no longer grant access. The account will need to be confirmed again before the new key grants access.
[**v3_account_email_get**](AccountApi.md#v3_account_email_get) | **GET** /v3/Account/{email} | Use this method to see if an email has already been registered for an API key
[**v3_account_email_notify_get**](AccountApi.md#v3_account_email_notify_get) | **GET** /v3/Account/{email}/notify | Use this method to have us re-send the confirmation email to an account pending confirmation, if it exists. The activation code will be reset in the process.
[**v3_account_register_post**](AccountApi.md#v3_account_register_post) | **POST** /v3/Account/Register | Use this method to request an API key and begin your registration process


# **v3_account_confirm_post**
> v3_account_confirm_post(email=email, code=code)

Use this method to confirm your email and activate your account

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
    api_instance = openapi_client.AccountApi(api_client)
    email = 'email_example' # str | Email address you used to register (optional)
    code = 'code_example' # str | Activation code we sent you in the confirmation email (optional)

    try:
        # Use this method to confirm your email and activate your account
        api_instance.v3_account_confirm_post(email=email, code=code)
    except Exception as e:
        print("Exception when calling AccountApi->v3_account_confirm_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Email address you used to register | [optional] 
 **code** | **str**| Activation code we sent you in the confirmation email | [optional] 

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

# **v3_account_email_api_key_reset_get**
> v3_account_email_api_key_reset_get(email, api_key)

User this method to put your account in pending confirmation status and generate a new API key. Your old key will no longer grant access. The account will need to be confirmed again before the new key grants access.

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
    api_instance = openapi_client.AccountApi(api_client)
    email = 'email_example' # str | Email address of associated account to reset
    api_key = 'api_key_example' # str | Current API account key

    try:
        # User this method to put your account in pending confirmation status and generate a new API key. Your old key will no longer grant access. The account will need to be confirmed again before the new key grants access.
        api_instance.v3_account_email_api_key_reset_get(email, api_key)
    except Exception as e:
        print("Exception when calling AccountApi->v3_account_email_api_key_reset_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Email address of associated account to reset | 
 **api_key** | **str**| Current API account key | 

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

# **v3_account_email_get**
> v3_account_email_get(email)

Use this method to see if an email has already been registered for an API key

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
    api_instance = openapi_client.AccountApi(api_client)
    email = 'email_example' # str | Email address to check

    try:
        # Use this method to see if an email has already been registered for an API key
        api_instance.v3_account_email_get(email)
    except Exception as e:
        print("Exception when calling AccountApi->v3_account_email_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Email address to check | 

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

# **v3_account_email_notify_get**
> v3_account_email_notify_get(email)

Use this method to have us re-send the confirmation email to an account pending confirmation, if it exists. The activation code will be reset in the process.

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
    api_instance = openapi_client.AccountApi(api_client)
    email = 'email_example' # str | Email address to re-send confirmation email to

    try:
        # Use this method to have us re-send the confirmation email to an account pending confirmation, if it exists. The activation code will be reset in the process.
        api_instance.v3_account_email_notify_get(email)
    except Exception as e:
        print("Exception when calling AccountApi->v3_account_email_notify_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Email address to re-send confirmation email to | 

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

# **v3_account_register_post**
> v3_account_register_post(email=email, project=project, uri=uri)

Use this method to request an API key and begin your registration process

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
    api_instance = openapi_client.AccountApi(api_client)
    email = 'email_example' # str | A unique email that we can use to identify you and contact you. We will ask to confirm it. (optional)
    project = 'project_example' # str | A name and description of your project (optional)
    uri = 'uri_example' # str | The web address of your project: it's live location, app store entry, or similar (optional)

    try:
        # Use this method to request an API key and begin your registration process
        api_instance.v3_account_register_post(email=email, project=project, uri=uri)
    except Exception as e:
        print("Exception when calling AccountApi->v3_account_register_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| A unique email that we can use to identify you and contact you. We will ask to confirm it. | [optional] 
 **project** | **str**| A name and description of your project | [optional] 
 **uri** | **str**| The web address of your project: it&#39;s live location, app store entry, or similar | [optional] 

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

