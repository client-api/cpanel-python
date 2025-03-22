# TeamHashUsers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | [optional] 
**info** | [**TeamHashUsersInfo**](TeamHashUsersInfo.md) |  | [optional] 

## Example

```python
from clientapi_cpanel.models.team_hash_users import TeamHashUsers

# TODO update the JSON string below
json = "{}"
# create an instance of TeamHashUsers from a JSON string
team_hash_users_instance = TeamHashUsers.from_json(json)
# print the JSON string representation of the object
print(TeamHashUsers.to_json())

# convert the object into a dict
team_hash_users_dict = team_hash_users_instance.to_dict()
# create an instance of TeamHashUsers from a dict
team_hash_users_from_dict = TeamHashUsers.from_dict(team_hash_users_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


