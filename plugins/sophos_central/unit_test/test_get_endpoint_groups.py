import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import PluginException


from util import Util
from parameterized import parameterized
from icon_sophos_central.actions.get_endpoint_groups import GetEndpointGroups


@patch("requests.request", side_effect=Util.mock_request)
class TestGetEndpointGroups(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetEndpointGroups())

    @parameterized.expand(
        [
            [
                "all",
                Util.read_file_to_dict("inputs/get_endpoint_groups_all.json.inp"),
                Util.read_file_to_dict("expected/get_endpoint_groups_all.json.exp"),
            ],
            [
                "specified_fields",
                Util.read_file_to_dict("inputs/get_endpoint_groups_specified_fields.json.inp"),
                Util.read_file_to_dict("expected/get_endpoint_groups_specified_fields.json.exp"),
            ],
            [
                "with_search",
                Util.read_file_to_dict("inputs/get_endpoint_groups_with_search.json.inp"),
                Util.read_file_to_dict("expected/get_endpoint_groups_with_search.json.exp"),
            ],
            [
                "with_ids",
                Util.read_file_to_dict("inputs/get_endpoint_groups_with_ids.json.inp"),
                Util.read_file_to_dict("expected/get_endpoint_groups_with_ids.json.exp"),
            ],
            [
                "not_found",
                Util.read_file_to_dict("inputs/get_endpoint_groups_not_found.json.inp"),
                Util.read_file_to_dict("expected/get_endpoint_groups_not_found.json.exp"),
            ],
        ]
    )
    def test_get_endpoint_groups(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertDictEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "invalid",
                Util.read_file_to_dict("inputs/get_endpoint_groups_invalid.json.inp"),
                "Bad request.",
                "The API client sent a malformed request.",
            ],
        ]
    )
    def test_get_endpoint_groups_raise_exception(self, mock_request, test_name, input_parameters, cause, assistance):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
