# InlineResponse200191ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**diskquota** | **int** | The disk quota. * A positive value that represents the disk quota, in bytes. * &#x60;0&#x60; - The account possesses an unlimited disk quota. | [optional] 
**diskused** | **int** | The disk space that the email account uses. * A positive value that represents the used disk space, in bytes. * &#x60;0&#x60; - The account possesses an unlimited disk quota. | [optional] 
**diskquota** | [**InlineResponse200191ResultDataDiskquota**](InlineResponse200191ResultDataDiskquota.md) |  | [optional] 
**diskused** | **int** | The disk space that the email account uses. * A positive floating-point value that represents the used disk space, in megabytes (MB). * &#x60;0&#x60; - The account possesses an unlimited disk quota. | [optional] 
**diskusedpercent** | **int** | The percentage of disk space that the email account uses. * A positive value. * &#x60;0&#x60; - The account has an unlimited disk quota. | [optional] 
**diskusedpercent20** | **int** | The percentage of disk space that the email account uses. * A positive value. * &#x60;0&#x60; - The account possesses an unlimited disk quota. | [optional] 
**diskusedpercent_float** | **float** | The floating-point value from which the function derives the &#x60;diskusedpercent&#x60; return. * A floating-point value. * &#x60;0&#x60; - Unlimited or disabled disk quota.  **Note:**   The &#x60;diskusedpercent_float&#x60; number can contain scientific notation values. For example, &#x60;1.20494365692139e-05&#x60;. | [optional] 
**domain** | **str** | The email account&#39;s domain. For example, &#x60;example.com&#x60; if the email address is &#x60;user@example.com&#x60;. | [optional] 
**email** | [**InlineResponse200191ResultDataEmail**](InlineResponse200191ResultDataEmail.md) |  | [optional] 
**has_suspended** | **int** | Whether the email account possesses one of the following suspension parameters: &#x60;suspended_login&#x60; &#x60;suspended_incoming&#x60; &#x60;suspended_outgoing&#x60; &#x60;hold_outgoing&#x60; * &#x60;1&#x60; - The email account has a suspension. * &#x60;0&#x60; - The email account does **not** have a suspension.  **Note:**    The function **only** returns this value if you pass the &#x60;get_restrictions&#x3D;1&#x60; parameter. | [optional] 
**hold_outgoing** | **int** | Whether the email account&#39;s outgoing email is held in Exim&#39;s queue. * &#x60;1&#x60; - Outgoing email is held in Exim&#39;s queue. * &#x60;0&#x60; - Outgoing email is **not** held in Exim&#39;s queue.  **Note:**    The function **only** returns this value if you pass the &#x60;get_restrictions&#x3D;1&#x60; parameter. | [optional] 
**humandiskquota** | [**InlineResponse200191ResultDataHumandiskquota**](InlineResponse200191ResultDataHumandiskquota.md) |  | [optional] 
**humandiskused** | **str** | The disk space that the email account uses, in human-readable format. * The disk space that the email account uses, a non-breaking space (&#x60;\\u00a0&#x60;), and the unit of measure. * &#x60;None&#x60; - The account possesses an unlimited disk quota. | [optional] 
**login** | [**InlineResponse200191ResultDataLogin**](InlineResponse200191ResultDataLogin.md) |  | [optional] 
**mtime** | **int** | The email account&#39;s last modification time, in [Unix time](https://wikipedia.org/wiki/Unix_time) format. | [optional] 
**suspended_incoming** | **int** | Whether the email account&#39;s incoming email is suspended. * &#x60;1&#x60; - Suspended. * &#x60;0&#x60; - **Not** suspended. | [optional] 
**suspended_login** | **int** | Whether the user&#39;s ability to log in to, send mail from, and read their email account is suspended. * &#x60;1&#x60; - Suspended. * &#x60;0&#x60; - **Not** suspended. | [optional] 
**suspended_outgoing** | **int** | Whether the email account&#39;s outgoing email is suspended. * &#x60;1&#x60; - Suspended. * &#x60;0&#x60; - **Not** suspended. | [optional] 
**txtdiskquota** | [**InlineResponse200191ResultDataTxtdiskquota**](InlineResponse200191ResultDataTxtdiskquota.md) |  | [optional] 
**user** | **str** | The email account username. For example, &#x60;user&#x60; if the email address is &#x60;user@example.com&#x60;. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200191_result_data import InlineResponse200191ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200191ResultData from a JSON string
inline_response200191_result_data_instance = InlineResponse200191ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200191ResultData.to_json())

# convert the object into a dict
inline_response200191_result_data_dict = inline_response200191_result_data_instance.to_dict()
# create an instance of InlineResponse200191ResultData from a dict
inline_response200191_result_data_from_dict = InlineResponse200191ResultData.from_dict(inline_response200191_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


