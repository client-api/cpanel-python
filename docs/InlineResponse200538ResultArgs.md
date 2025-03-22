# InlineResponse200538ResultArgs

An object containing one or more action- and subsystem-specific arguments, if any exist.  For example, a task that returns an `action` value of `create` and a `subsystem` value of `VersionControl` will include the `repository_root` argument.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repository_root** | **str** | The absolute path to the repostiory&#39;s &#x60;root&#x60; directory. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200538_result_args import InlineResponse200538ResultArgs

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200538ResultArgs from a JSON string
inline_response200538_result_args_instance = InlineResponse200538ResultArgs.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200538ResultArgs.to_json())

# convert the object into a dict
inline_response200538_result_args_dict = inline_response200538_result_args_instance.to_dict()
# create an instance of InlineResponse200538ResultArgs from a dict
inline_response200538_result_args_from_dict = InlineResponse200538ResultArgs.from_dict(inline_response200538_result_args_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


