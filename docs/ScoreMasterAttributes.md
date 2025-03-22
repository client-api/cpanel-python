# ScoreMasterAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**score** | **int** |  | [optional] 
**limit** | **int** |  | [optional] 

## Example

```python
from clientapi_cpanel.models.score_master_attributes import ScoreMasterAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ScoreMasterAttributes from a JSON string
score_master_attributes_instance = ScoreMasterAttributes.from_json(json)
# print the JSON string representation of the object
print(ScoreMasterAttributes.to_json())

# convert the object into a dict
score_master_attributes_dict = score_master_attributes_instance.to_dict()
# create an instance of ScoreMasterAttributes from a dict
score_master_attributes_from_dict = ScoreMasterAttributes.from_dict(score_master_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


