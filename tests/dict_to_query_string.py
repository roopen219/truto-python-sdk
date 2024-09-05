import unittest
import datetime

from truto_python_sdk.dict_to_query_string import dict_to_query_string

class TestDictToQueryString(unittest.TestCase):

    def test_simple_params(self):
        query_params = {"name": "foo", "limit": 10}
        expected = "name=foo&limit=10"
        self.assertEqual(dict_to_query_string(query_params), expected)

    def test_boolean_param(self):
        query_params = {"is_active": True}
        expected = "is_active=true"
        self.assertEqual(dict_to_query_string(query_params), expected)

    def test_nested_object(self):
        query_params = {"foo": {"bar": "baz"}}
        expected = "foo%5Bbar%5D=baz"
        self.assertEqual(dict_to_query_string(query_params), expected)

    def test_array(self):
        query_params = {"foo": ["bar", "baz"]}
        expected = "foo%5B%5D=bar&foo%5B%5D=baz"
        self.assertEqual(dict_to_query_string(query_params), expected)

    def test_mixed_params(self):
        query_params = {
            "name": "foo",
            "is_active": True,
            "foo": {"bar": "baz"},
            "foo_array": ["bar", {"bar1": "baz1"}],
        }
        expected = (
            "name=foo&is_active=true&foo%5Bbar%5D=baz&foo_array%5B%5D=bar&foo_array%5B%5D%5Bbar1%5D=baz1"
        )
        self.assertEqual(dict_to_query_string(query_params), expected)

    def test_date_param(self):
        query_params = {
            "created_at": {
                "gte": datetime.datetime(2021, 1, 1, 0, 0, 0),
                "lte": datetime.datetime(2021, 1, 31, 23, 59, 59),
            }
        }
        expected = (
            "created_at%5Bgte%5D=2021-01-01T00%3A00%3A00&created_at%5Blte%5D=2021-01-31T23%3A59%3A59"
        )
        self.assertEqual(dict_to_query_string(query_params), expected)

if __name__ == "__main__":
    unittest.main()