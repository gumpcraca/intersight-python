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


class CondHclStatus(object):
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
        'details': 'list[CondHclStatusDetailRef]',
        'hcl_firmware_version': 'str',
        'hcl_model': 'str',
        'hcl_os_vendor': 'str',
        'hcl_os_version': 'str',
        'hcl_processor': 'str',
        'inv_firmware_version': 'str',
        'inv_model': 'str',
        'inv_os_vendor': 'str',
        'inv_os_version': 'str',
        'inv_processor': 'str',
        'managed_object': 'InventoryBaseRef',
        'reason': 'str',
        'registered_device': 'AssetDeviceRegistrationRef',
        'status': 'str'
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
        'details': 'Details',
        'hcl_firmware_version': 'HclFirmwareVersion',
        'hcl_model': 'HclModel',
        'hcl_os_vendor': 'HclOsVendor',
        'hcl_os_version': 'HclOsVersion',
        'hcl_processor': 'HclProcessor',
        'inv_firmware_version': 'InvFirmwareVersion',
        'inv_model': 'InvModel',
        'inv_os_vendor': 'InvOsVendor',
        'inv_os_version': 'InvOsVersion',
        'inv_processor': 'InvProcessor',
        'managed_object': 'ManagedObject',
        'reason': 'Reason',
        'registered_device': 'RegisteredDevice',
        'status': 'Status'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, tags=None, details=None, hcl_firmware_version=None, hcl_model=None, hcl_os_vendor=None, hcl_os_version=None, hcl_processor=None, inv_firmware_version=None, inv_model=None, inv_os_vendor=None, inv_os_version=None, inv_processor=None, managed_object=None, reason='Missing-Os-Info', registered_device=None, status='Incomplete'):
        """
        CondHclStatus - a model defined in Swagger
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
        self._details = None
        self._hcl_firmware_version = None
        self._hcl_model = None
        self._hcl_os_vendor = None
        self._hcl_os_version = None
        self._hcl_processor = None
        self._inv_firmware_version = None
        self._inv_model = None
        self._inv_os_vendor = None
        self._inv_os_version = None
        self._inv_processor = None
        self._managed_object = None
        self._reason = None
        self._registered_device = None
        self._status = None

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
        if details is not None:
          self.details = details
        if hcl_firmware_version is not None:
          self.hcl_firmware_version = hcl_firmware_version
        if hcl_model is not None:
          self.hcl_model = hcl_model
        if hcl_os_vendor is not None:
          self.hcl_os_vendor = hcl_os_vendor
        if hcl_os_version is not None:
          self.hcl_os_version = hcl_os_version
        if hcl_processor is not None:
          self.hcl_processor = hcl_processor
        if inv_firmware_version is not None:
          self.inv_firmware_version = inv_firmware_version
        if inv_model is not None:
          self.inv_model = inv_model
        if inv_os_vendor is not None:
          self.inv_os_vendor = inv_os_vendor
        if inv_os_version is not None:
          self.inv_os_version = inv_os_version
        if inv_processor is not None:
          self.inv_processor = inv_processor
        if managed_object is not None:
          self.managed_object = managed_object
        if reason is not None:
          self.reason = reason
        if registered_device is not None:
          self.registered_device = registered_device
        if status is not None:
          self.status = status

    @property
    def account_moid(self):
        """
        Gets the account_moid of this CondHclStatus.
        The Account ID for this managed object.  

        :return: The account_moid of this CondHclStatus.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this CondHclStatus.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this CondHclStatus.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this CondHclStatus.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this CondHclStatus.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this CondHclStatus.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this CondHclStatus.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this CondHclStatus.
        The time when this managed object was created.  

        :return: The create_time of this CondHclStatus.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this CondHclStatus.
        The time when this managed object was created.  

        :param create_time: The create_time of this CondHclStatus.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def mod_time(self):
        """
        Gets the mod_time of this CondHclStatus.
        The time when this managed object was last modified.  

        :return: The mod_time of this CondHclStatus.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this CondHclStatus.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this CondHclStatus.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this CondHclStatus.
        A unique identifier of this Managed Object instance.  

        :return: The moid of this CondHclStatus.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this CondHclStatus.
        A unique identifier of this Managed Object instance.  

        :param moid: The moid of this CondHclStatus.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this CondHclStatus.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this CondHclStatus.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this CondHclStatus.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this CondHclStatus.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this CondHclStatus.
        An array of owners which represent effective ownership of this object.   

        :return: The owners of this CondHclStatus.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this CondHclStatus.
        An array of owners which represent effective ownership of this object.   

        :param owners: The owners of this CondHclStatus.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this CondHclStatus.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this CondHclStatus.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this CondHclStatus.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this CondHclStatus.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def tags(self):
        """
        Gets the tags of this CondHclStatus.
        An array of tags, which allow to add key, value meta-data to managed objects.   

        :return: The tags of this CondHclStatus.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this CondHclStatus.
        An array of tags, which allow to add key, value meta-data to managed objects.   

        :param tags: The tags of this CondHclStatus.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def details(self):
        """
        Gets the details of this CondHclStatus.
        a collection of all the HclStatusDetails 

        :return: The details of this CondHclStatus.
        :rtype: list[CondHclStatusDetailRef]
        """
        return self._details

    @details.setter
    def details(self, details):
        """
        Sets the details of this CondHclStatus.
        a collection of all the HclStatusDetails 

        :param details: The details of this CondHclStatus.
        :type: list[CondHclStatusDetailRef]
        """

        self._details = details

    @property
    def hcl_firmware_version(self):
        """
        Gets the hcl_firmware_version of this CondHclStatus.
        the current CIMC version for the server normalized for querying HCL data  

        :return: The hcl_firmware_version of this CondHclStatus.
        :rtype: str
        """
        return self._hcl_firmware_version

    @hcl_firmware_version.setter
    def hcl_firmware_version(self, hcl_firmware_version):
        """
        Sets the hcl_firmware_version of this CondHclStatus.
        the current CIMC version for the server normalized for querying HCL data  

        :param hcl_firmware_version: The hcl_firmware_version of this CondHclStatus.
        :type: str
        """

        self._hcl_firmware_version = hcl_firmware_version

    @property
    def hcl_model(self):
        """
        Gets the hcl_model of this CondHclStatus.
        the managed object's model to validate normalized for querying HCL data  

        :return: The hcl_model of this CondHclStatus.
        :rtype: str
        """
        return self._hcl_model

    @hcl_model.setter
    def hcl_model(self, hcl_model):
        """
        Sets the hcl_model of this CondHclStatus.
        the managed object's model to validate normalized for querying HCL data  

        :param hcl_model: The hcl_model of this CondHclStatus.
        :type: str
        """

        self._hcl_model = hcl_model

    @property
    def hcl_os_vendor(self):
        """
        Gets the hcl_os_vendor of this CondHclStatus.
        the OS Vendor for the managed object to validate normalized for querying HCL data. Empty if we are missing this information  

        :return: The hcl_os_vendor of this CondHclStatus.
        :rtype: str
        """
        return self._hcl_os_vendor

    @hcl_os_vendor.setter
    def hcl_os_vendor(self, hcl_os_vendor):
        """
        Sets the hcl_os_vendor of this CondHclStatus.
        the OS Vendor for the managed object to validate normalized for querying HCL data. Empty if we are missing this information  

        :param hcl_os_vendor: The hcl_os_vendor of this CondHclStatus.
        :type: str
        """

        self._hcl_os_vendor = hcl_os_vendor

    @property
    def hcl_os_version(self):
        """
        Gets the hcl_os_version of this CondHclStatus.
        the OS Version for the managed object to validate normalized for querying HCL data. Empty if we are missing this information  

        :return: The hcl_os_version of this CondHclStatus.
        :rtype: str
        """
        return self._hcl_os_version

    @hcl_os_version.setter
    def hcl_os_version(self, hcl_os_version):
        """
        Sets the hcl_os_version of this CondHclStatus.
        the OS Version for the managed object to validate normalized for querying HCL data. Empty if we are missing this information  

        :param hcl_os_version: The hcl_os_version of this CondHclStatus.
        :type: str
        """

        self._hcl_os_version = hcl_os_version

    @property
    def hcl_processor(self):
        """
        Gets the hcl_processor of this CondHclStatus.
        the managed object's processor to validate if applicable normalized for querying HCL data. It is left empty if processor is not required for the HCL validation, for example if we are evaluating some other managedObject that is not a server. Currently only server validation is supported.  

        :return: The hcl_processor of this CondHclStatus.
        :rtype: str
        """
        return self._hcl_processor

    @hcl_processor.setter
    def hcl_processor(self, hcl_processor):
        """
        Sets the hcl_processor of this CondHclStatus.
        the managed object's processor to validate if applicable normalized for querying HCL data. It is left empty if processor is not required for the HCL validation, for example if we are evaluating some other managedObject that is not a server. Currently only server validation is supported.  

        :param hcl_processor: The hcl_processor of this CondHclStatus.
        :type: str
        """

        self._hcl_processor = hcl_processor

    @property
    def inv_firmware_version(self):
        """
        Gets the inv_firmware_version of this CondHclStatus.
        the current CIMC version for the server as received from inventory  

        :return: The inv_firmware_version of this CondHclStatus.
        :rtype: str
        """
        return self._inv_firmware_version

    @inv_firmware_version.setter
    def inv_firmware_version(self, inv_firmware_version):
        """
        Sets the inv_firmware_version of this CondHclStatus.
        the current CIMC version for the server as received from inventory  

        :param inv_firmware_version: The inv_firmware_version of this CondHclStatus.
        :type: str
        """

        self._inv_firmware_version = inv_firmware_version

    @property
    def inv_model(self):
        """
        Gets the inv_model of this CondHclStatus.
        the managed object's model to validate as received from the inventory.  

        :return: The inv_model of this CondHclStatus.
        :rtype: str
        """
        return self._inv_model

    @inv_model.setter
    def inv_model(self, inv_model):
        """
        Sets the inv_model of this CondHclStatus.
        the managed object's model to validate as received from the inventory.  

        :param inv_model: The inv_model of this CondHclStatus.
        :type: str
        """

        self._inv_model = inv_model

    @property
    def inv_os_vendor(self):
        """
        Gets the inv_os_vendor of this CondHclStatus.
        the OS Vendor for the managed object to validate as received from inventory. Empty if we are missing this information  

        :return: The inv_os_vendor of this CondHclStatus.
        :rtype: str
        """
        return self._inv_os_vendor

    @inv_os_vendor.setter
    def inv_os_vendor(self, inv_os_vendor):
        """
        Sets the inv_os_vendor of this CondHclStatus.
        the OS Vendor for the managed object to validate as received from inventory. Empty if we are missing this information  

        :param inv_os_vendor: The inv_os_vendor of this CondHclStatus.
        :type: str
        """

        self._inv_os_vendor = inv_os_vendor

    @property
    def inv_os_version(self):
        """
        Gets the inv_os_version of this CondHclStatus.
        the OS Version for the managed object to validate as received from inventory. Empty if we are missing this information  

        :return: The inv_os_version of this CondHclStatus.
        :rtype: str
        """
        return self._inv_os_version

    @inv_os_version.setter
    def inv_os_version(self, inv_os_version):
        """
        Sets the inv_os_version of this CondHclStatus.
        the OS Version for the managed object to validate as received from inventory. Empty if we are missing this information  

        :param inv_os_version: The inv_os_version of this CondHclStatus.
        :type: str
        """

        self._inv_os_version = inv_os_version

    @property
    def inv_processor(self):
        """
        Gets the inv_processor of this CondHclStatus.
        the managed object's processor to validate if applicable as received from inventory. It is left empty if processor is not required for the HCL validation, for example if we are evaluating some other managedObject that is not a server. Currently only server validation is supported.  

        :return: The inv_processor of this CondHclStatus.
        :rtype: str
        """
        return self._inv_processor

    @inv_processor.setter
    def inv_processor(self, inv_processor):
        """
        Sets the inv_processor of this CondHclStatus.
        the managed object's processor to validate if applicable as received from inventory. It is left empty if processor is not required for the HCL validation, for example if we are evaluating some other managedObject that is not a server. Currently only server validation is supported.  

        :param inv_processor: The inv_processor of this CondHclStatus.
        :type: str
        """

        self._inv_processor = inv_processor

    @property
    def managed_object(self):
        """
        Gets the managed_object of this CondHclStatus.
        specifies the managed object for which this HCLStatus applies 

        :return: The managed_object of this CondHclStatus.
        :rtype: InventoryBaseRef
        """
        return self._managed_object

    @managed_object.setter
    def managed_object(self, managed_object):
        """
        Sets the managed_object of this CondHclStatus.
        specifies the managed object for which this HCLStatus applies 

        :param managed_object: The managed_object of this CondHclStatus.
        :type: InventoryBaseRef
        """

        self._managed_object = managed_object

    @property
    def reason(self):
        """
        Gets the reason of this CondHclStatus.
        the reason for the HCL status. It will be one of the following \"Missing-Os-Info\" - we are missing os information in the inventory from the device connector \"Incompatible-Components\" - we have 1 or more components with \"Not-Validated\" status \"Compatible\" - all the components have \"Validated\" status  

        :return: The reason of this CondHclStatus.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """
        Sets the reason of this CondHclStatus.
        the reason for the HCL status. It will be one of the following \"Missing-Os-Info\" - we are missing os information in the inventory from the device connector \"Incompatible-Components\" - we have 1 or more components with \"Not-Validated\" status \"Compatible\" - all the components have \"Validated\" status  

        :param reason: The reason of this CondHclStatus.
        :type: str
        """
        allowed_values = ["Missing-Os-Info", "Incompatible-Components", "Compatible"]
        if reason not in allowed_values:
            raise ValueError(
                "Invalid value for `reason` ({0}), must be one of {1}"
                .format(reason, allowed_values)
            )

        self._reason = reason

    @property
    def registered_device(self):
        """
        Gets the registered_device of this CondHclStatus.
        Relationship to the registered device. We need this in order to correctly set permissions during device claim 

        :return: The registered_device of this CondHclStatus.
        :rtype: AssetDeviceRegistrationRef
        """
        return self._registered_device

    @registered_device.setter
    def registered_device(self, registered_device):
        """
        Sets the registered_device of this CondHclStatus.
        Relationship to the registered device. We need this in order to correctly set permissions during device claim 

        :param registered_device: The registered_device of this CondHclStatus.
        :type: AssetDeviceRegistrationRef
        """

        self._registered_device = registered_device

    @property
    def status(self):
        """
        Gets the status of this CondHclStatus.
        the status of the managed objects compatibility against HCL. The status can be one of the following \"Unknown\" - we do not have enough information to evaluate against the HCL data \"Validated\" - we have validated all components against the HCL and they all have \"Validated\" status \"Not-Validated\" - we have validated all components against the HCL and 1 or more has \"Not-Validated\" status   

        :return: The status of this CondHclStatus.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this CondHclStatus.
        the status of the managed objects compatibility against HCL. The status can be one of the following \"Unknown\" - we do not have enough information to evaluate against the HCL data \"Validated\" - we have validated all components against the HCL and they all have \"Validated\" status \"Not-Validated\" - we have validated all components against the HCL and 1 or more has \"Not-Validated\" status   

        :param status: The status of this CondHclStatus.
        :type: str
        """
        allowed_values = ["Incomplete", "Not-Found", "Validated"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

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
        if not isinstance(other, CondHclStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
