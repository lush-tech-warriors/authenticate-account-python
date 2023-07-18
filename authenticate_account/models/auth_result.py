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

class AuthResult(object):
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
        'token': 'str',
        'refresh_token': 'str',
        'expires_in': 'float',
        'expires_in': 'float',
        'id': 'str',
        'name': 'str',
        'date_logged_in': 'datetime',
        'date_logged_in': 'datetime'
    }

    attribute_map = {
        'token': 'token',
        'refresh_token': 'refreshToken',
        'expires_in': 'expiresIn',
        'expires_in': 'expires_in',
        'id': 'id',
        'name': 'name',
        'date_logged_in': 'dateLoggedIn',
        'date_logged_in': 'date_logged_in'
    }

    def __init__(self, token=None, refresh_token=None, expires_in=None, expires_in=None, id=None, name=None, date_logged_in=None, date_logged_in=None):  # noqa: E501
        """AuthResult - a model defined in Swagger"""  # noqa: E501
        self._token = None
        self._refresh_token = None
        self._expires_in = None
        self._expires_in = None
        self._id = None
        self._name = None
        self._date_logged_in = None
        self._date_logged_in = None
        self.discriminator = None
        if token is not None:
            self.token = token
        if refresh_token is not None:
            self.refresh_token = refresh_token
        if expires_in is not None:
            self.expires_in = expires_in
        if expires_in is not None:
            self.expires_in = expires_in
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if date_logged_in is not None:
            self.date_logged_in = date_logged_in
        if date_logged_in is not None:
            self.date_logged_in = date_logged_in

    @property
    def token(self):
        """Gets the token of this AuthResult.  # noqa: E501


        :return: The token of this AuthResult.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this AuthResult.


        :param token: The token of this AuthResult.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def refresh_token(self):
        """Gets the refresh_token of this AuthResult.  # noqa: E501


        :return: The refresh_token of this AuthResult.  # noqa: E501
        :rtype: str
        """
        return self._refresh_token

    @refresh_token.setter
    def refresh_token(self, refresh_token):
        """Sets the refresh_token of this AuthResult.


        :param refresh_token: The refresh_token of this AuthResult.  # noqa: E501
        :type: str
        """

        self._refresh_token = refresh_token

    @property
    def expires_in(self):
        """Gets the expires_in of this AuthResult.  # noqa: E501


        :return: The expires_in of this AuthResult.  # noqa: E501
        :rtype: float
        """
        return self._expires_in

    @expires_in.setter
    def expires_in(self, expires_in):
        """Sets the expires_in of this AuthResult.


        :param expires_in: The expires_in of this AuthResult.  # noqa: E501
        :type: float
        """

        self._expires_in = expires_in

    @property
    def expires_in(self):
        """Gets the expires_in of this AuthResult.  # noqa: E501


        :return: The expires_in of this AuthResult.  # noqa: E501
        :rtype: float
        """
        return self._expires_in

    @expires_in.setter
    def expires_in(self, expires_in):
        """Sets the expires_in of this AuthResult.


        :param expires_in: The expires_in of this AuthResult.  # noqa: E501
        :type: float
        """

        self._expires_in = expires_in

    @property
    def id(self):
        """Gets the id of this AuthResult.  # noqa: E501


        :return: The id of this AuthResult.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AuthResult.


        :param id: The id of this AuthResult.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this AuthResult.  # noqa: E501


        :return: The name of this AuthResult.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AuthResult.


        :param name: The name of this AuthResult.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def date_logged_in(self):
        """Gets the date_logged_in of this AuthResult.  # noqa: E501


        :return: The date_logged_in of this AuthResult.  # noqa: E501
        :rtype: datetime
        """
        return self._date_logged_in

    @date_logged_in.setter
    def date_logged_in(self, date_logged_in):
        """Sets the date_logged_in of this AuthResult.


        :param date_logged_in: The date_logged_in of this AuthResult.  # noqa: E501
        :type: datetime
        """

        self._date_logged_in = date_logged_in

    @property
    def date_logged_in(self):
        """Gets the date_logged_in of this AuthResult.  # noqa: E501


        :return: The date_logged_in of this AuthResult.  # noqa: E501
        :rtype: datetime
        """
        return self._date_logged_in

    @date_logged_in.setter
    def date_logged_in(self, date_logged_in):
        """Sets the date_logged_in of this AuthResult.


        :param date_logged_in: The date_logged_in of this AuthResult.  # noqa: E501
        :type: datetime
        """

        self._date_logged_in = date_logged_in

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
        if issubclass(AuthResult, dict):
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
        if not isinstance(other, AuthResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
