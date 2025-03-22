# TeamHashUsersInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact_email** | **str** |  | [optional] 
**created** | **int** |  | [optional] 
**expire_date** | **int** |  | [optional] 
**expire_reason** | **str** |  | [optional] 
**lastlogin** | **int** |  | [optional] 
**locale** | **str** |  | [optional] 
**notes** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**roles** | **List[str]** |  | [optional] 
**secondary_contact_email** | **str** |  | [optional] 
**services** | [**Services**](Services.md) |  | [optional] 
**suspend_date** | **str** |  | [optional] 
**suspend_reason** | **str** |  | [optional] 

## Example

```python
from clientapi_cpanel.models.team_hash_users_info import TeamHashUsersInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TeamHashUsersInfo from a JSON string
team_hash_users_info_instance = TeamHashUsersInfo.from_json(json)
# print the JSON string representation of the object
print(TeamHashUsersInfo.to_json())

# convert the object into a dict
team_hash_users_info_dict = team_hash_users_info_instance.to_dict()
# create an instance of TeamHashUsersInfo from a dict
team_hash_users_info_from_dict = TeamHashUsersInfo.from_dict(team_hash_users_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


