# coding: utf-8

"""
    Intersight REST API

    This is Intersight REST API 

    OpenAPI spec version: 1.0.5-612
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class InventoryJobInfo(object):
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
        'execution_status': 'str',
        'job_name': 'str',
        'last_processed_time': 'datetime',
        'last_scheduled_time': 'datetime',
        'properties': 'list[str]',
        'regex': 'list[str]'
    }

    attribute_map = {
        'execution_status': 'ExecutionStatus',
        'job_name': 'JobName',
        'last_processed_time': 'LastProcessedTime',
        'last_scheduled_time': 'LastScheduledTime',
        'properties': 'Properties',
        'regex': 'Regex'
    }

    def __init__(self, execution_status='Unknown', job_name=None, last_processed_time=None, last_scheduled_time=None, properties=None, regex=None):
        """
        InventoryJobInfo - a model defined in Swagger
        """

        self._execution_status = None
        self._job_name = None
        self._last_processed_time = None
        self._last_scheduled_time = None
        self._properties = None
        self._regex = None

        if execution_status is not None:
          self.execution_status = execution_status
        if job_name is not None:
          self.job_name = job_name
        if last_processed_time is not None:
          self.last_processed_time = last_processed_time
        if last_scheduled_time is not None:
          self.last_scheduled_time = last_scheduled_time
        if properties is not None:
          self.properties = properties
        if regex is not None:
          self.regex = regex

    @property
    def execution_status(self):
        """
        Gets the execution_status of this InventoryJobInfo.

        :return: The execution_status of this InventoryJobInfo.
        :rtype: str
        """
        return self._execution_status

    @execution_status.setter
    def execution_status(self, execution_status):
        """
        Sets the execution_status of this InventoryJobInfo.

        :param execution_status: The execution_status of this InventoryJobInfo.
        :type: str
        """
        allowed_values = ["Unknown", "Scheduled", "Completed", "Error"]
        if execution_status not in allowed_values:
            raise ValueError(
                "Invalid value for `execution_status` ({0}), must be one of {1}"
                .format(execution_status, allowed_values)
            )

        self._execution_status = execution_status

    @property
    def job_name(self):
        """
        Gets the job_name of this InventoryJobInfo.

        :return: The job_name of this InventoryJobInfo.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """
        Sets the job_name of this InventoryJobInfo.

        :param job_name: The job_name of this InventoryJobInfo.
        :type: str
        """

        self._job_name = job_name

    @property
    def last_processed_time(self):
        """
        Gets the last_processed_time of this InventoryJobInfo.

        :return: The last_processed_time of this InventoryJobInfo.
        :rtype: datetime
        """
        return self._last_processed_time

    @last_processed_time.setter
    def last_processed_time(self, last_processed_time):
        """
        Sets the last_processed_time of this InventoryJobInfo.

        :param last_processed_time: The last_processed_time of this InventoryJobInfo.
        :type: datetime
        """

        self._last_processed_time = last_processed_time

    @property
    def last_scheduled_time(self):
        """
        Gets the last_scheduled_time of this InventoryJobInfo.

        :return: The last_scheduled_time of this InventoryJobInfo.
        :rtype: datetime
        """
        return self._last_scheduled_time

    @last_scheduled_time.setter
    def last_scheduled_time(self, last_scheduled_time):
        """
        Sets the last_scheduled_time of this InventoryJobInfo.

        :param last_scheduled_time: The last_scheduled_time of this InventoryJobInfo.
        :type: datetime
        """

        self._last_scheduled_time = last_scheduled_time

    @property
    def properties(self):
        """
        Gets the properties of this InventoryJobInfo.

        :return: The properties of this InventoryJobInfo.
        :rtype: list[str]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this InventoryJobInfo.

        :param properties: The properties of this InventoryJobInfo.
        :type: list[str]
        """

        self._properties = properties

    @property
    def regex(self):
        """
        Gets the regex of this InventoryJobInfo.

        :return: The regex of this InventoryJobInfo.
        :rtype: list[str]
        """
        return self._regex

    @regex.setter
    def regex(self, regex):
        """
        Sets the regex of this InventoryJobInfo.

        :param regex: The regex of this InventoryJobInfo.
        :type: list[str]
        """

        self._regex = regex

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
        if not isinstance(other, InventoryJobInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
