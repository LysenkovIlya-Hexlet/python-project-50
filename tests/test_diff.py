import os
from gendiff import generate_diff

def get_fixture_path(file_name):
    return os.path.join('tests/test_data', file_name)

def read_file(file_path):
    with open(file_path) as f:
        return f.read()

def test_flat_json_diff():
    file1 = get_fixture_path('file1.json')
    file2 = get_fixture_path('file2.json')
    expected = read_file(get_fixture_path('expected_result.txt'))
    
    assert generate_diff(file1, file2) == expected