# coding: utf-8

"""
    Authenticate Platform Account API

    Through this API you can authenticate user credentials and thereby gain access to the available suite of APIs  # noqa: E501

    OpenAPI spec version: 1.0
    Contact: platform-support@authenticateis.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import authenticate_account
from authenticate_account.models.renewal_dto import RenewalDto  # noqa: E501
from authenticate_account.rest import ApiException


class TestRenewalDto(unittest.TestCase):
    """RenewalDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testRenewalDto(self):
        """Test RenewalDto"""
        # FIXME: construct object with mandatory attributes with example values
        # model = authenticate_account.models.renewal_dto.RenewalDto()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
