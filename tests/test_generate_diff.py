import pytest
import os.path
from gendiff.generate import generate_diff


@pytest.mark.parametrize(
    'file1, file2, formatter, expected',
    [
        (
            'file1.json',
            'file2.json',
            'stylish',
            'stylish_right_result.txt',
        ),
        (
            'file1.yml',
            'file2.yml',
            'stylish',
            'stylish_right_result.txt',
        ),
        (
            'file1.json',
            'file2.json',
            'plain',
            'plain_right_result.txt',
        ),
        (
            'file1.json',
            'file2.json',
            'json',
            'json_right_result.txt',
        ),
    ],
)
def test_generate_diff(file1, file2, formatter, expected):
    fixtures_path = os.path.join(os.path.dirname(__file__), 'fixtures')
    file1_path = os.path.join(fixtures_path, file1)
    file2_path = os.path.join(fixtures_path, file2)
    expected_path = os.path.join(fixtures_path, expected)
    with open(expected_path) as right_result:
        assert generate_diff(file1_path, file2_path, formatter) == right_result.read()
