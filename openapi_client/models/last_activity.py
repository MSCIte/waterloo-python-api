# coding: utf-8

"""
    Waterloo OpenData API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class LastActivity(BaseModel):
    """
    LastActivity
    """ # noqa: E501
    predicates: Optional[List[StrictStr]] = None
    datatype: Optional[StrictStr] = None
    callback: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["predicates", "datatype", "callback"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of LastActivity from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # set to None if predicates (nullable) is None
        # and model_fields_set contains the field
        if self.predicates is None and "predicates" in self.model_fields_set:
            _dict['predicates'] = None

        # set to None if datatype (nullable) is None
        # and model_fields_set contains the field
        if self.datatype is None and "datatype" in self.model_fields_set:
            _dict['datatype'] = None

        # set to None if callback (nullable) is None
        # and model_fields_set contains the field
        if self.callback is None and "callback" in self.model_fields_set:
            _dict['callback'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of LastActivity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "predicates": obj.get("predicates"),
            "datatype": obj.get("datatype"),
            "callback": obj.get("callback")
        })
        return _obj


