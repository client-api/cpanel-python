# TeamHash


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owner** | **str** |  | [optional] 
**users** | [**TeamHashUsers**](TeamHashUsers.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.team_hash import TeamHash

# TODO update the JSON string below
json = "{}"
# create an instance of TeamHash from a JSON string
team_hash_instance = TeamHash.from_json(json)
# print the JSON string representation of the object
print(TeamHash.to_json())

# convert the object into a dict
team_hash_dict = team_hash_instance.to_dict()
# create an instance of TeamHash from a dict
team_hash_from_dict = TeamHash.from_dict(team_hash_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


