# ScoreAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scoring** | **str** |  | [optional] 
**score** | **int** |  | [optional] 
**components_processed** | **int** |  | [optional] 
**components_failed** | **int** |  | [optional] 
**limit** | **int** |  | [optional] 
**tool** | **str** |  | [optional] 

## Example

```python
from clientapi_cpanel.models.score_attributes import ScoreAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ScoreAttributes from a JSON string
score_attributes_instance = ScoreAttributes.from_json(json)
# print the JSON string representation of the object
print(ScoreAttributes.to_json())

# convert the object into a dict
score_attributes_dict = score_attributes_instance.to_dict()
# create an instance of ScoreAttributes from a dict
score_attributes_from_dict = ScoreAttributes.from_dict(score_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


