# InlineResponse200187ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accesstype** | **str** | The level of access that users have to the mailing list. * &#x60;private&#x60; - The list has **all** of the following settings:   * The list has private archives.   * The administrator **must** approve subscriptions.   * The Mailman directory page does **not** display the list. * &#x60;public&#x60; - The list has **any** of the following settings:   * The list has public archives.   * Anyone can subscribe.   * The Mailman directory page displays the list. | [optional] 
**advertised** | **int** | Whether the Mailman directory page displays the list. * &#x60;1&#x60; - The Mailman directory page displays the list. * &#x60;0&#x60; - The Mailman directory page does not display the list. | [optional] 
**archive_private** | **int** | Whether the mailing list archive is &#x60;private&#x60;. * &#x60;1&#x60; - The mailing list archive is &#x60;private&#x60;. * &#x60;0&#x60; - The mailing list archive is &#x60;public&#x60;. | [optional] 
**desthost** | [**InlineResponse200187ResultDataDesthost**](InlineResponse200187ResultDataDesthost.md) |  | [optional] 
**diskused** | **int** | The disk space that the mailing list currently uses, measured in megabytes (MB). | [optional] 
**humandiskused** | **str** | The disk space that the mailing list uses, in human-readable format. | [optional] 
**list** | **str** | The mailing list name and domain. | [optional] 
**listadmin** | **str** | The mailing list&#39;s administrators&#39; email addresses. A comma-separated list of email addresses. | [optional] 
**listid** | **str** | The mailing list&#39;s name and domain. The mailing list name, an underscore (_), and the domain. | [optional] 
**subscribe_policy** | **int** | The level of control that the mailing list administrator has over new subscribers. * &#x60;1&#x60; - Anyone can subscribe. The system sends a confirmation email. * &#x60;2&#x60; - The administrator **must** approve subscriptions. The system does **not** send a confirmation email. * &#x60;3&#x60; - The administrator **must** approve subscriptions. The system sends a confirmation email. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200187_result_data import InlineResponse200187ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200187ResultData from a JSON string
inline_response200187_result_data_instance = InlineResponse200187ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200187ResultData.to_json())

# convert the object into a dict
inline_response200187_result_data_dict = inline_response200187_result_data_instance.to_dict()
# create an instance of InlineResponse200187ResultData from a dict
inline_response200187_result_data_from_dict = InlineResponse200187ResultData.from_dict(inline_response200187_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


