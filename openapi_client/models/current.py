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
from pydantic import BaseModel, StrictInt, StrictStr
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Current(BaseModel):
    """
    Current
    """ # noqa: E501
    hid: Optional[StrictStr] = None
    vid: Optional[StrictStr] = None
    nid: Optional[StrictStr] = None
    from_state: Optional[StrictStr] = None
    state: Optional[StrictStr] = None
    uid: Optional[StrictStr] = None
    stamp: Optional[StrictStr] = None
    published: Optional[StrictStr] = None
    is_current: Optional[StrictInt] = None
    title: Optional[StrictStr] = None
    timestamp: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["hid", "vid", "nid", "from_state", "state", "uid", "stamp", "published", "is_current", "title", "timestamp"]

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
        """Create an instance of Current from a JSON string"""
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
        # set to None if hid (nullable) is None
        # and model_fields_set contains the field
        if self.hid is None and "hid" in self.model_fields_set:
            _dict['hid'] = None

        # set to None if vid (nullable) is None
        # and model_fields_set contains the field
        if self.vid is None and "vid" in self.model_fields_set:
            _dict['vid'] = None

        # set to None if nid (nullable) is None
        # and model_fields_set contains the field
        if self.nid is None and "nid" in self.model_fields_set:
            _dict['nid'] = None

        # set to None if from_state (nullable) is None
        # and model_fields_set contains the field
        if self.from_state is None and "from_state" in self.model_fields_set:
            _dict['from_state'] = None

        # set to None if state (nullable) is None
        # and model_fields_set contains the field
        if self.state is None and "state" in self.model_fields_set:
            _dict['state'] = None

        # set to None if uid (nullable) is None
        # and model_fields_set contains the field
        if self.uid is None and "uid" in self.model_fields_set:
            _dict['uid'] = None

        # set to None if stamp (nullable) is None
        # and model_fields_set contains the field
        if self.stamp is None and "stamp" in self.model_fields_set:
            _dict['stamp'] = None

        # set to None if published (nullable) is None
        # and model_fields_set contains the field
        if self.published is None and "published" in self.model_fields_set:
            _dict['published'] = None

        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if timestamp (nullable) is None
        # and model_fields_set contains the field
        if self.timestamp is None and "timestamp" in self.model_fields_set:
            _dict['timestamp'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Current from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "hid": obj.get("hid"),
            "vid": obj.get("vid"),
            "nid": obj.get("nid"),
            "from_state": obj.get("from_state"),
            "state": obj.get("state"),
            "uid": obj.get("uid"),
            "stamp": obj.get("stamp"),
            "published": obj.get("published"),
            "is_current": obj.get("is_current"),
            "title": obj.get("title"),
            "timestamp": obj.get("timestamp")
        })
        return _obj


