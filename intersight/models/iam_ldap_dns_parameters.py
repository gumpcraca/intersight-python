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


class IamLdapDnsParameters(object):
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
        'search_domain': 'str',
        'search_forest': 'str',
        'source': 'str'
    }

    attribute_map = {
        'search_domain': 'SearchDomain',
        'search_forest': 'SearchForest',
        'source': 'Source'
    }

    def __init__(self, search_domain=None, search_forest=None, source='Extracted'):
        """
        IamLdapDnsParameters - a model defined in Swagger
        """

        self._search_domain = None
        self._search_forest = None
        self._source = None

        if search_domain is not None:
          self.search_domain = search_domain
        if search_forest is not None:
          self.search_forest = search_forest
        if source is not None:
          self.source = source

    @property
    def search_domain(self):
        """
        Gets the search_domain of this IamLdapDnsParameters.
        Domain name that acts as a source for a DNS query  

        :return: The search_domain of this IamLdapDnsParameters.
        :rtype: str
        """
        return self._search_domain

    @search_domain.setter
    def search_domain(self, search_domain):
        """
        Sets the search_domain of this IamLdapDnsParameters.
        Domain name that acts as a source for a DNS query  

        :param search_domain: The search_domain of this IamLdapDnsParameters.
        :type: str
        """

        self._search_domain = search_domain

    @property
    def search_forest(self):
        """
        Gets the search_forest of this IamLdapDnsParameters.
        Forest name that acts as a source for a DNS query  

        :return: The search_forest of this IamLdapDnsParameters.
        :rtype: str
        """
        return self._search_forest

    @search_forest.setter
    def search_forest(self, search_forest):
        """
        Sets the search_forest of this IamLdapDnsParameters.
        Forest name that acts as a source for a DNS query  

        :param search_forest: The search_forest of this IamLdapDnsParameters.
        :type: str
        """

        self._search_forest = search_forest

    @property
    def source(self):
        """
        Gets the source of this IamLdapDnsParameters.
        Specifies the source of the domain name used for the DNS SRV request   

        :return: The source of this IamLdapDnsParameters.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this IamLdapDnsParameters.
        Specifies the source of the domain name used for the DNS SRV request   

        :param source: The source of this IamLdapDnsParameters.
        :type: str
        """
        allowed_values = ["Extracted", "Configured", "ConfiguredExtracted"]
        if source not in allowed_values:
            raise ValueError(
                "Invalid value for `source` ({0}), must be one of {1}"
                .format(source, allowed_values)
            )

        self._source = source

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
        if not isinstance(other, IamLdapDnsParameters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
