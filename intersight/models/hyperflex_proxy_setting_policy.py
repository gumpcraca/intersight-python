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


class HyperflexProxySettingPolicy(object):
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
        'account_moid': 'str',
        'ancestors': 'list[MoBaseMoRef]',
        'create_time': 'datetime',
        'mod_time': 'datetime',
        'moid': 'str',
        'object_type': 'str',
        'owners': 'list[str]',
        'parent': 'MoBaseMoRef',
        'tags': 'list[MoTag]',
        'description': 'str',
        'name': 'str',
        'cluster_profiles': 'list[HyperflexClusterProfileRef]',
        'hostname': 'str',
        'is_password_set': 'bool',
        'organization': 'IamAccountRef',
        'password': 'str',
        'port': 'int',
        'username': 'str'
    }

    attribute_map = {
        'account_moid': 'AccountMoid',
        'ancestors': 'Ancestors',
        'create_time': 'CreateTime',
        'mod_time': 'ModTime',
        'moid': 'Moid',
        'object_type': 'ObjectType',
        'owners': 'Owners',
        'parent': 'Parent',
        'tags': 'Tags',
        'description': 'Description',
        'name': 'Name',
        'cluster_profiles': 'ClusterProfiles',
        'hostname': 'Hostname',
        'is_password_set': 'IsPasswordSet',
        'organization': 'Organization',
        'password': 'Password',
        'port': 'Port',
        'username': 'Username'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, tags=None, description=None, name=None, cluster_profiles=None, hostname=None, is_password_set=None, organization=None, password=None, port=None, username=None):
        """
        HyperflexProxySettingPolicy - a model defined in Swagger
        """

        self._account_moid = None
        self._ancestors = None
        self._create_time = None
        self._mod_time = None
        self._moid = None
        self._object_type = None
        self._owners = None
        self._parent = None
        self._tags = None
        self._description = None
        self._name = None
        self._cluster_profiles = None
        self._hostname = None
        self._is_password_set = None
        self._organization = None
        self._password = None
        self._port = None
        self._username = None

        if account_moid is not None:
          self.account_moid = account_moid
        if ancestors is not None:
          self.ancestors = ancestors
        if create_time is not None:
          self.create_time = create_time
        if mod_time is not None:
          self.mod_time = mod_time
        if moid is not None:
          self.moid = moid
        if object_type is not None:
          self.object_type = object_type
        if owners is not None:
          self.owners = owners
        if parent is not None:
          self.parent = parent
        if tags is not None:
          self.tags = tags
        if description is not None:
          self.description = description
        if name is not None:
          self.name = name
        if cluster_profiles is not None:
          self.cluster_profiles = cluster_profiles
        if hostname is not None:
          self.hostname = hostname
        if is_password_set is not None:
          self.is_password_set = is_password_set
        if organization is not None:
          self.organization = organization
        if password is not None:
          self.password = password
        if port is not None:
          self.port = port
        if username is not None:
          self.username = username

    @property
    def account_moid(self):
        """
        Gets the account_moid of this HyperflexProxySettingPolicy.
        The Account ID for this managed object.  

        :return: The account_moid of this HyperflexProxySettingPolicy.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this HyperflexProxySettingPolicy.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this HyperflexProxySettingPolicy.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this HyperflexProxySettingPolicy.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this HyperflexProxySettingPolicy.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this HyperflexProxySettingPolicy.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this HyperflexProxySettingPolicy.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this HyperflexProxySettingPolicy.
        The time when this managed object was created.  

        :return: The create_time of this HyperflexProxySettingPolicy.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this HyperflexProxySettingPolicy.
        The time when this managed object was created.  

        :param create_time: The create_time of this HyperflexProxySettingPolicy.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def mod_time(self):
        """
        Gets the mod_time of this HyperflexProxySettingPolicy.
        The time when this managed object was last modified.  

        :return: The mod_time of this HyperflexProxySettingPolicy.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this HyperflexProxySettingPolicy.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this HyperflexProxySettingPolicy.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this HyperflexProxySettingPolicy.
        A unique identifier of this Managed Object instance.  

        :return: The moid of this HyperflexProxySettingPolicy.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this HyperflexProxySettingPolicy.
        A unique identifier of this Managed Object instance.  

        :param moid: The moid of this HyperflexProxySettingPolicy.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this HyperflexProxySettingPolicy.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this HyperflexProxySettingPolicy.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this HyperflexProxySettingPolicy.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this HyperflexProxySettingPolicy.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this HyperflexProxySettingPolicy.
        An array of owners which represent effective ownership of this object.   

        :return: The owners of this HyperflexProxySettingPolicy.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this HyperflexProxySettingPolicy.
        An array of owners which represent effective ownership of this object.   

        :param owners: The owners of this HyperflexProxySettingPolicy.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this HyperflexProxySettingPolicy.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this HyperflexProxySettingPolicy.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this HyperflexProxySettingPolicy.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this HyperflexProxySettingPolicy.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def tags(self):
        """
        Gets the tags of this HyperflexProxySettingPolicy.
        An array of tags, which allow to add key, value meta-data to managed objects.   

        :return: The tags of this HyperflexProxySettingPolicy.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this HyperflexProxySettingPolicy.
        An array of tags, which allow to add key, value meta-data to managed objects.   

        :param tags: The tags of this HyperflexProxySettingPolicy.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def description(self):
        """
        Gets the description of this HyperflexProxySettingPolicy.
        Description of the policy.  

        :return: The description of this HyperflexProxySettingPolicy.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this HyperflexProxySettingPolicy.
        Description of the policy.  

        :param description: The description of this HyperflexProxySettingPolicy.
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """
        Gets the name of this HyperflexProxySettingPolicy.
        Name of the policy.   

        :return: The name of this HyperflexProxySettingPolicy.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this HyperflexProxySettingPolicy.
        Name of the policy.   

        :param name: The name of this HyperflexProxySettingPolicy.
        :type: str
        """

        self._name = name

    @property
    def cluster_profiles(self):
        """
        Gets the cluster_profiles of this HyperflexProxySettingPolicy.
        List of cluster profiles using this policy 

        :return: The cluster_profiles of this HyperflexProxySettingPolicy.
        :rtype: list[HyperflexClusterProfileRef]
        """
        return self._cluster_profiles

    @cluster_profiles.setter
    def cluster_profiles(self, cluster_profiles):
        """
        Sets the cluster_profiles of this HyperflexProxySettingPolicy.
        List of cluster profiles using this policy 

        :param cluster_profiles: The cluster_profiles of this HyperflexProxySettingPolicy.
        :type: list[HyperflexClusterProfileRef]
        """

        self._cluster_profiles = cluster_profiles

    @property
    def hostname(self):
        """
        Gets the hostname of this HyperflexProxySettingPolicy.
        HTTP Proxy server FQDN or IP  

        :return: The hostname of this HyperflexProxySettingPolicy.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """
        Sets the hostname of this HyperflexProxySettingPolicy.
        HTTP Proxy server FQDN or IP  

        :param hostname: The hostname of this HyperflexProxySettingPolicy.
        :type: str
        """

        self._hostname = hostname

    @property
    def is_password_set(self):
        """
        Gets the is_password_set of this HyperflexProxySettingPolicy.

        :return: The is_password_set of this HyperflexProxySettingPolicy.
        :rtype: bool
        """
        return self._is_password_set

    @is_password_set.setter
    def is_password_set(self, is_password_set):
        """
        Sets the is_password_set of this HyperflexProxySettingPolicy.

        :param is_password_set: The is_password_set of this HyperflexProxySettingPolicy.
        :type: bool
        """

        self._is_password_set = is_password_set

    @property
    def organization(self):
        """
        Gets the organization of this HyperflexProxySettingPolicy.
        Organization 

        :return: The organization of this HyperflexProxySettingPolicy.
        :rtype: IamAccountRef
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """
        Sets the organization of this HyperflexProxySettingPolicy.
        Organization 

        :param organization: The organization of this HyperflexProxySettingPolicy.
        :type: IamAccountRef
        """

        self._organization = organization

    @property
    def password(self):
        """
        Gets the password of this HyperflexProxySettingPolicy.
        HTTP Proxy password. It must contain at least 6 characters.  

        :return: The password of this HyperflexProxySettingPolicy.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this HyperflexProxySettingPolicy.
        HTTP Proxy password. It must contain at least 6 characters.  

        :param password: The password of this HyperflexProxySettingPolicy.
        :type: str
        """

        self._password = password

    @property
    def port(self):
        """
        Gets the port of this HyperflexProxySettingPolicy.
        HTTP Proxy port number  

        :return: The port of this HyperflexProxySettingPolicy.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this HyperflexProxySettingPolicy.
        HTTP Proxy port number  

        :param port: The port of this HyperflexProxySettingPolicy.
        :type: int
        """

        self._port = port

    @property
    def username(self):
        """
        Gets the username of this HyperflexProxySettingPolicy.
        HTTP Proxy username   

        :return: The username of this HyperflexProxySettingPolicy.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this HyperflexProxySettingPolicy.
        HTTP Proxy username   

        :param username: The username of this HyperflexProxySettingPolicy.
        :type: str
        """

        self._username = username

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
        if not isinstance(other, HyperflexProxySettingPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
