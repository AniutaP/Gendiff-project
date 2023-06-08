import pytest
from gendiff.generate import generate_diff


@pytest.mark.parametrize(
    'file1, file2, formatter, expected',
    [
        (
            'tests/fixtures/filepath1.json',
            'tests/fixtures/filepath2.json',
            'stylish',
            'tests/fixtures/flat_right_result.txt',
        ),
        (
            'tests/fixtures/filepath1.yml',
            'tests/fixtures/filepath2.yml',
            'stylish',
            'tests/fixtures/flat_right_result.txt',
        ),
        (
            'tests/fixtures/file1.json',
            'tests/fixtures/file2.json',
            'stylish',
            'tests/fixtures/stylish_right_result.txt',
        ),
        (
            'tests/fixtures/file1.yml',
            'tests/fixtures/file2.yml',
            'stylish',
            'tests/fixtures/stylish_right_result.txt',
        ),
        (
            'tests/fixtures/file1.json',
            'tests/fixtures/file2.json',
            'plain',
            'tests/fixtures/plain_right_result.txt',
        ),
        (
            'tests/fixtures/file1.json',
            'tests/fixtures/file2.json',
            'json',
            'tests/fixtures/json_right_result.txt',
        ),
    ],
)
def test_generate_diff(file1, file2, formatter, expected):
    with open(expected) as right_result:
        assert generate_diff(file1, file2, formatter) == right_result.read()
