# InlineResponse200232ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The feature&#39;s system ID. | [optional] 
**is_cpaddon** | **int** | Whether the feature is a [cPAddon](https://go.cpanel.net/cPanelGlossary#addons-cpaddons).  * &#x60;1&#x60; — cPAddon. * &#x60;0&#x60; — **Not** a cPAddon. | [optional] 
**is_plugin** | **int** | Whether the feature is a [plugin](https://go.cpanel.net/cpanelplugin).  * &#x60;1&#x60; — Plugin. * &#x60;0&#x60; — **Not** a plugin. | [optional] 
**name** | **str** | The feature&#39;s name. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200232_result_data import InlineResponse200232ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200232ResultData from a JSON string
inline_response200232_result_data_instance = InlineResponse200232ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200232ResultData.to_json())

# convert the object into a dict
inline_response200232_result_data_dict = inline_response200232_result_data_instance.to_dict()
# create an instance of InlineResponse200232ResultData from a dict
inline_response200232_result_data_from_dict = InlineResponse200232ResultData.from_dict(inline_response200232_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


