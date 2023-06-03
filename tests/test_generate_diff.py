from gendiff.generate import generate_diff
from tests.fixtures.right_result import JSON_RESULT, YML_RESULT, STYLISH_REFERENS_RESULT, PLAIN_REFERENS_RESULT


def test_generate_diff_json():
    assert generate_diff('tests/fixtures/filepath1.json', 'tests/fixtures/filepath2.json') == JSON_RESULT


def test_generate_diff_yml():
    assert generate_diff('tests/fixtures/filepath1.yml', 'tests/fixtures/filepath2.yml') == YML_RESULT


def test_generate_diff_stylish_json():
    assert generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json') == STYLISH_REFERENS_RESULT


def test_generate_diff_stylish_yml():
    assert generate_diff('tests/fixtures/file1.yml', 'tests/fixtures/file2.yml') == STYLISH_REFERENS_RESULT


def test_generate_diff_plain_json():
    assert generate_diff('tests/fixtures/file1.yml', 'tests/fixtures/file2.yml', 'plain') == PLAIN_REFERENS_RESULT