# SchemasTeamArrayInner


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
**roles** | **List[str]** |  | [optional] 
**secondary_contact_email** | **str** |  | [optional] 
**services** | [**Services**](Services.md) |  | [optional] 
**suspend_date** | **int** |  | [optional] 
**suspend_reason** | **str** |  | [optional] 
**username** | **str** |  | [optional] 

## Example

```python
from clientapi_cpanel.models.schemas_team_array_inner import SchemasTeamArrayInner

# TODO update the JSON string below
json = "{}"
# create an instance of SchemasTeamArrayInner from a JSON string
schemas_team_array_inner_instance = SchemasTeamArrayInner.from_json(json)
# print the JSON string representation of the object
print(SchemasTeamArrayInner.to_json())

# convert the object into a dict
schemas_team_array_inner_dict = schemas_team_array_inner_instance.to_dict()
# create an instance of SchemasTeamArrayInner from a dict
schemas_team_array_inner_from_dict = SchemasTeamArrayInner.from_dict(schemas_team_array_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


