# clientapi_cpanel.ImageManagerApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**convert_file**](ImageManagerApi.md#convert_file) | **GET** /ImageManager/convert_file | Create image with new format
[**create_thumbnails**](ImageManagerApi.md#create_thumbnails) | **GET** /ImageManager/create_thumbnails | Create image thumbnails
[**get_dimensions**](ImageManagerApi.md#get_dimensions) | **GET** /ImageManager/get_dimensions | Return image dimensions
[**resize_image**](ImageManagerApi.md#resize_image) | **GET** /ImageManager/resize_image | Save resized image


# **convert_file**
> InlineResponse200270 convert_file(image_file, type)

Create image with new format

This function converts an image to a new file format.

**Important:**

When you disable the [WebServer role](https://docs.cpanel.net/knowledge-base/general-systems-administration/how-to-use-server-profiles/#roles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200270 import InlineResponse200270
from clientapi_cpanel.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://cpanel-server.tld:2083/execute
# See configuration.py for a list of all supported configuration parameters.
configuration = clientapi_cpanel.Configuration(
    host = "https://cpanel-server.tld:2083/execute"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = clientapi_cpanel.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with clientapi_cpanel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = clientapi_cpanel.ImageManagerApi(api_client)
    image_file = 'images/myimage.jpg' # str | The image file to convert, relative to the cPanel account's `/home` directory.
    type = 'png' # str | The format to which to convert the images.

    try:
        # Create image with new format
        api_response = api_instance.convert_file(image_file, type)
        print("The response of ImageManagerApi->convert_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImageManagerApi->convert_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_file** | **str**| The image file to convert, relative to the cPanel account&#39;s &#x60;/home&#x60; directory. | 
 **type** | **str**| The format to which to convert the images. | 

### Return type

[**InlineResponse200270**](InlineResponse200270.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | HTTP Request was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_thumbnails**
> InlineResponse200271 create_thumbnails(dir, height_percentage, width_percentage)

Create image thumbnails

This function creates thumbnails from images. The function saves the new thumbnail images in a thumbnails subdirectory inside the original directory. The system prepends thumbnail filenames with ``tn_`` (for example, ``tn_picture.jpg``).

**Important:**

When you disable the [WebServer role](https://go.cpanel.net/serverroles), the system disables this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200271 import InlineResponse200271
from clientapi_cpanel.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://cpanel-server.tld:2083/execute
# See configuration.py for a list of all supported configuration parameters.
configuration = clientapi_cpanel.Configuration(
    host = "https://cpanel-server.tld:2083/execute"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = clientapi_cpanel.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with clientapi_cpanel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = clientapi_cpanel.ImageManagerApi(api_client)
    dir = 'images' # str | The path to the directory where the image resides. When you pass this parameter, the function creates a thumbnail directory directly below the image directory.  **NOTE:**  This parameter can use an absolute directory path or a path relative to the user's home directory.
    height_percentage = 25 # int | The percentage by which to reduce the thumbnails' height.
    width_percentage = 25 # int | The percentage by which to reduce the thumbnails' width.

    try:
        # Create image thumbnails
        api_response = api_instance.create_thumbnails(dir, height_percentage, width_percentage)
        print("The response of ImageManagerApi->create_thumbnails:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImageManagerApi->create_thumbnails: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dir** | **str**| The path to the directory where the image resides. When you pass this parameter, the function creates a thumbnail directory directly below the image directory.  **NOTE:**  This parameter can use an absolute directory path or a path relative to the user&#39;s home directory. | 
 **height_percentage** | **int**| The percentage by which to reduce the thumbnails&#39; height. | 
 **width_percentage** | **int**| The percentage by which to reduce the thumbnails&#39; width. | 

### Return type

[**InlineResponse200271**](InlineResponse200271.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | HTTP Request was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dimensions**
> InlineResponse200272 get_dimensions(image_file)

Return image dimensions

This function returns the dimensions of the image file that you specify.

**Important:**

When you disable the [WebServer role](https://docs.cpanel.net/knowledge-base/general-systems-administration/how-to-use-server-profiles/#roles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200272 import InlineResponse200272
from clientapi_cpanel.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://cpanel-server.tld:2083/execute
# See configuration.py for a list of all supported configuration parameters.
configuration = clientapi_cpanel.Configuration(
    host = "https://cpanel-server.tld:2083/execute"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = clientapi_cpanel.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with clientapi_cpanel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = clientapi_cpanel.ImageManagerApi(api_client)
    image_file = 'image/myimage.jpg' # str | The path to the file to measure.  **Note:**  Use the absolute filepath or a path relative to the user's home directory.

    try:
        # Return image dimensions
        api_response = api_instance.get_dimensions(image_file)
        print("The response of ImageManagerApi->get_dimensions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImageManagerApi->get_dimensions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_file** | **str**| The path to the file to measure.  **Note:**  Use the absolute filepath or a path relative to the user&#39;s home directory. | 

### Return type

[**InlineResponse200272**](InlineResponse200272.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | HTTP Request was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resize_image**
> InlineResponse200273 resize_image(height, image_file, width, save_original_as=save_original_as)

Save resized image

This function resizes a specified image.

**Important:**

When you disable the [WebServer role](https://docs.cpanel.net/knowledge-base/general-systems-administration/how-to-use-server-profiles/#roles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200273 import InlineResponse200273
from clientapi_cpanel.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://cpanel-server.tld:2083/execute
# See configuration.py for a list of all supported configuration parameters.
configuration = clientapi_cpanel.Configuration(
    host = "https://cpanel-server.tld:2083/execute"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = clientapi_cpanel.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with clientapi_cpanel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = clientapi_cpanel.ImageManagerApi(api_client)
    height = 300 # int | The height to which to set the image size.
    image_file = '/images/image.jpg' # str | The name of the file to scale.  **Note:**  Use the absolute filepath or a filepath relative to the user's home directory.
    width = 200 # int | The width to which to set the image size.
    save_original_as = 'images/original.jpg' # str | The path to the directory in which to save a copy the original image file.  **Note:**  * If you don't pass this parameter, the function doesn't save a copy of the original image. * Use the absolute filepath or a filepath relative to the user's home directory. (optional)

    try:
        # Save resized image
        api_response = api_instance.resize_image(height, image_file, width, save_original_as=save_original_as)
        print("The response of ImageManagerApi->resize_image:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImageManagerApi->resize_image: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **height** | **int**| The height to which to set the image size. | 
 **image_file** | **str**| The name of the file to scale.  **Note:**  Use the absolute filepath or a filepath relative to the user&#39;s home directory. | 
 **width** | **int**| The width to which to set the image size. | 
 **save_original_as** | **str**| The path to the directory in which to save a copy the original image file.  **Note:**  * If you don&#39;t pass this parameter, the function doesn&#39;t save a copy of the original image. * Use the absolute filepath or a filepath relative to the user&#39;s home directory. | [optional] 

### Return type

[**InlineResponse200273**](InlineResponse200273.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | HTTP Request was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

