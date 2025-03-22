# ScoreMaster

The overall results for the check.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The title of the check. | [optional] 
**status** | **str** | The check&#39;s summarized status.   * &#x60;good&#x60; — The check has returned a positive result.   * &#x60;bad&#x60;  — The check has returned a negative result. | [optional] 
**message** | **str** | The check&#39;s status message. | [optional] 
**description** | **str** | A description of the check. | [optional] 
**identifier** | **str** | An unique identifier for the check. | [optional] 
**score** | **int** | A numeral score for the check.  ** Note: **  A higher score indicates that your website performs well in that check. | [optional] 
**incidents** | **List[str]** |  | [optional] [default to []]
**attributes** | [**ScoreMasterAttributes**](ScoreMasterAttributes.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.score_master import ScoreMaster

# TODO update the JSON string below
json = "{}"
# create an instance of ScoreMaster from a JSON string
score_master_instance = ScoreMaster.from_json(json)
# print the JSON string representation of the object
print(ScoreMaster.to_json())

# convert the object into a dict
score_master_dict = score_master_instance.to_dict()
# create an instance of ScoreMaster from a dict
score_master_from_dict = ScoreMaster.from_dict(score_master_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


