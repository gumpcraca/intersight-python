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


class UcsdconnectorFieldQuery(object):
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
        'field_name': 'str',
        'query': 'UcsdconnectorSqlQuery'
    }

    attribute_map = {
        'field_name': 'FieldName',
        'query': 'Query'
    }

    def __init__(self, field_name=None, query=None):
        """
        UcsdconnectorFieldQuery - a model defined in Swagger
        """

        self._field_name = None
        self._query = None

        if field_name is not None:
          self.field_name = field_name
        if query is not None:
          self.query = query

    @property
    def field_name(self):
        """
        Gets the field_name of this UcsdconnectorFieldQuery.
        FieldName corresponds to property name of Fanwood Mo  

        :return: The field_name of this UcsdconnectorFieldQuery.
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        """
        Sets the field_name of this UcsdconnectorFieldQuery.
        FieldName corresponds to property name of Fanwood Mo  

        :param field_name: The field_name of this UcsdconnectorFieldQuery.
        :type: str
        """

        self._field_name = field_name

    @property
    def query(self):
        """
        Gets the query of this UcsdconnectorFieldQuery.
        SQL query string   

        :return: The query of this UcsdconnectorFieldQuery.
        :rtype: UcsdconnectorSqlQuery
        """
        return self._query

    @query.setter
    def query(self, query):
        """
        Sets the query of this UcsdconnectorFieldQuery.
        SQL query string   

        :param query: The query of this UcsdconnectorFieldQuery.
        :type: UcsdconnectorSqlQuery
        """

        self._query = query

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
        if not isinstance(other, UcsdconnectorFieldQuery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
