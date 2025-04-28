from gendiff.differ import compare_data
from gendiff.formatters.stylish import format_stylish
from gendiff.parsers import parse_file

def generate_diff(file1_path, file2_path, format_name='stylish'):
    """Основной интерфейс библиотеки"""
    data1 = parse_file(file1_path)
    data2 = parse_file(file2_path)
    diff = compare_data(data1, data2)
    return format_stylish(diff)