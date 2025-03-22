# Score


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**master** | [**ScoreMaster**](ScoreMaster.md) |  | [optional] 
**sub_scores** | [**List[ScoreSubScores]**](ScoreSubScores.md) | Monitoring checks subcategory results.  ** Note: **  We use the check subcategory results to calculate the master results. | [optional] [default to []]

## Example

```python
from clientapi_cpanel.models.score import Score

# TODO update the JSON string below
json = "{}"
# create an instance of Score from a JSON string
score_instance = Score.from_json(json)
# print the JSON string representation of the object
print(Score.to_json())

# convert the object into a dict
score_dict = score_instance.to_dict()
# create an instance of Score from a dict
score_from_dict = Score.from_dict(score_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


