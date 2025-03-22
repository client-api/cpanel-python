# InlineResponse20063ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**details** | [**List[InlineResponse20063ResultDataDetailsInner]**](InlineResponse20063ResultDataDetailsInner.md) | The list of events recorded in the log. If you pass the &#x60;last_id&#x60; parameter, only records in the log after that id are returned. | [optional] 
**log** | **str** | Path to the disinfection log file. The log file will contain a list of JSON objects one per line.  If the last line includes &#x60;\&quot;type\&quot;:\&quot;done\&quot;&#x60;, the file disinfection is complete. | [optional] 
**status** | **str** | * &#x60;done&#x60; - The disinfection is finished. * &#x60;none&#x60; - There is no disinfection scheduled. * &#x60;queued&#x60; - The disinfection is queued. * &#x60;running&#x60; - The disinfection is in progress. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response20063_result_data import InlineResponse20063ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse20063ResultData from a JSON string
inline_response20063_result_data_instance = InlineResponse20063ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse20063ResultData.to_json())

# convert the object into a dict
inline_response20063_result_data_dict = inline_response20063_result_data_instance.to_dict()
# create an instance of InlineResponse20063ResultData from a dict
inline_response20063_result_data_from_dict = InlineResponse20063ResultData.from_dict(inline_response20063_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


