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


class HyperflexSummary(object):
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
        'active_nodes': 'str',
        'address': 'str',
        'boottime': 'int',
        'cluster_access_policy': 'str',
        'compression_savings': 'float',
        'data_replication_compliance': 'str',
        'data_replication_factor': 'str',
        'deduplication_savings': 'float',
        'downtime': 'str',
        'free_capacity': 'int',
        'healing_info': 'HyperflexStPlatformClusterHealingInfo',
        'name': 'str',
        'resiliency_details': 'object',
        'resiliency_details_size': 'int',
        'resiliency_info': 'HyperflexStPlatformClusterResiliencyInfo',
        'space_status': 'str',
        'state': 'str',
        'total_capacity': 'int',
        'total_savings': 'float',
        'uptime': 'str',
        'used_capacity': 'int'
    }

    attribute_map = {
        'active_nodes': 'ActiveNodes',
        'address': 'Address',
        'boottime': 'Boottime',
        'cluster_access_policy': 'ClusterAccessPolicy',
        'compression_savings': 'CompressionSavings',
        'data_replication_compliance': 'DataReplicationCompliance',
        'data_replication_factor': 'DataReplicationFactor',
        'deduplication_savings': 'DeduplicationSavings',
        'downtime': 'Downtime',
        'free_capacity': 'FreeCapacity',
        'healing_info': 'HealingInfo',
        'name': 'Name',
        'resiliency_details': 'ResiliencyDetails',
        'resiliency_details_size': 'ResiliencyDetailsSize',
        'resiliency_info': 'ResiliencyInfo',
        'space_status': 'SpaceStatus',
        'state': 'State',
        'total_capacity': 'TotalCapacity',
        'total_savings': 'TotalSavings',
        'uptime': 'Uptime',
        'used_capacity': 'UsedCapacity'
    }

    def __init__(self, active_nodes=None, address=None, boottime=None, cluster_access_policy=None, compression_savings=None, data_replication_compliance=None, data_replication_factor=None, deduplication_savings=None, downtime=None, free_capacity=None, healing_info=None, name=None, resiliency_details=None, resiliency_details_size=None, resiliency_info=None, space_status=None, state=None, total_capacity=None, total_savings=None, uptime=None, used_capacity=None):
        """
        HyperflexSummary - a model defined in Swagger
        """

        self._active_nodes = None
        self._address = None
        self._boottime = None
        self._cluster_access_policy = None
        self._compression_savings = None
        self._data_replication_compliance = None
        self._data_replication_factor = None
        self._deduplication_savings = None
        self._downtime = None
        self._free_capacity = None
        self._healing_info = None
        self._name = None
        self._resiliency_details = None
        self._resiliency_details_size = None
        self._resiliency_info = None
        self._space_status = None
        self._state = None
        self._total_capacity = None
        self._total_savings = None
        self._uptime = None
        self._used_capacity = None

        if active_nodes is not None:
          self.active_nodes = active_nodes
        if address is not None:
          self.address = address
        if boottime is not None:
          self.boottime = boottime
        if cluster_access_policy is not None:
          self.cluster_access_policy = cluster_access_policy
        if compression_savings is not None:
          self.compression_savings = compression_savings
        if data_replication_compliance is not None:
          self.data_replication_compliance = data_replication_compliance
        if data_replication_factor is not None:
          self.data_replication_factor = data_replication_factor
        if deduplication_savings is not None:
          self.deduplication_savings = deduplication_savings
        if downtime is not None:
          self.downtime = downtime
        if free_capacity is not None:
          self.free_capacity = free_capacity
        if healing_info is not None:
          self.healing_info = healing_info
        if name is not None:
          self.name = name
        if resiliency_details is not None:
          self.resiliency_details = resiliency_details
        if resiliency_details_size is not None:
          self.resiliency_details_size = resiliency_details_size
        if resiliency_info is not None:
          self.resiliency_info = resiliency_info
        if space_status is not None:
          self.space_status = space_status
        if state is not None:
          self.state = state
        if total_capacity is not None:
          self.total_capacity = total_capacity
        if total_savings is not None:
          self.total_savings = total_savings
        if uptime is not None:
          self.uptime = uptime
        if used_capacity is not None:
          self.used_capacity = used_capacity

    @property
    def active_nodes(self):
        """
        Gets the active_nodes of this HyperflexSummary.

        :return: The active_nodes of this HyperflexSummary.
        :rtype: str
        """
        return self._active_nodes

    @active_nodes.setter
    def active_nodes(self, active_nodes):
        """
        Sets the active_nodes of this HyperflexSummary.

        :param active_nodes: The active_nodes of this HyperflexSummary.
        :type: str
        """

        self._active_nodes = active_nodes

    @property
    def address(self):
        """
        Gets the address of this HyperflexSummary.

        :return: The address of this HyperflexSummary.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets the address of this HyperflexSummary.

        :param address: The address of this HyperflexSummary.
        :type: str
        """

        self._address = address

    @property
    def boottime(self):
        """
        Gets the boottime of this HyperflexSummary.

        :return: The boottime of this HyperflexSummary.
        :rtype: int
        """
        return self._boottime

    @boottime.setter
    def boottime(self, boottime):
        """
        Sets the boottime of this HyperflexSummary.

        :param boottime: The boottime of this HyperflexSummary.
        :type: int
        """

        self._boottime = boottime

    @property
    def cluster_access_policy(self):
        """
        Gets the cluster_access_policy of this HyperflexSummary.

        :return: The cluster_access_policy of this HyperflexSummary.
        :rtype: str
        """
        return self._cluster_access_policy

    @cluster_access_policy.setter
    def cluster_access_policy(self, cluster_access_policy):
        """
        Sets the cluster_access_policy of this HyperflexSummary.

        :param cluster_access_policy: The cluster_access_policy of this HyperflexSummary.
        :type: str
        """

        self._cluster_access_policy = cluster_access_policy

    @property
    def compression_savings(self):
        """
        Gets the compression_savings of this HyperflexSummary.

        :return: The compression_savings of this HyperflexSummary.
        :rtype: float
        """
        return self._compression_savings

    @compression_savings.setter
    def compression_savings(self, compression_savings):
        """
        Sets the compression_savings of this HyperflexSummary.

        :param compression_savings: The compression_savings of this HyperflexSummary.
        :type: float
        """

        self._compression_savings = compression_savings

    @property
    def data_replication_compliance(self):
        """
        Gets the data_replication_compliance of this HyperflexSummary.

        :return: The data_replication_compliance of this HyperflexSummary.
        :rtype: str
        """
        return self._data_replication_compliance

    @data_replication_compliance.setter
    def data_replication_compliance(self, data_replication_compliance):
        """
        Sets the data_replication_compliance of this HyperflexSummary.

        :param data_replication_compliance: The data_replication_compliance of this HyperflexSummary.
        :type: str
        """

        self._data_replication_compliance = data_replication_compliance

    @property
    def data_replication_factor(self):
        """
        Gets the data_replication_factor of this HyperflexSummary.

        :return: The data_replication_factor of this HyperflexSummary.
        :rtype: str
        """
        return self._data_replication_factor

    @data_replication_factor.setter
    def data_replication_factor(self, data_replication_factor):
        """
        Sets the data_replication_factor of this HyperflexSummary.

        :param data_replication_factor: The data_replication_factor of this HyperflexSummary.
        :type: str
        """

        self._data_replication_factor = data_replication_factor

    @property
    def deduplication_savings(self):
        """
        Gets the deduplication_savings of this HyperflexSummary.

        :return: The deduplication_savings of this HyperflexSummary.
        :rtype: float
        """
        return self._deduplication_savings

    @deduplication_savings.setter
    def deduplication_savings(self, deduplication_savings):
        """
        Sets the deduplication_savings of this HyperflexSummary.

        :param deduplication_savings: The deduplication_savings of this HyperflexSummary.
        :type: float
        """

        self._deduplication_savings = deduplication_savings

    @property
    def downtime(self):
        """
        Gets the downtime of this HyperflexSummary.

        :return: The downtime of this HyperflexSummary.
        :rtype: str
        """
        return self._downtime

    @downtime.setter
    def downtime(self, downtime):
        """
        Sets the downtime of this HyperflexSummary.

        :param downtime: The downtime of this HyperflexSummary.
        :type: str
        """

        self._downtime = downtime

    @property
    def free_capacity(self):
        """
        Gets the free_capacity of this HyperflexSummary.

        :return: The free_capacity of this HyperflexSummary.
        :rtype: int
        """
        return self._free_capacity

    @free_capacity.setter
    def free_capacity(self, free_capacity):
        """
        Sets the free_capacity of this HyperflexSummary.

        :param free_capacity: The free_capacity of this HyperflexSummary.
        :type: int
        """

        self._free_capacity = free_capacity

    @property
    def healing_info(self):
        """
        Gets the healing_info of this HyperflexSummary.

        :return: The healing_info of this HyperflexSummary.
        :rtype: HyperflexStPlatformClusterHealingInfo
        """
        return self._healing_info

    @healing_info.setter
    def healing_info(self, healing_info):
        """
        Sets the healing_info of this HyperflexSummary.

        :param healing_info: The healing_info of this HyperflexSummary.
        :type: HyperflexStPlatformClusterHealingInfo
        """

        self._healing_info = healing_info

    @property
    def name(self):
        """
        Gets the name of this HyperflexSummary.

        :return: The name of this HyperflexSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this HyperflexSummary.

        :param name: The name of this HyperflexSummary.
        :type: str
        """

        self._name = name

    @property
    def resiliency_details(self):
        """
        Gets the resiliency_details of this HyperflexSummary.

        :return: The resiliency_details of this HyperflexSummary.
        :rtype: object
        """
        return self._resiliency_details

    @resiliency_details.setter
    def resiliency_details(self, resiliency_details):
        """
        Sets the resiliency_details of this HyperflexSummary.

        :param resiliency_details: The resiliency_details of this HyperflexSummary.
        :type: object
        """

        self._resiliency_details = resiliency_details

    @property
    def resiliency_details_size(self):
        """
        Gets the resiliency_details_size of this HyperflexSummary.

        :return: The resiliency_details_size of this HyperflexSummary.
        :rtype: int
        """
        return self._resiliency_details_size

    @resiliency_details_size.setter
    def resiliency_details_size(self, resiliency_details_size):
        """
        Sets the resiliency_details_size of this HyperflexSummary.

        :param resiliency_details_size: The resiliency_details_size of this HyperflexSummary.
        :type: int
        """

        self._resiliency_details_size = resiliency_details_size

    @property
    def resiliency_info(self):
        """
        Gets the resiliency_info of this HyperflexSummary.

        :return: The resiliency_info of this HyperflexSummary.
        :rtype: HyperflexStPlatformClusterResiliencyInfo
        """
        return self._resiliency_info

    @resiliency_info.setter
    def resiliency_info(self, resiliency_info):
        """
        Sets the resiliency_info of this HyperflexSummary.

        :param resiliency_info: The resiliency_info of this HyperflexSummary.
        :type: HyperflexStPlatformClusterResiliencyInfo
        """

        self._resiliency_info = resiliency_info

    @property
    def space_status(self):
        """
        Gets the space_status of this HyperflexSummary.

        :return: The space_status of this HyperflexSummary.
        :rtype: str
        """
        return self._space_status

    @space_status.setter
    def space_status(self, space_status):
        """
        Sets the space_status of this HyperflexSummary.

        :param space_status: The space_status of this HyperflexSummary.
        :type: str
        """

        self._space_status = space_status

    @property
    def state(self):
        """
        Gets the state of this HyperflexSummary.

        :return: The state of this HyperflexSummary.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this HyperflexSummary.

        :param state: The state of this HyperflexSummary.
        :type: str
        """

        self._state = state

    @property
    def total_capacity(self):
        """
        Gets the total_capacity of this HyperflexSummary.

        :return: The total_capacity of this HyperflexSummary.
        :rtype: int
        """
        return self._total_capacity

    @total_capacity.setter
    def total_capacity(self, total_capacity):
        """
        Sets the total_capacity of this HyperflexSummary.

        :param total_capacity: The total_capacity of this HyperflexSummary.
        :type: int
        """

        self._total_capacity = total_capacity

    @property
    def total_savings(self):
        """
        Gets the total_savings of this HyperflexSummary.

        :return: The total_savings of this HyperflexSummary.
        :rtype: float
        """
        return self._total_savings

    @total_savings.setter
    def total_savings(self, total_savings):
        """
        Sets the total_savings of this HyperflexSummary.

        :param total_savings: The total_savings of this HyperflexSummary.
        :type: float
        """

        self._total_savings = total_savings

    @property
    def uptime(self):
        """
        Gets the uptime of this HyperflexSummary.

        :return: The uptime of this HyperflexSummary.
        :rtype: str
        """
        return self._uptime

    @uptime.setter
    def uptime(self, uptime):
        """
        Sets the uptime of this HyperflexSummary.

        :param uptime: The uptime of this HyperflexSummary.
        :type: str
        """

        self._uptime = uptime

    @property
    def used_capacity(self):
        """
        Gets the used_capacity of this HyperflexSummary.

        :return: The used_capacity of this HyperflexSummary.
        :rtype: int
        """
        return self._used_capacity

    @used_capacity.setter
    def used_capacity(self, used_capacity):
        """
        Sets the used_capacity of this HyperflexSummary.

        :param used_capacity: The used_capacity of this HyperflexSummary.
        :type: int
        """

        self._used_capacity = used_capacity

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
        if not isinstance(other, HyperflexSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
