# coding: utf-8

"""
    Intersight REST API

    This is Intersight REST API 

    OpenAPI spec version: 1.0.9-255
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class NotifsCondition(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'change_set': 'list[str]',
        'change_type': 'str',
        'filter': 'str'
    }

    attribute_map = {
        'change_set': 'ChangeSet',
        'change_type': 'ChangeType',
        'filter': 'Filter'
    }

    def __init__(self, change_set=None, change_type='Update', filter=None):
        """
        NotifsCondition - a model defined in Swagger
        """

        self._change_set = None
        self._change_type = None
        self._filter = None

        if change_set is not None:
          self.change_set = change_set
        if change_type is not None:
          self.change_type = change_type
        if filter is not None:
          self.filter = filter

    @property
    def change_set(self):
        """
        Gets the change_set of this NotifsCondition.
        A list of properties which have been modified on an MO in a transaction. Applicable only for MO updates, ignored for creation/deletion. Evaluates to True if any of the listed properties has changed or if the list is empty. Eg: ConnectorStatus,ConnectorVersion 

        :return: The change_set of this NotifsCondition.
        :rtype: list[str]
        """
        return self._change_set

    @change_set.setter
    def change_set(self, change_set):
        """
        Sets the change_set of this NotifsCondition.
        A list of properties which have been modified on an MO in a transaction. Applicable only for MO updates, ignored for creation/deletion. Evaluates to True if any of the listed properties has changed or if the list is empty. Eg: ConnectorStatus,ConnectorVersion 

        :param change_set: The change_set of this NotifsCondition.
        :type: list[str]
        """

        self._change_set = change_set

    @property
    def change_type(self):
        """
        Gets the change_type of this NotifsCondition.
        Indicates the type of change (create, update, delete) performed on the MO. 

        :return: The change_type of this NotifsCondition.
        :rtype: str
        """
        return self._change_type

    @change_type.setter
    def change_type(self, change_type):
        """
        Sets the change_type of this NotifsCondition.
        Indicates the type of change (create, update, delete) performed on the MO. 

        :param change_type: The change_type of this NotifsCondition.
        :type: str
        """
        allowed_values = ["Update", "Create", "Delete"]
        if change_type not in allowed_values:
            raise ValueError(
                "Invalid value for `change_type` ({0}), must be one of {1}"
                .format(change_type, allowed_values)
            )

        self._change_type = change_type

    @property
    def filter(self):
        """
        Gets the filter of this NotifsCondition.
        An Odata-style filter which is evaluated against the state of an MO at the time of transaction commit. An empty filter string evaluates to True. Eg: ConnectionStatus eq 'Connected' 

        :return: The filter of this NotifsCondition.
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """
        Sets the filter of this NotifsCondition.
        An Odata-style filter which is evaluated against the state of an MO at the time of transaction commit. An empty filter string evaluates to True. Eg: ConnectionStatus eq 'Connected' 

        :param filter: The filter of this NotifsCondition.
        :type: str
        """

        self._filter = filter

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, NotifsCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
