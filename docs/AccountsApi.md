# authenticate_account.AccountsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_accounts_forgotten_password_post**](AccountsApi.md#api_v1_accounts_forgotten_password_post) | **POST** /api/v1/Accounts/ForgottenPassword | 
[**api_v1_accounts_login_post**](AccountsApi.md#api_v1_accounts_login_post) | **POST** /api/v1/Accounts/Login | Logon to the Authenticate platform using credentials of a platform user account
[**api_v1_accounts_refresh_token_post**](AccountsApi.md#api_v1_accounts_refresh_token_post) | **POST** /api/v1/Accounts/RefreshToken | Refresh an expired JWT using a pre-prepared refresh token
[**api_v1_accounts_reset_password_post**](AccountsApi.md#api_v1_accounts_reset_password_post) | **POST** /api/v1/Accounts/ResetPassword | 

# **api_v1_accounts_forgotten_password_post**
> api_v1_accounts_forgotten_password_post(body=body)



### Example
```python
from __future__ import print_function
import time
import authenticate_account
from authenticate_account.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_account.AccountsApi()
body = authenticate_account.ForgottenPasswordDto() # ForgottenPasswordDto |  (optional)

try:
    api_instance.api_v1_accounts_forgotten_password_post(body=body)
except ApiException as e:
    print("Exception when calling AccountsApi->api_v1_accounts_forgotten_password_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ForgottenPasswordDto**](ForgottenPasswordDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_accounts_login_post**
> AuthResultResponse api_v1_accounts_login_post(body=body)

Logon to the Authenticate platform using credentials of a platform user account

### Example
```python
from __future__ import print_function
import time
import authenticate_account
from authenticate_account.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_account.AccountsApi()
body = authenticate_account.AuthenticationDto() # AuthenticationDto |  (optional)

try:
    # Logon to the Authenticate platform using credentials of a platform user account
    api_response = api_instance.api_v1_accounts_login_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->api_v1_accounts_login_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthenticationDto**](AuthenticationDto.md)|  | [optional] 

### Return type

[**AuthResultResponse**](AuthResultResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_accounts_refresh_token_post**
> AuthResultResponse api_v1_accounts_refresh_token_post(body=body)

Refresh an expired JWT using a pre-prepared refresh token

### Example
```python
from __future__ import print_function
import time
import authenticate_account
from authenticate_account.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_account.AccountsApi()
body = authenticate_account.RenewalDto() # RenewalDto |  (optional)

try:
    # Refresh an expired JWT using a pre-prepared refresh token
    api_response = api_instance.api_v1_accounts_refresh_token_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->api_v1_accounts_refresh_token_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RenewalDto**](RenewalDto.md)|  | [optional] 

### Return type

[**AuthResultResponse**](AuthResultResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_accounts_reset_password_post**
> api_v1_accounts_reset_password_post(body=body)



### Example
```python
from __future__ import print_function
import time
import authenticate_account
from authenticate_account.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = authenticate_account.AccountsApi()
body = authenticate_account.ResetPasswordDto() # ResetPasswordDto |  (optional)

try:
    api_instance.api_v1_accounts_reset_password_post(body=body)
except ApiException as e:
    print("Exception when calling AccountsApi->api_v1_accounts_reset_password_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ResetPasswordDto**](ResetPasswordDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

