# InlineResponse200371ResultDeps


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gem** | **str** | The shell command to ensure ruby dependencies. It is &#x60;0&#x60; if there are no ruby dependencies. | [optional] 
**npm** | **str** | The shell command to ensure node dependencies. It is &#x60;0&#x60; if there are no node dependencies. | [optional] 
**pip** | **str** | The shell command to ensure python dependencies. It is &#x60;0&#x60; if there are no python dependencies. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200371_result_deps import InlineResponse200371ResultDeps

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200371ResultDeps from a JSON string
inline_response200371_result_deps_instance = InlineResponse200371ResultDeps.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200371ResultDeps.to_json())

# convert the object into a dict
inline_response200371_result_deps_dict = inline_response200371_result_deps_instance.to_dict()
# create an instance of InlineResponse200371ResultDeps from a dict
inline_response200371_result_deps_from_dict = InlineResponse200371ResultDeps.from_dict(inline_response200371_result_deps_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


