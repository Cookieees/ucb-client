# ucb_client.BillingApi

All URIs are relative to *https://localhost/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**billing_plan**](BillingApi.md#billing_plan) | **GET** /orgs/{orgid}/projects/{projectid}/billingplan_alpha | Get billing plan


# **billing_plan**
> object billing_plan(orgid, projectid)

Get billing plan

Get the billing plan for the specified organization (but pull from project)

### Example
```python
from __future__ import print_function
import time
import ucb_client
from ucb_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: apikey
configuration = ucb_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure OAuth2 access token for authorization: permissions
configuration = ucb_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = ucb_client.BillingApi(ucb_client.ApiClient(configuration))
orgid = 'orgid_example' # str | Organization identifier
projectid = 'projectid_example' # str | Project identifier

try:
    # Get billing plan
    api_response = api_instance.billing_plan(orgid, projectid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingApi->billing_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 
 **projectid** | **str**| Project identifier | 

### Return type

**object**

### Authorization

[apikey](../README.md#apikey), [permissions](../README.md#permissions)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

