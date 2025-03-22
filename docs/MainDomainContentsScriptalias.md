# MainDomainContentsScriptalias

The domain's CGI information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | The absolute path to the domain&#39;s CGI directory. | [optional] 
**url** | **str** | The domain&#39;s CGI directory. | [optional] 

## Example

```python
from clientapi_cpanel.models.main_domain_contents_scriptalias import MainDomainContentsScriptalias

# TODO update the JSON string below
json = "{}"
# create an instance of MainDomainContentsScriptalias from a JSON string
main_domain_contents_scriptalias_instance = MainDomainContentsScriptalias.from_json(json)
# print the JSON string representation of the object
print(MainDomainContentsScriptalias.to_json())

# convert the object into a dict
main_domain_contents_scriptalias_dict = main_domain_contents_scriptalias_instance.to_dict()
# create an instance of MainDomainContentsScriptalias from a dict
main_domain_contents_scriptalias_from_dict = MainDomainContentsScriptalias.from_dict(main_domain_contents_scriptalias_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


