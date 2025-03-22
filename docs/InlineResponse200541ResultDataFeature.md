# InlineResponse200541ResultDataFeature

The available features on the account that exist in the `/var/cpanel/users/user` file`, where user represents the cPanel user.  **Note:**  This object returns any custom features that the hosting provider adds to the `/var/cpanel/users/user` file.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_properties** | **int** | Whether the feature is enabled. * &#x60;1&#x60; - Enabled. * &#x60;0&#x60; - Disabled.  **Note:**  The feature&#39;s name is the return name. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200541_result_data_feature import InlineResponse200541ResultDataFeature

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200541ResultDataFeature from a JSON string
inline_response200541_result_data_feature_instance = InlineResponse200541ResultDataFeature.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200541ResultDataFeature.to_json())

# convert the object into a dict
inline_response200541_result_data_feature_dict = inline_response200541_result_data_feature_instance.to_dict()
# create an instance of InlineResponse200541ResultDataFeature from a dict
inline_response200541_result_data_feature_from_dict = InlineResponse200541ResultDataFeature.from_dict(inline_response200541_result_data_feature_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


