from gendiff.generate import generate_diff
from tests.fixtures.json_right_result import JSON_RESULT


def test_generate_diff():
    assert generate_diff('tests/fixtures/filepath1.json', 'tests/fixtures/filepath2.json') == JSON_RESULT