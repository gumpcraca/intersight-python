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


class IamSystem(object):
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
        'version_context': 'MoVersionContext',
        'end_point_privileges': 'list[IamEndPointPrivilegeRef]',
        'end_point_roles': 'list[IamEndPointRoleRef]',
        'idp': 'IamIdpRef',
        'privilege_sets': 'list[IamPrivilegeSetRef]',
        'privileges': 'list[IamPrivilegeRef]',
        'roles': 'list[IamRoleRef]',
        'service_provider': 'IamServiceProviderRef'
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
        'version_context': 'VersionContext',
        'end_point_privileges': 'EndPointPrivileges',
        'end_point_roles': 'EndPointRoles',
        'idp': 'Idp',
        'privilege_sets': 'PrivilegeSets',
        'privileges': 'Privileges',
        'roles': 'Roles',
        'service_provider': 'ServiceProvider'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, tags=None, version_context=None, end_point_privileges=None, end_point_roles=None, idp=None, privilege_sets=None, privileges=None, roles=None, service_provider=None):
        """
        IamSystem - a model defined in Swagger
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
        self._version_context = None
        self._end_point_privileges = None
        self._end_point_roles = None
        self._idp = None
        self._privilege_sets = None
        self._privileges = None
        self._roles = None
        self._service_provider = None

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
        if version_context is not None:
          self.version_context = version_context
        if end_point_privileges is not None:
          self.end_point_privileges = end_point_privileges
        if end_point_roles is not None:
          self.end_point_roles = end_point_roles
        if idp is not None:
          self.idp = idp
        if privilege_sets is not None:
          self.privilege_sets = privilege_sets
        if privileges is not None:
          self.privileges = privileges
        if roles is not None:
          self.roles = roles
        if service_provider is not None:
          self.service_provider = service_provider

    @property
    def account_moid(self):
        """
        Gets the account_moid of this IamSystem.
        The Account ID for this managed object.  

        :return: The account_moid of this IamSystem.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this IamSystem.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this IamSystem.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this IamSystem.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this IamSystem.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this IamSystem.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this IamSystem.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this IamSystem.
        The time when this managed object was created.  

        :return: The create_time of this IamSystem.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this IamSystem.
        The time when this managed object was created.  

        :param create_time: The create_time of this IamSystem.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def mod_time(self):
        """
        Gets the mod_time of this IamSystem.
        The time when this managed object was last modified.  

        :return: The mod_time of this IamSystem.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this IamSystem.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this IamSystem.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this IamSystem.
        A unique identifier of this Managed Object instance.  

        :return: The moid of this IamSystem.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this IamSystem.
        A unique identifier of this Managed Object instance.  

        :param moid: The moid of this IamSystem.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this IamSystem.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this IamSystem.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this IamSystem.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this IamSystem.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this IamSystem.
        An array of owners which represent effective ownership of this object.   

        :return: The owners of this IamSystem.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this IamSystem.
        An array of owners which represent effective ownership of this object.   

        :param owners: The owners of this IamSystem.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this IamSystem.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this IamSystem.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this IamSystem.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this IamSystem.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def tags(self):
        """
        Gets the tags of this IamSystem.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :return: The tags of this IamSystem.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this IamSystem.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :param tags: The tags of this IamSystem.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this IamSystem.
        The versioning info for this managed object   

        :return: The version_context of this IamSystem.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this IamSystem.
        The versioning info for this managed object   

        :param version_context: The version_context of this IamSystem.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def end_point_privileges(self):
        """
        Gets the end_point_privileges of this IamSystem.
        Privileges defined in end point devices such as UCSFI, IMC, HX managed by Intersight. These privileges are assigned to Intersight users using end point roles to perform operations such as GUI/CLI cross launch. 

        :return: The end_point_privileges of this IamSystem.
        :rtype: list[IamEndPointPrivilegeRef]
        """
        return self._end_point_privileges

    @end_point_privileges.setter
    def end_point_privileges(self, end_point_privileges):
        """
        Sets the end_point_privileges of this IamSystem.
        Privileges defined in end point devices such as UCSFI, IMC, HX managed by Intersight. These privileges are assigned to Intersight users using end point roles to perform operations such as GUI/CLI cross launch. 

        :param end_point_privileges: The end_point_privileges of this IamSystem.
        :type: list[IamEndPointPrivilegeRef]
        """

        self._end_point_privileges = end_point_privileges

    @property
    def end_point_roles(self):
        """
        Gets the end_point_roles of this IamSystem.
        Roles defined in end point devices such as UCSFI, IMC, HX managed by Intersight. These roles are assigned to Intersight users to perform end point operations such as GUI/CLI cross launch. 

        :return: The end_point_roles of this IamSystem.
        :rtype: list[IamEndPointRoleRef]
        """
        return self._end_point_roles

    @end_point_roles.setter
    def end_point_roles(self, end_point_roles):
        """
        Sets the end_point_roles of this IamSystem.
        Roles defined in end point devices such as UCSFI, IMC, HX managed by Intersight. These roles are assigned to Intersight users to perform end point operations such as GUI/CLI cross launch. 

        :param end_point_roles: The end_point_roles of this IamSystem.
        :type: list[IamEndPointRoleRef]
        """

        self._end_point_roles = end_point_roles

    @property
    def idp(self):
        """
        Gets the idp of this IamSystem.
        Default Cisco IdP used for SAML authentication. 

        :return: The idp of this IamSystem.
        :rtype: IamIdpRef
        """
        return self._idp

    @idp.setter
    def idp(self, idp):
        """
        Sets the idp of this IamSystem.
        Default Cisco IdP used for SAML authentication. 

        :param idp: The idp of this IamSystem.
        :type: IamIdpRef
        """

        self._idp = idp

    @property
    def privilege_sets(self):
        """
        Gets the privilege_sets of this IamSystem.
        Privilege set is a collection of privileges. Privilege sets are assigned to a user using roles. 

        :return: The privilege_sets of this IamSystem.
        :rtype: list[IamPrivilegeSetRef]
        """
        return self._privilege_sets

    @privilege_sets.setter
    def privilege_sets(self, privilege_sets):
        """
        Sets the privilege_sets of this IamSystem.
        Privilege set is a collection of privileges. Privilege sets are assigned to a user using roles. 

        :param privilege_sets: The privilege_sets of this IamSystem.
        :type: list[IamPrivilegeSetRef]
        """

        self._privilege_sets = privilege_sets

    @property
    def privileges(self):
        """
        Gets the privileges of this IamSystem.
        Privilege represents an action which can be performed in Intersight such as creating server profile, deleting a user etc. Privileges are assigned to a user using privilege sets and roles. 

        :return: The privileges of this IamSystem.
        :rtype: list[IamPrivilegeRef]
        """
        return self._privileges

    @privileges.setter
    def privileges(self, privileges):
        """
        Sets the privileges of this IamSystem.
        Privilege represents an action which can be performed in Intersight such as creating server profile, deleting a user etc. Privileges are assigned to a user using privilege sets and roles. 

        :param privileges: The privileges of this IamSystem.
        :type: list[IamPrivilegeRef]
        """

        self._privileges = privileges

    @property
    def roles(self):
        """
        Gets the roles of this IamSystem.
        Default roles such as Account Administrator and Read-Only roles. A role is a collection of privilege sets that are assigned to a user using a permission object. 

        :return: The roles of this IamSystem.
        :rtype: list[IamRoleRef]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """
        Sets the roles of this IamSystem.
        Default roles such as Account Administrator and Read-Only roles. A role is a collection of privilege sets that are assigned to a user using a permission object. 

        :param roles: The roles of this IamSystem.
        :type: list[IamRoleRef]
        """

        self._roles = roles

    @property
    def service_provider(self):
        """
        Gets the service_provider of this IamSystem.
        SAML service provider which holds the Intersight Service Provider's SAML entity ID and metadata to integrate with the IdPs. 

        :return: The service_provider of this IamSystem.
        :rtype: IamServiceProviderRef
        """
        return self._service_provider

    @service_provider.setter
    def service_provider(self, service_provider):
        """
        Sets the service_provider of this IamSystem.
        SAML service provider which holds the Intersight Service Provider's SAML entity ID and metadata to integrate with the IdPs. 

        :param service_provider: The service_provider of this IamSystem.
        :type: IamServiceProviderRef
        """

        self._service_provider = service_provider

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
        if not isinstance(other, IamSystem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
