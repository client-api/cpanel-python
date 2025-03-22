# InlineResponse200492ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **str** | The queried data&#39;s value. | [optional] 
**max** | **str** | The queried parameter&#39;s limit. | [optional] 
**maxed** | **int** | Whether the queried value reached its maximum value.  * &#x60;1&#x60; — Reached maximum value. * &#x60;0&#x60; — Has **not** reached maximum value. | [optional] 
**condition** | **int** | Whether the queried data&#39;s value possesses a conditional requirement.  * &#x60;1&#x60; — Possesses a condition. * &#x60;0&#x60; — Does **not** possess a condition.  **Note:**  The function will **only** return this value if it determines that the related statistic meets the subsystem installation requirements. | [optional] 
**count** | **str** | The queried data&#39;s value. | [optional] 
**feature** | **str** | The queried item&#39;s feature name. | [optional] 
**id** | **str** | The queried item&#39;s reference name. | [optional] 
**is_maxed** | **int** | Whether the queried value has reached its maximum value.  * &#x60;1&#x60; — The queried value has reached its maximum value. * &#x60;0&#x60; — The queried value has **not** reached its maximum value. | [optional] 
**item** | **str** | A human-readable version of the queried item. | [optional] 
**max** | **str** | The queried value&#39;s maximum limit. | [optional] 
**maxed_phrase** | **str** | The [&#x60;maketext&#x60;-formatted](https://go.cpanel.net/locale) message that the interface displays when the user reaches their maximum allowed value. | [optional] 
**module** | **str** | The module that retrieved the information. | [optional] 
**name** | **str** | The display key. | [optional] 
**near_limit_phrase** | **str** | The [&#x60;maketext&#x60;-formatted](https://go.cpanel.net/locale) message that the interface displays when the user approaches their maximum allowed value. | [optional] 
**normalized** | **int** | Whether the function normalized the output values.  * &#x60;1&#x60; — Normalized. * &#x60;0&#x60; — Did **not** normalize. | [optional] 
**percent** | **int** | The percentage of value, if applicable. | [optional] 
**percent10** | **int** | The percentage of value that the system rounds to the nearest ten, if applicable. | [optional] 
**percent20** | **int** | The percentage of value that the system rounds to the nearest twenty, if applicable. | [optional] 
**percent5** | **int** | The percentage of value that the system rounds to the nearest five, if applicable. | [optional] 
**phrase** | **str** | The human-readable name of the queried item. | [optional] 
**role** | **str** | The queried value&#39;s role.  * &#x60;CalendarContact&#x60; * &#x60;DNS&#x60; * &#x60;FileStorage&#x60; * &#x60;FTP&#x60; * &#x60;MailLocal&#x60; * &#x60;MailReceive&#x60; * &#x60;MailSend&#x60; * &#x60;MySQL&#x60; * &#x60;Postgres&#x60; * &#x60;SpamFilter&#x60; * &#x60;Webmail&#x60; * &#x60;WebDisk&#x60; * &#x60;WebServer&#x60; | [optional] 
**rowtype** | **str** | The queried value&#39;s row type.  * &#x60;even&#x60; * &#x60;odd&#x60; | [optional] 
**units** | **str** | The queried value&#39;s unit of measure. | [optional] 
**zeroisunlimited** | **int** | Whether a value of &#x60;0&#x60; means unlimited or zero.  * &#x60;1&#x60; — Unlimited. * &#x60;0&#x60; — Zero. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200492_result_data import InlineResponse200492ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200492ResultData from a JSON string
inline_response200492_result_data_instance = InlineResponse200492ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200492ResultData.to_json())

# convert the object into a dict
inline_response200492_result_data_dict = inline_response200492_result_data_instance.to_dict()
# create an instance of InlineResponse200492ResultData from a dict
inline_response200492_result_data_from_dict = InlineResponse200492ResultData.from_dict(inline_response200492_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


