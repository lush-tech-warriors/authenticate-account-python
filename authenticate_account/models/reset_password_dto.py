# coding: utf-8

"""
    Authenticate Platform Account API

    Through this API you can authenticate user credentials and thereby gain access to the available suite of APIs  # noqa: E501

    OpenAPI spec version: 1.0
    Contact: platform-support@authenticateis.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ResetPasswordDto(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'email': 'str',
        'reset_identifier': 'str',
        'password': 'str',
        'confirm_password': 'str'
    }

    attribute_map = {
        'email': 'email',
        'reset_identifier': 'resetIdentifier',
        'password': 'password',
        'confirm_password': 'confirmPassword'
    }

    def __init__(self, email=None, reset_identifier=None, password=None, confirm_password=None):  # noqa: E501
        """ResetPasswordDto - a model defined in Swagger"""  # noqa: E501
        self._email = None
        self._reset_identifier = None
        self._password = None
        self._confirm_password = None
        self.discriminator = None
        self.email = email
        self.reset_identifier = reset_identifier
        self.password = password
        self.confirm_password = confirm_password

    @property
    def email(self):
        """Gets the email of this ResetPasswordDto.  # noqa: E501

        The email that belongs to the account  # noqa: E501

        :return: The email of this ResetPasswordDto.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ResetPasswordDto.

        The email that belongs to the account  # noqa: E501

        :param email: The email of this ResetPasswordDto.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def reset_identifier(self):
        """Gets the reset_identifier of this ResetPasswordDto.  # noqa: E501

        The unique identifier to reset your password received in email  # noqa: E501

        :return: The reset_identifier of this ResetPasswordDto.  # noqa: E501
        :rtype: str
        """
        return self._reset_identifier

    @reset_identifier.setter
    def reset_identifier(self, reset_identifier):
        """Sets the reset_identifier of this ResetPasswordDto.

        The unique identifier to reset your password received in email  # noqa: E501

        :param reset_identifier: The reset_identifier of this ResetPasswordDto.  # noqa: E501
        :type: str
        """
        if reset_identifier is None:
            raise ValueError("Invalid value for `reset_identifier`, must not be `None`")  # noqa: E501

        self._reset_identifier = reset_identifier

    @property
    def password(self):
        """Gets the password of this ResetPasswordDto.  # noqa: E501

        Password  # noqa: E501

        :return: The password of this ResetPasswordDto.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this ResetPasswordDto.

        Password  # noqa: E501

        :param password: The password of this ResetPasswordDto.  # noqa: E501
        :type: str
        """
        if password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501

        self._password = password

    @property
    def confirm_password(self):
        """Gets the confirm_password of this ResetPasswordDto.  # noqa: E501

        Confirm password  # noqa: E501

        :return: The confirm_password of this ResetPasswordDto.  # noqa: E501
        :rtype: str
        """
        return self._confirm_password

    @confirm_password.setter
    def confirm_password(self, confirm_password):
        """Sets the confirm_password of this ResetPasswordDto.

        Confirm password  # noqa: E501

        :param confirm_password: The confirm_password of this ResetPasswordDto.  # noqa: E501
        :type: str
        """
        if confirm_password is None:
            raise ValueError("Invalid value for `confirm_password`, must not be `None`")  # noqa: E501

        self._confirm_password = confirm_password

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(ResetPasswordDto, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ResetPasswordDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
