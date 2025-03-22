# HashOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addon_domains** | [**List[Contents]**](Contents.md) | An array of objects containing information about each addon domain. | [optional] 
**main_domain** | [**List[MainDomainContents]**](MainDomainContents.md) | An array of objects containing information about the main domain. | [optional] 
**parked_domains** | [**List[Contents]**](Contents.md) | An array of objects containing information about each parked domain. | [optional] 
**sub_domains** | [**List[Contents]**](Contents.md) | An array of objects containing information about each subdomain. | [optional] 

## Example

```python
from clientapi_cpanel.models.hash_output import HashOutput

# TODO update the JSON string below
json = "{}"
# create an instance of HashOutput from a JSON string
hash_output_instance = HashOutput.from_json(json)
# print the JSON string representation of the object
print(HashOutput.to_json())

# convert the object into a dict
hash_output_dict = hash_output_instance.to_dict()
# create an instance of HashOutput from a dict
hash_output_from_dict = HashOutput.from_dict(hash_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


