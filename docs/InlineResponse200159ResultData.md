# InlineResponse200159ResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** | The contents of the autoresponder message&#39;s &#x60;Body&#x60; section. | [optional] 
**charset** | **str** | The autoresponder&#39;s [character set](https://en.wikipedia.org/wiki/Character_encoding). | [optional] 
**var_from** | **str** | The contents of the autoresponder message&#39;s &#x60;From&#x60; field. | [optional] 
**interval** | **int** | The amount of time, in hours, that the server waits between autoresponder messages to the same address.  **Note:**  A value of &#x60;0&#x60; indicates that the system sends a message for each email received. | [optional] 
**is_html** | **int** | Whether the body of the autoresponder message begins with an [HTML content type declaration](https://en.wikipedia.org/wiki/Character_encodings_in_HTML#Specifying_the_document.27s_character_encoding). - &#x60;1&#x60; - Includes an HTML content type declaration. - &#x60;0&#x60; - Does **not** include an HTML content type declaration. | [optional] 
**start** | **int** | When the autoresponder becomes enabled in Unix time. | [optional] 
**stop** | **int** | When the autoresponder becomes disabled in Unix time. | [optional] 
**subject** | **str** | The contents of the autoresponder message&#39;s &#x60;Subject&#x60; field. | [optional] 

## Example

```python
from clientapi_cpanel.models.inline_response200159_result_data import InlineResponse200159ResultData

# TODO update the JSON string below
json = "{}"
# create an instance of InlineResponse200159ResultData from a JSON string
inline_response200159_result_data_instance = InlineResponse200159ResultData.from_json(json)
# print the JSON string representation of the object
print(InlineResponse200159ResultData.to_json())

# convert the object into a dict
inline_response200159_result_data_dict = inline_response200159_result_data_instance.to_dict()
# create an instance of InlineResponse200159ResultData from a dict
inline_response200159_result_data_from_dict = InlineResponse200159ResultData.from_dict(inline_response200159_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


