# FeatureDescriptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**features** | **List[str]** | The list of features in a role. | [optional] 
**id** | **str** | The role&#39;s ID. | [optional] 
**title** | **str** | The role&#39;s title. | [optional] 

## Example

```python
from clientapi_cpanel.models.feature_descriptions import FeatureDescriptions

# TODO update the JSON string below
json = "{}"
# create an instance of FeatureDescriptions from a JSON string
feature_descriptions_instance = FeatureDescriptions.from_json(json)
# print the JSON string representation of the object
print(FeatureDescriptions.to_json())

# convert the object into a dict
feature_descriptions_dict = feature_descriptions_instance.to_dict()
# create an instance of FeatureDescriptions from a dict
feature_descriptions_from_dict = FeatureDescriptions.from_dict(feature_descriptions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


