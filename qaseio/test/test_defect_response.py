"""
    Qase.io API

    Qase API Specification.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@qase.io
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import qaseio
from qaseio.model.defect import Defect
from qaseio.model.defect_response_all_of import DefectResponseAllOf
from qaseio.model.response import Response
globals()['Defect'] = Defect
globals()['DefectResponseAllOf'] = DefectResponseAllOf
globals()['Response'] = Response
from qaseio.model.defect_response import DefectResponse


class TestDefectResponse(unittest.TestCase):
    """DefectResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDefectResponse(self):
        """Test DefectResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = DefectResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()