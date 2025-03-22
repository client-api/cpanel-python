# MainDomainContentsCustomlog

The domain's [Apache log](http://httpd.apache.org/docs/2.2/mod/mod_log_config.html) information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** | **str** | The [log file](https://httpd.apache.org/docs/2.2/mod/mod_log_config.html#logformat)&#39;s format. | [optional] 
**target** | **str** | The absolute path to the domain&#39;s log file in the &#x60;domlogs&#x60; directory. | [optional] 

## Example

```python
from clientapi_cpanel.models.main_domain_contents_customlog import MainDomainContentsCustomlog

# TODO update the JSON string below
json = "{}"
# create an instance of MainDomainContentsCustomlog from a JSON string
main_domain_contents_customlog_instance = MainDomainContentsCustomlog.from_json(json)
# print the JSON string representation of the object
print(MainDomainContentsCustomlog.to_json())

# convert the object into a dict
main_domain_contents_customlog_dict = main_domain_contents_customlog_instance.to_dict()
# create an instance of MainDomainContentsCustomlog from a dict
main_domain_contents_customlog_from_dict = MainDomainContentsCustomlog.from_dict(main_domain_contents_customlog_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


