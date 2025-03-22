# clientapi_cpanel.FilemanApi

All URIs are relative to *https://cpanel-server.tld:2083/execute*

Method | HTTP request | Description
------------- | ------------- | -------------
[**autocompletedir**](FilemanApi.md#autocompletedir) | **GET** /Fileman/autocompletedir | Return autocomplete file and directory names
[**empty_trash**](FilemanApi.md#empty_trash) | **GET** /Fileman/empty_trash | Delete .trash folder content
[**get_file_content**](FilemanApi.md#get_file_content) | **GET** /Fileman/get_file_content | Return file content
[**get_file_information**](FilemanApi.md#get_file_information) | **GET** /Fileman/get_file_information | Return file or directory information
[**list_files**](FilemanApi.md#list_files) | **GET** /Fileman/list_files | Return directory content
[**save_file_content**](FilemanApi.md#save_file_content) | **GET** /Fileman/save_file_content | Save file
[**transcode**](FilemanApi.md#transcode) | **GET** /Fileman/transcode | Update buffer encoding
[**upload_files**](FilemanApi.md#upload_files) | **GET** /Fileman/upload_files | Upload files


# **autocompletedir**
> InlineResponse200235 autocompletedir(path, dirsonly=dirsonly, html=html, list_all=list_all)

Return autocomplete file and directory names

This function returns any files and directories that begin with a specified string.

**Important:**

  When you disable the [File Storage role](https://go.cpanel.net/howtouseserverprofiles#roles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200235 import InlineResponse200235
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
    api_instance = clientapi_cpanel.FilemanApi(api_client)
    path = 'public' # str | The prefix of the paths to complete.
    dirsonly = 0 # int | Whether to include only directories in the output. * `1` — **Only** include directories. * `0` — Include directories **and** files. (optional) (default to 0)
    html = 1 # int | Whether to return HTML-encoded results. * `1` — Return HTML-encoded output. * `0` — Return plaintext output. (optional) (default to 1)
    list_all = 1 # int | Whether to return all files and directories inside the specified directory. If you set this parameter's value to `1`, you **must** set the `path` parameter's value to a full directory path. * `1` — Return **all** files and directories inside the specified directory. * `0` — Return partial file and directory name matches. (optional) (default to 1)

    try:
        # Return autocomplete file and directory names
        api_response = api_instance.autocompletedir(path, dirsonly=dirsonly, html=html, list_all=list_all)
        print("The response of FilemanApi->autocompletedir:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilemanApi->autocompletedir: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| The prefix of the paths to complete. | 
 **dirsonly** | **int**| Whether to include only directories in the output. * &#x60;1&#x60; — **Only** include directories. * &#x60;0&#x60; — Include directories **and** files. | [optional] [default to 0]
 **html** | **int**| Whether to return HTML-encoded results. * &#x60;1&#x60; — Return HTML-encoded output. * &#x60;0&#x60; — Return plaintext output. | [optional] [default to 1]
 **list_all** | **int**| Whether to return all files and directories inside the specified directory. If you set this parameter&#39;s value to &#x60;1&#x60;, you **must** set the &#x60;path&#x60; parameter&#39;s value to a full directory path. * &#x60;1&#x60; — Return **all** files and directories inside the specified directory. * &#x60;0&#x60; — Return partial file and directory name matches. | [optional] [default to 1]

### Return type

[**InlineResponse200235**](InlineResponse200235.md)

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

# **empty_trash**
> InlineResponse200236 empty_trash(older_than=older_than)

Delete .trash folder content

This function purges content from the `.trash` folder in the user's home directory.

**Important:**

  When you disable the [FileStorage role](https://docs.cpanel.net/knowledge-base/general-systems-administration/how-to-use-server-profiles/#roles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200236 import InlineResponse200236
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
    api_instance = clientapi_cpanel.FilemanApi(api_client)
    older_than = 0 # int | The maximum age in days of content that the function will not purge.  **Note:**  A value of `0` will purge everything from the user's `.trash` folder. (optional) (default to 0)

    try:
        # Delete .trash folder content
        api_response = api_instance.empty_trash(older_than=older_than)
        print("The response of FilemanApi->empty_trash:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilemanApi->empty_trash: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **older_than** | **int**| The maximum age in days of content that the function will not purge.  **Note:**  A value of &#x60;0&#x60; will purge everything from the user&#39;s &#x60;.trash&#x60; folder. | [optional] [default to 0]

### Return type

[**InlineResponse200236**](InlineResponse200236.md)

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

# **get_file_content**
> InlineResponse200237 get_file_content(dir, file, from_charset=from_charset, to_charset=to_charset, update_html_document_encoding=update_html_document_encoding)

Return file content

This function retrieves a file's content.

**Important:**

When you disable the [File Storage](https://go.cpanel.net/serverroles) role, the system **disables** this function.

**Note:**

JSON strings **must** be valid UTF-8. To retrieve a non-UTF-8 file via
JSON, we recommend that you give `ISO-8859-1` as `from_charset` and
`UTF-8` as `to_charset`, then decode the return payload’s `content`
as UTF-8.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200237 import InlineResponse200237
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
    api_instance = clientapi_cpanel.FilemanApi(api_client)
    dir = '/home/user/public.html' # str | The file path to the directory that contains the selected file.
    file = 'example.html' # str | The file to retrieve.
    from_charset = '_DETECT_' # str | The file’s character encoding. This parameter defaults to `_DETECT_`, which indicates a request to detect the file’s character encoding. (optional) (default to '_DETECT_')
    to_charset = '_LOCALE_' # str | The output character encoding. This parameter defaults to `_LOCALE_`, which indicates a request to use the session locale’s character encoding.  **Important:**  Contexts that serialize the API response as JSON **require** this value to be `utf-8` or `US-ASCII`. Behavior is **undefined** if the request indicates any other encoding. (optional) (default to '_LOCALE_')
    update_html_document_encoding = 1 # int | Whether to update the file's HTML document encoding.  * `1` — Update the file's HTML document encoding. * `0` — Don't update the file's HTML encoding. (optional) (default to 1)

    try:
        # Return file content
        api_response = api_instance.get_file_content(dir, file, from_charset=from_charset, to_charset=to_charset, update_html_document_encoding=update_html_document_encoding)
        print("The response of FilemanApi->get_file_content:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilemanApi->get_file_content: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dir** | **str**| The file path to the directory that contains the selected file. | 
 **file** | **str**| The file to retrieve. | 
 **from_charset** | **str**| The file’s character encoding. This parameter defaults to &#x60;_DETECT_&#x60;, which indicates a request to detect the file’s character encoding. | [optional] [default to &#39;_DETECT_&#39;]
 **to_charset** | **str**| The output character encoding. This parameter defaults to &#x60;_LOCALE_&#x60;, which indicates a request to use the session locale’s character encoding.  **Important:**  Contexts that serialize the API response as JSON **require** this value to be &#x60;utf-8&#x60; or &#x60;US-ASCII&#x60;. Behavior is **undefined** if the request indicates any other encoding. | [optional] [default to &#39;_LOCALE_&#39;]
 **update_html_document_encoding** | **int**| Whether to update the file&#39;s HTML document encoding.  * &#x60;1&#x60; — Update the file&#39;s HTML document encoding. * &#x60;0&#x60; — Don&#39;t update the file&#39;s HTML encoding. | [optional] [default to 1]

### Return type

[**InlineResponse200237**](InlineResponse200237.md)

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

# **get_file_information**
> InlineResponse200238 get_file_information(path, check_for_leaf_directories=check_for_leaf_directories, include_hash=include_hash, include_mime=include_mime, include_permissions=include_permissions, show_hidden=show_hidden)

Return file or directory information

This function returns the information for a specified file or directory.

**Important:**

When you disable the [File Storage](https://go.cpanel.net/serverroles) role, the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200238 import InlineResponse200238
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
    api_instance = clientapi_cpanel.FilemanApi(api_client)
    path = 'public_html' # str | The directory from which to list files.
    check_for_leaf_directories = 0 # int | Whether to flag directories that contain subdirectories.  * `1` - Flag directories that contain subdirectories. * `0` - Do **not** flag directories that contain subdirectories. (optional) (default to 0)
    include_hash = 0 # int | Whether to return a hash of the file's information.  * `1` - Return a hash of the file's information. * `0` - Do **not** return a hash of the file's information. (optional) (default to 0)
    include_mime = 0 # int | Whether to return the file's MIME type.  * `1` - Return the file's MIME type. * `0` - Do **not** return the file's MIME type. (optional) (default to 0)
    include_permissions = 0 # int | Whether to parse the file owner's read and write permissions.  * `1` - Parse the file owner's read and write permissions. * `0` - Do **not** parse the file owner's read and write permissions. (optional) (default to 0)
    show_hidden = 0 # int | Whether to include hidden files in the output.  * `1` - Include hidden files. * `0` - Do **not** include hidden files. (optional) (default to 0)

    try:
        # Return file or directory information
        api_response = api_instance.get_file_information(path, check_for_leaf_directories=check_for_leaf_directories, include_hash=include_hash, include_mime=include_mime, include_permissions=include_permissions, show_hidden=show_hidden)
        print("The response of FilemanApi->get_file_information:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilemanApi->get_file_information: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| The directory from which to list files. | 
 **check_for_leaf_directories** | **int**| Whether to flag directories that contain subdirectories.  * &#x60;1&#x60; - Flag directories that contain subdirectories. * &#x60;0&#x60; - Do **not** flag directories that contain subdirectories. | [optional] [default to 0]
 **include_hash** | **int**| Whether to return a hash of the file&#39;s information.  * &#x60;1&#x60; - Return a hash of the file&#39;s information. * &#x60;0&#x60; - Do **not** return a hash of the file&#39;s information. | [optional] [default to 0]
 **include_mime** | **int**| Whether to return the file&#39;s MIME type.  * &#x60;1&#x60; - Return the file&#39;s MIME type. * &#x60;0&#x60; - Do **not** return the file&#39;s MIME type. | [optional] [default to 0]
 **include_permissions** | **int**| Whether to parse the file owner&#39;s read and write permissions.  * &#x60;1&#x60; - Parse the file owner&#39;s read and write permissions. * &#x60;0&#x60; - Do **not** parse the file owner&#39;s read and write permissions. | [optional] [default to 0]
 **show_hidden** | **int**| Whether to include hidden files in the output.  * &#x60;1&#x60; - Include hidden files. * &#x60;0&#x60; - Do **not** include hidden files. | [optional] [default to 0]

### Return type

[**InlineResponse200238**](InlineResponse200238.md)

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

# **list_files**
> InlineResponse200239 list_files(dir, check_for_leaf_directories=check_for_leaf_directories, include_hash=include_hash, include_mime=include_mime, include_permissions=include_permissions, limit_to_list=limit_to_list, mime_types=mime_types, only_these_files=only_these_files, raw_mime_types=raw_mime_types, show_hidden=show_hidden, types=types)

Return directory content

This function returns a sorted list of files and directories.

**Important:**

When you disable the [FileStorage role](https://go.cpanel.net/howtouseserverprofiles#roles), the system **disables** this function. For more information, read our How to Use Server Profiles documentation.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200239 import InlineResponse200239
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
    api_instance = clientapi_cpanel.FilemanApi(api_client)
    dir = 'public_html' # str | The directory from which to list files.
    check_for_leaf_directories = 0 # int | Whether to return directories that contain subdirectories.  * `1` — Return subdirectories. * `0` — Do **not** retain subdirectories. (optional) (default to 0)
    include_hash = 0 # int | Whether to include a hash of the file's information in the return.  * `1` — Generate a hash. * `0` — Do **not** generate a hash. (optional) (default to 0)
    include_mime = 0 # int | Whether to return the file's MIME type.  * `1` — Include MIME type. * `0` — Do **not** include MIME type.  **Note:**   If you set this value to `0` but also include the `mime_types` or `raw_mime_types` parameters, the function **overrides** your specified value and sets this parameter to `1`. (optional) (default to 0)
    include_permissions = 0 # int | Whether to parse the file owner's read and write permissions.  * `1` — Parse file permissions. * `0` — Do **not** parse file permissions. (optional) (default to 0)
    limit_to_list = 0 # int | Whether to return only entries that begin with the `filepath-` prefix.  * `1` — Return only files that begin with the `filepath-` prefix. * `0` — Return **all** files.  If you do not use this parameter, the function returns all filenames. (optional)
    mime_types = 'text-plain' # str | The MIME types to return.  * If you use this parameter, the function returns the specified MIME types and sets the `include_mime` parameter's value to `1`. * If you do **not** use this parameter, the function returns all MIME types. (optional)
    only_these_files = 'cpbackup-exclude.conf' # str | A comma-separated list of files to return.  If you do not use this parameter, the function returns all files. (optional)
    raw_mime_types = 'text/plain' # str | The raw MIME types to return.  * If you use this parameter, the function returns the specified MIME types and sets the `include_mime` parameter's value to `1`. * If you do **not** use this parameter, the function returns all MIME types. (optional)
    show_hidden = 0 # int | Whether to include hidden files in the output.  * `1` — Include hidden files. * `0` — Do **not** include hidden files. (optional) (default to 0)
    types = ['types_example'] # List[str] | A pipe-separated list of file types to return.  * `file` — A file. * `dir` — A directory. * `char` — A character special device. * `block` — A block special device. * `fifo` — A named pipe (FIFO). * `link` — A symbolic link. * `socket` — A Unix domain socket.  If you do not use this parameter, the function returns all file types. (optional)

    try:
        # Return directory content
        api_response = api_instance.list_files(dir, check_for_leaf_directories=check_for_leaf_directories, include_hash=include_hash, include_mime=include_mime, include_permissions=include_permissions, limit_to_list=limit_to_list, mime_types=mime_types, only_these_files=only_these_files, raw_mime_types=raw_mime_types, show_hidden=show_hidden, types=types)
        print("The response of FilemanApi->list_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilemanApi->list_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dir** | **str**| The directory from which to list files. | 
 **check_for_leaf_directories** | **int**| Whether to return directories that contain subdirectories.  * &#x60;1&#x60; — Return subdirectories. * &#x60;0&#x60; — Do **not** retain subdirectories. | [optional] [default to 0]
 **include_hash** | **int**| Whether to include a hash of the file&#39;s information in the return.  * &#x60;1&#x60; — Generate a hash. * &#x60;0&#x60; — Do **not** generate a hash. | [optional] [default to 0]
 **include_mime** | **int**| Whether to return the file&#39;s MIME type.  * &#x60;1&#x60; — Include MIME type. * &#x60;0&#x60; — Do **not** include MIME type.  **Note:**   If you set this value to &#x60;0&#x60; but also include the &#x60;mime_types&#x60; or &#x60;raw_mime_types&#x60; parameters, the function **overrides** your specified value and sets this parameter to &#x60;1&#x60;. | [optional] [default to 0]
 **include_permissions** | **int**| Whether to parse the file owner&#39;s read and write permissions.  * &#x60;1&#x60; — Parse file permissions. * &#x60;0&#x60; — Do **not** parse file permissions. | [optional] [default to 0]
 **limit_to_list** | **int**| Whether to return only entries that begin with the &#x60;filepath-&#x60; prefix.  * &#x60;1&#x60; — Return only files that begin with the &#x60;filepath-&#x60; prefix. * &#x60;0&#x60; — Return **all** files.  If you do not use this parameter, the function returns all filenames. | [optional] 
 **mime_types** | **str**| The MIME types to return.  * If you use this parameter, the function returns the specified MIME types and sets the &#x60;include_mime&#x60; parameter&#39;s value to &#x60;1&#x60;. * If you do **not** use this parameter, the function returns all MIME types. | [optional] 
 **only_these_files** | **str**| A comma-separated list of files to return.  If you do not use this parameter, the function returns all files. | [optional] 
 **raw_mime_types** | **str**| The raw MIME types to return.  * If you use this parameter, the function returns the specified MIME types and sets the &#x60;include_mime&#x60; parameter&#39;s value to &#x60;1&#x60;. * If you do **not** use this parameter, the function returns all MIME types. | [optional] 
 **show_hidden** | **int**| Whether to include hidden files in the output.  * &#x60;1&#x60; — Include hidden files. * &#x60;0&#x60; — Do **not** include hidden files. | [optional] [default to 0]
 **types** | [**List[str]**](str.md)| A pipe-separated list of file types to return.  * &#x60;file&#x60; — A file. * &#x60;dir&#x60; — A directory. * &#x60;char&#x60; — A character special device. * &#x60;block&#x60; — A block special device. * &#x60;fifo&#x60; — A named pipe (FIFO). * &#x60;link&#x60; — A symbolic link. * &#x60;socket&#x60; — A Unix domain socket.  If you do not use this parameter, the function returns all file types. | [optional] 

### Return type

[**InlineResponse200239**](InlineResponse200239.md)

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

# **save_file_content**
> InlineResponse200240 save_file_content(file, content=content, dir=dir, fallback=fallback, from_charset=from_charset, to_charset=to_charset)

Save file

This function saves a file in a directory and encodes it in a character set.

**Important:**

  When you disable the [File Storage role](https://go.cpanel.net/howtouseserverprofiles#roles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200240 import InlineResponse200240
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
    api_instance = clientapi_cpanel.FilemanApi(api_client)
    file = 'example.html' # str | The files to retrieve.
    content = 'hi' # str | The new file's contents. If you do **not** use this parameter, the function creates a blank file. (optional)
    dir = '/home/username/public_html' # str | The directory that contains the selected file.  **Note:**  This parameter defaults to the currently-authenticated user's `/home` directory. (optional)
    fallback = 1 # int | Whether the function will return an error or save in the default character set if it cannot save in the specified character set.  * `1` — Save in the default character set. * `0` — Return an error. (optional) (default to 1)
    from_charset = 'UTF-8' # str | The [character set encoding](https://en.wikipedia.org/wiki/Character_encoding) of the `content` parameter's value. (optional) (default to 'UTF-8')
    to_charset = 'UTF-8' # str | The [character set encoding](https://en.wikipedia.org/wiki/Character_encoding) in which to encode the file. (optional) (default to 'UTF-8')

    try:
        # Save file
        api_response = api_instance.save_file_content(file, content=content, dir=dir, fallback=fallback, from_charset=from_charset, to_charset=to_charset)
        print("The response of FilemanApi->save_file_content:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilemanApi->save_file_content: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **str**| The files to retrieve. | 
 **content** | **str**| The new file&#39;s contents. If you do **not** use this parameter, the function creates a blank file. | [optional] 
 **dir** | **str**| The directory that contains the selected file.  **Note:**  This parameter defaults to the currently-authenticated user&#39;s &#x60;/home&#x60; directory. | [optional] 
 **fallback** | **int**| Whether the function will return an error or save in the default character set if it cannot save in the specified character set.  * &#x60;1&#x60; — Save in the default character set. * &#x60;0&#x60; — Return an error. | [optional] [default to 1]
 **from_charset** | **str**| The [character set encoding](https://en.wikipedia.org/wiki/Character_encoding) of the &#x60;content&#x60; parameter&#39;s value. | [optional] [default to &#39;UTF-8&#39;]
 **to_charset** | **str**| The [character set encoding](https://en.wikipedia.org/wiki/Character_encoding) in which to encode the file. | [optional] [default to &#39;UTF-8&#39;]

### Return type

[**InlineResponse200240**](InlineResponse200240.md)

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

# **transcode**
> InlineResponse200241 transcode(content, discard_illegal=discard_illegal, from_charset=from_charset, to_charset=to_charset, transliterate=transliterate)

Update buffer encoding

This function converts a buffer from one encoding language to another.

**Important:**

  When you disable the [File Storage role](https://go.cpanel.net/serverroles), the system **disables** this function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200241 import InlineResponse200241
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
    api_instance = clientapi_cpanel.FilemanApi(api_client)
    content = 'hi' # str | The file's contents.
    discard_illegal = 1 # int | Whether to discard any characters that do not transcode correctly.   * `1` - Discard invalid characters.   * `0` - Transcode invalid characters in the default [character set encoding](https://en.wikipedia.org/wiki/Character_encoding). (optional)
    from_charset = 'UTF-8' # str | The file's current [character set encoding](https://en.wikipedia.org/wiki/Character_encoding). (optional)
    to_charset = 'ASCII' # str | The [character set encoding](https://en.wikipedia.org/wiki/Character_encoding) in which to encode the file. (optional)
    transliterate = 0 # int | Whether to transcode invalid characters to valid characters in the new character set encoding.   * `1` - Transcode invalid characters in the new [character set encoding](https://en.wikipedia.org/wiki/Character_encoding).   * `0` - Return an error message. (optional)

    try:
        # Update buffer encoding
        api_response = api_instance.transcode(content, discard_illegal=discard_illegal, from_charset=from_charset, to_charset=to_charset, transliterate=transliterate)
        print("The response of FilemanApi->transcode:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilemanApi->transcode: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content** | **str**| The file&#39;s contents. | 
 **discard_illegal** | **int**| Whether to discard any characters that do not transcode correctly.   * &#x60;1&#x60; - Discard invalid characters.   * &#x60;0&#x60; - Transcode invalid characters in the default [character set encoding](https://en.wikipedia.org/wiki/Character_encoding). | [optional] 
 **from_charset** | **str**| The file&#39;s current [character set encoding](https://en.wikipedia.org/wiki/Character_encoding). | [optional] 
 **to_charset** | **str**| The [character set encoding](https://en.wikipedia.org/wiki/Character_encoding) in which to encode the file. | [optional] 
 **transliterate** | **int**| Whether to transcode invalid characters to valid characters in the new character set encoding.   * &#x60;1&#x60; - Transcode invalid characters in the new [character set encoding](https://en.wikipedia.org/wiki/Character_encoding).   * &#x60;0&#x60; - Return an error message. | [optional] 

### Return type

[**InlineResponse200241**](InlineResponse200241.md)

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

# **upload_files**
> InlineResponse200242 upload_files()

Upload files

This function uploads files.

**Note:**

  For more information about how to use this function in your custom code,
  read our [Use UAPI's `Fileman::upload_files` 
  Function in Custom Code tutorial](https://go.cpanel.net/tutorial-use-uapis-fileman-upload-files-function-in-custom-code). 

**Important:**

 When you disable the [File Storage](https://go.cpanel.net/serverroles) role, the system **disables** this function.

You cannot call this function through WHM API 1's [uapi_cpanel](https://go.cpanel.net/UseWHMAPItoCallcPanelAPIandUAPI) function.

### Example

* Basic Authentication (BasicAuth):

```python
import clientapi_cpanel
from clientapi_cpanel.models.inline_response200242 import InlineResponse200242
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
    api_instance = clientapi_cpanel.FilemanApi(api_client)

    try:
        # Upload files
        api_response = api_instance.upload_files()
        print("The response of FilemanApi->upload_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilemanApi->upload_files: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InlineResponse200242**](InlineResponse200242.md)

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

