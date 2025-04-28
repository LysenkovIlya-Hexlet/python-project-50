import pytest
from gendiff import generate_diff

@pytest.mark.parametrize("file1, file2", [
    ("file1.json", "file2.json"),
    ("file1.yml", "file2.yml")  # Новый тест для YAML
])
def test_generate_diff(file1, file2):
    fixture_path = "tests/test_data/"
    expected = open(f"{fixture_path}expected_result.txt").read().strip()
    assert generate_diff(f"{fixture_path}{file1}", f"{fixture_path}{file2}") == expected