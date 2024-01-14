# PaymentAccepted


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tid** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.payment_accepted import PaymentAccepted

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentAccepted from a JSON string
payment_accepted_instance = PaymentAccepted.from_json(json)
# print the JSON string representation of the object
print PaymentAccepted.to_json()

# convert the object into a dict
payment_accepted_dict = payment_accepted_instance.to_dict()
# create an instance of PaymentAccepted from a dict
payment_accepted_form_dict = payment_accepted.from_dict(payment_accepted_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


