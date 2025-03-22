# PersonalizationSetBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**personalization** | **Dict[str, str]** | The NVData keys and values to update. | [optional] 

## Example

```python
from clientapi_cpanel.models.personalization_set_body import PersonalizationSetBody

# TODO update the JSON string below
json = "{}"
# create an instance of PersonalizationSetBody from a JSON string
personalization_set_body_instance = PersonalizationSetBody.from_json(json)
# print the JSON string representation of the object
print(PersonalizationSetBody.to_json())

# convert the object into a dict
personalization_set_body_dict = personalization_set_body_instance.to_dict()
# create an instance of PersonalizationSetBody from a dict
personalization_set_body_from_dict = PersonalizationSetBody.from_dict(personalization_set_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


