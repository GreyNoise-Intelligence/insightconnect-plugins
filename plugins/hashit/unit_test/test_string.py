import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Dict
from unittest import TestCase

from icon_hashit.actions.string import String
from icon_hashit.actions.string.schema import Input, Output
from jsonschema import validate
from parameterized import parameterized


class TestString(TestCase):
    def setUp(self) -> None:
        self.action = String()
        self.maxDiff = None

    @parameterized.expand(
        [
            (
                "hello world",
                {
                    Output.MD5: "5eb63bbbe01eeed093cb22bb8f5acdc3",
                    Output.SHA1: "2aae6c35c94fcfb415dbe95f408b9ce91ee846ed",
                    Output.SHA256: "b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9",
                    Output.SHA512: "309ecc489c12d6eb4cc40f50c902f2b4d0ed77ee511a7c7a9bcd3ca86d4cd86f989dd35bc5ff499670da34255b45b0cfd830e81f605dcf7dc5542e93ae9cd76f",
                },
            )
        ]
    )
    def test_string(self, input_string: str, expected: Dict[str, str]) -> None:
        response = self.action.run({Input.STRING: input_string})
        validate(response, self.action.output.schema)
        self.assertEqual(response, expected)