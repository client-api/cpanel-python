# ScoreSubScores


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The title of the check subcategory. | [optional] 
**status** | **str** | The check subcategory&#39;s summarized status.   * &#x60;good&#x60; — The check has returned a positive result.   * &#x60;bad&#x60;  — The check has returned a negative result. | [optional] 
**message** | **str** | The check subcategory&#39;s status message. | [optional] 
**description** | **str** | A description of the check. | [optional] 
**identifier** | **str** | An unique identifier for the check. | [optional] 
**score** | **int** | A numeral score for the check subcategory.  ** Note: **  A higher score indicates that your website performs well in that check. | [optional] 
**incidents** | **List[str]** |  | [optional] [default to []]
**weight** | **int** | The weighted contribution of the subcategory check&#39;s &#x60;score&#x60; result to the &#x60;master&#x60; object&#39;s &#x60;score&#x60; result. | [optional] 
**weighted_score** | **int** | The score after weight has been adjusted. | [optional] 
**attributes** | [**ScoreAttributes**](ScoreAttributes.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.score_sub_scores import ScoreSubScores

# TODO update the JSON string below
json = "{}"
# create an instance of ScoreSubScores from a JSON string
score_sub_scores_instance = ScoreSubScores.from_json(json)
# print the JSON string representation of the object
print(ScoreSubScores.to_json())

# convert the object into a dict
score_sub_scores_dict = score_sub_scores_instance.to_dict()
# create an instance of ScoreSubScores from a dict
score_sub_scores_from_dict = ScoreSubScores.from_dict(score_sub_scores_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


