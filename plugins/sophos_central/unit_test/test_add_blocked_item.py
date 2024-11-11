import sys
import os

sys.path.append(os.path.abspath("../"))


from unittest import TestCase
from unittest.mock import patch
from parameterized import parameterized

from insightconnect_plugin_runtime.exceptions import PluginException

from util import Util
from icon_sophos_central.actions.add_blocked_item import AddBlockedItem


@patch("requests.request", side_effect=Util.mock_request)
class TestAddBlockedItem(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.action = Util.default_connector(AddBlockedItem())

    @parameterized.expand(
        [
            [
                "valid_data",
                Util.read_file_to_dict("inputs/add_blocked_item.json.inp"),
                Util.read_file_to_dict("expected/add_blocked_item.json.exp"),
            ],
        ]
    )
    def test_add_blocked_item(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "duplicated_sha",
                Util.read_file_to_dict("inputs/add_blocked_item_bad.json.inp"),
                "Conflict.",
                (
                    "Request made conflicts with an existing resource. Please check the API documentation "
                    "or contact Support."
                ),
            ],
        ]
    )
    def test_add_blocked_item_raise_exception(self, mock_request, test_name, input_parameters, cause, assistance):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
