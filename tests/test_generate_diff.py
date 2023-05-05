from gendiff.generate import generate_diff
from tests.fixtures.right_result import JSON_RESULT, YML_RESULT


def test_generate_diff_json():
    assert generate_diff('tests/fixtures/filepath1.json', 'tests/fixtures/filepath2.json') == JSON_RESULT


def test_generate_diff_yml():
    assert generate_diff('tests/fixtures/filepath1.yml', 'tests/fixtures/filepath2.yml') == YML_RESULT
