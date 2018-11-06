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


class IamEndPointPasswordProperties(object):
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
        'enable_password_expiry': 'bool',
        'enforce_strong_password': 'bool',
        'grace_period': 'int',
        'notification_period': 'int',
        'password_expiry_duration': 'int',
        'password_history': 'int'
    }

    attribute_map = {
        'enable_password_expiry': 'EnablePasswordExpiry',
        'enforce_strong_password': 'EnforceStrongPassword',
        'grace_period': 'GracePeriod',
        'notification_period': 'NotificationPeriod',
        'password_expiry_duration': 'PasswordExpiryDuration',
        'password_history': 'PasswordHistory'
    }

    def __init__(self, enable_password_expiry=None, enforce_strong_password=None, grace_period=None, notification_period=None, password_expiry_duration=None, password_history=None):
        """
        IamEndPointPasswordProperties - a model defined in Swagger
        """

        self._enable_password_expiry = None
        self._enforce_strong_password = None
        self._grace_period = None
        self._notification_period = None
        self._password_expiry_duration = None
        self._password_history = None

        if enable_password_expiry is not None:
          self.enable_password_expiry = enable_password_expiry
        if enforce_strong_password is not None:
          self.enforce_strong_password = enforce_strong_password
        if grace_period is not None:
          self.grace_period = grace_period
        if notification_period is not None:
          self.notification_period = notification_period
        if password_expiry_duration is not None:
          self.password_expiry_duration = password_expiry_duration
        if password_history is not None:
          self.password_history = password_history

    @property
    def enable_password_expiry(self):
        """
        Gets the enable_password_expiry of this IamEndPointPasswordProperties.
        Enables password expiry on the endpoint  

        :return: The enable_password_expiry of this IamEndPointPasswordProperties.
        :rtype: bool
        """
        return self._enable_password_expiry

    @enable_password_expiry.setter
    def enable_password_expiry(self, enable_password_expiry):
        """
        Sets the enable_password_expiry of this IamEndPointPasswordProperties.
        Enables password expiry on the endpoint  

        :param enable_password_expiry: The enable_password_expiry of this IamEndPointPasswordProperties.
        :type: bool
        """

        self._enable_password_expiry = enable_password_expiry

    @property
    def enforce_strong_password(self):
        """
        Gets the enforce_strong_password of this IamEndPointPasswordProperties.
        Enables a strong password policy Strong password requirements: A. The password must have a minimum of 8 and a maximum of 20 characters. B. The password must not contain the User's Name. C. The password must contain characters from three of the following four categories. 1) English uppercase characters (A through Z). 2) English lowercase characters (a through z). 3) Base 10 digits (0 through 9). 4) Non-alphabetic characters (!, @, #, $, %, ^, &, *, -, _, +, =). 

        :return: The enforce_strong_password of this IamEndPointPasswordProperties.
        :rtype: bool
        """
        return self._enforce_strong_password

    @enforce_strong_password.setter
    def enforce_strong_password(self, enforce_strong_password):
        """
        Sets the enforce_strong_password of this IamEndPointPasswordProperties.
        Enables a strong password policy Strong password requirements: A. The password must have a minimum of 8 and a maximum of 20 characters. B. The password must not contain the User's Name. C. The password must contain characters from three of the following four categories. 1) English uppercase characters (A through Z). 2) English lowercase characters (a through z). 3) Base 10 digits (0 through 9). 4) Non-alphabetic characters (!, @, #, $, %, ^, &, *, -, _, +, =). 

        :param enforce_strong_password: The enforce_strong_password of this IamEndPointPasswordProperties.
        :type: bool
        """

        self._enforce_strong_password = enforce_strong_password

    @property
    def grace_period(self):
        """
        Gets the grace_period of this IamEndPointPasswordProperties.
        Time period until when you can use the existing password, after it expires  

        :return: The grace_period of this IamEndPointPasswordProperties.
        :rtype: int
        """
        return self._grace_period

    @grace_period.setter
    def grace_period(self, grace_period):
        """
        Sets the grace_period of this IamEndPointPasswordProperties.
        Time period until when you can use the existing password, after it expires  

        :param grace_period: The grace_period of this IamEndPointPasswordProperties.
        :type: int
        """

        self._grace_period = grace_period

    @property
    def notification_period(self):
        """
        Gets the notification_period of this IamEndPointPasswordProperties.
        Specifies the duration by when the password will expire  

        :return: The notification_period of this IamEndPointPasswordProperties.
        :rtype: int
        """
        return self._notification_period

    @notification_period.setter
    def notification_period(self, notification_period):
        """
        Sets the notification_period of this IamEndPointPasswordProperties.
        Specifies the duration by when the password will expire  

        :param notification_period: The notification_period of this IamEndPointPasswordProperties.
        :type: int
        """

        self._notification_period = notification_period

    @property
    def password_expiry_duration(self):
        """
        Gets the password_expiry_duration of this IamEndPointPasswordProperties.
        Set time period for password expiration. Value should be greater than notification period and grace period.  

        :return: The password_expiry_duration of this IamEndPointPasswordProperties.
        :rtype: int
        """
        return self._password_expiry_duration

    @password_expiry_duration.setter
    def password_expiry_duration(self, password_expiry_duration):
        """
        Sets the password_expiry_duration of this IamEndPointPasswordProperties.
        Set time period for password expiration. Value should be greater than notification period and grace period.  

        :param password_expiry_duration: The password_expiry_duration of this IamEndPointPasswordProperties.
        :type: int
        """

        self._password_expiry_duration = password_expiry_duration

    @property
    def password_history(self):
        """
        Gets the password_history of this IamEndPointPasswordProperties.
        Tracks password change history. Specifies in number of instances, that the new password was already used.   

        :return: The password_history of this IamEndPointPasswordProperties.
        :rtype: int
        """
        return self._password_history

    @password_history.setter
    def password_history(self, password_history):
        """
        Sets the password_history of this IamEndPointPasswordProperties.
        Tracks password change history. Specifies in number of instances, that the new password was already used.   

        :param password_history: The password_history of this IamEndPointPasswordProperties.
        :type: int
        """

        self._password_history = password_history

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
        if not isinstance(other, IamEndPointPasswordProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
