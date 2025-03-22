# InlineResponse200282ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | The system’s default PHP version.  Possible values include:   * An installed PHP package that cPanel provides. For example, &#x60;ea-php80&#x60;   * An installed PHP package that another vendor provides. For example, &#x60;alt-php42&#x60;   * &#x60;null&#x60; – This value means PHP is **not** installed. Also, the &#x60;errors&#x60; return will contain a message that indicates that PHP is not installed.  **Note**:    If no default is explicitly set, the package for the newest installed version of PHP is chosen. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200282_result_data import InlineResponse200282ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200282ResultData from a JSON string
inline_response200282_result_data_instance = InlineResponse200282ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200282ResultData.to_json())

# convert the object into a dict
inline_response200282_result_data_dict = inline_response200282_result_data_instance.to_dict()
# create an instance of InlineResponse200282ResultData from a dict
inline_response200282_result_data_from_dict = InlineResponse200282ResultData.from_dict(inline_response200282_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


