# PersonalizationGetBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**names** | **List[str]** | List of NVData keys to query the server about. | [optional] 

## Example

```python
from clientapi_cpanel.models.personalization_get_body import PersonalizationGetBody

# TODO update the JSON string below
json = "{}"
# create an instance of PersonalizationGetBody from a JSON string
personalization_get_body_instance = PersonalizationGetBody.from_json(json)
# print the JSON string representation of the object
print(PersonalizationGetBody.to_json())

# convert the object into a dict
personalization_get_body_dict = personalization_get_body_instance.to_dict()
# create an instance of PersonalizationGetBody from a dict
personalization_get_body_from_dict = PersonalizationGetBody.from_dict(personalization_get_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


