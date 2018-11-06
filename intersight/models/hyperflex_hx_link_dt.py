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


class HyperflexHxLinkDt(object):
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
        'comments': 'str',
        'href': 'str',
        'method': 'str',
        'rel': 'str'
    }

    attribute_map = {
        'comments': 'Comments',
        'href': 'Href',
        'method': 'Method',
        'rel': 'Rel'
    }

    def __init__(self, comments=None, href=None, method='POST', rel=None):
        """
        HyperflexHxLinkDt - a model defined in Swagger
        """

        self._comments = None
        self._href = None
        self._method = None
        self._rel = None

        if comments is not None:
          self.comments = comments
        if href is not None:
          self.href = href
        if method is not None:
          self.method = method
        if rel is not None:
          self.rel = rel

    @property
    def comments(self):
        """
        Gets the comments of this HyperflexHxLinkDt.

        :return: The comments of this HyperflexHxLinkDt.
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """
        Sets the comments of this HyperflexHxLinkDt.

        :param comments: The comments of this HyperflexHxLinkDt.
        :type: str
        """

        self._comments = comments

    @property
    def href(self):
        """
        Gets the href of this HyperflexHxLinkDt.

        :return: The href of this HyperflexHxLinkDt.
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """
        Sets the href of this HyperflexHxLinkDt.

        :param href: The href of this HyperflexHxLinkDt.
        :type: str
        """

        self._href = href

    @property
    def method(self):
        """
        Gets the method of this HyperflexHxLinkDt.

        :return: The method of this HyperflexHxLinkDt.
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """
        Sets the method of this HyperflexHxLinkDt.

        :param method: The method of this HyperflexHxLinkDt.
        :type: str
        """
        allowed_values = ["POST", "GET", "PUT", "DELETE"]
        if method not in allowed_values:
            raise ValueError(
                "Invalid value for `method` ({0}), must be one of {1}"
                .format(method, allowed_values)
            )

        self._method = method

    @property
    def rel(self):
        """
        Gets the rel of this HyperflexHxLinkDt.

        :return: The rel of this HyperflexHxLinkDt.
        :rtype: str
        """
        return self._rel

    @rel.setter
    def rel(self, rel):
        """
        Sets the rel of this HyperflexHxLinkDt.

        :param rel: The rel of this HyperflexHxLinkDt.
        :type: str
        """

        self._rel = rel

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
        if not isinstance(other, HyperflexHxLinkDt):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
