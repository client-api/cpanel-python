# InlineResponse200254ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**diskquota** | **str** | The FTP account&#39;s quota in megabytes, with two digits of fractional precision, encoded as a string. &#x60;0.00&#x60; means that the quota is unlimited.  **Note:**  This value is different from the value for &#x60;diskquota&#x60;. | [optional] 
**diskused** | **str** | The amount of disk space in megabytes that the account currently uses, with two digits of fractional precision, encoded as a string.  **Note:**  This value is the same as the value for &#x60;diskused&#x60;. | [optional] 
**accttype** | **str** | The type of FTP account.  * &#x60;anonymous&#x60; * &#x60;logaccess&#x60; * &#x60;main&#x60; * &#x60;sub&#x60; | [optional] 
**deleteable** | **int** | Whether the function&#39;s caller can delete the account.  * &#x60;1&#x60; – The caller can delete the account. * &#x60;0&#x60; – The caller **cannot** delete the account. | [optional] 
**dir** | **str** | The absolute path to the FTP account&#39;s document root. | [optional] 
**diskquota** | [**InlineResponse200254ResultDataDiskquota**](InlineResponse200254ResultDataDiskquota.md) |  | [optional] 
**diskused** | **str** | The amount of disk space in megabytes that the account currently uses, with two digits of fractional precision, encoded as a string.  **Note:**  This value is the same as the value for &#x60;_diskused&#x60;. | [optional] 
**diskusedpercent** | **int** | The percentage of the disk space quota that the account currently uses. | [optional] 
**diskusedpercent20** | **int** | The percentage of disk space that the account currently uses, rounded in 20 percent increments. | [optional] 
**htmldir** | **str** | The path to the FTP account&#39;s HTML directory. | [optional] 
**humandiskquota** | **str** | The FTP account&#39;s quota, in human-readable format.  * &#x60;None&#x60; — The function returns this value if the account has an unlimited quota. * The quota in megabytes (MB), a space, and the characters &#x60;MB&#x60;. | [optional] 
**humandiskused** | **str** | The amount of disk space that the account currently uses, in human-readable format. The function formats this value as the quota&#39;s size, a space, and the characters &#x60;MB&#x60;. | [optional] 
**login** | **str** | The FTP account username. | [optional] 
**reldir** | **str** | The path to the FTP account&#39;s document root, relative to the cPanel account&#39;s home directory. | [optional] 
**serverlogin** | **str** | The full FTP login username. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200254_result_data import InlineResponse200254ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200254ResultData from a JSON string
inline_response200254_result_data_instance = InlineResponse200254ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200254ResultData.to_json())

# convert the object into a dict
inline_response200254_result_data_dict = inline_response200254_result_data_instance.to_dict()
# create an instance of InlineResponse200254ResultData from a dict
inline_response200254_result_data_from_dict = InlineResponse200254ResultData.from_dict(inline_response200254_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


