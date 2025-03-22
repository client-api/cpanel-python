# TeamArrayInner


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
**suspend_date** | **int** |  | [optional] 
**suspend_reason** | **str** |  | [optional] 
**username** | **str** |  | [optional] 

## Example

```python
from clientapi_cpanel.models.team_array_inner import TeamArrayInner

# TODO update the JSON string below
json = "{}"
# create an instance of TeamArrayInner from a JSON string
team_array_inner_instance = TeamArrayInner.from_json(json)
# print the JSON string representation of the object
print(TeamArrayInner.to_json())

# convert the object into a dict
team_array_inner_dict = team_array_inner_instance.to_dict()
# create an instance of TeamArrayInner from a dict
team_array_inner_from_dict = TeamArrayInner.from_dict(team_array_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


