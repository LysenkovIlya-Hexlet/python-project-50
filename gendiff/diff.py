import json
import yaml
from gendiff.formatters.stylish import format_stylish

def load_file(file_path):
    if file_path.endswith('.json'):
        return json.load(open(file_path))
    elif file_path.endswith(('.yaml', '.yml')):
        return yaml.safe_load(open(file_path))
    else:
        raise ValueError("Unsupported file format")

def generate_diff(file1_path, file2_path, format_name='stylish'):
    data1 = load_file(file1_path)
    data2 = load_file(file2_path)
    
    diff = build_diff(data1, data2)
    
    if format_name == 'stylish':
        return format_stylish(diff)

def build_diff(data1, data2):
    diff = {}
    all_keys = sorted(set(data1.keys()) | set(data2.keys()))
    
    for key in all_keys:
        if key not in data1:
            diff[key] = {'type': 'added', 'value': data2[key]}
        elif key not in data2:
            diff[key] = {'type': 'removed', 'value': data1[key]}
        elif data1[key] == data2[key]:
            diff[key] = {'type': 'unchanged', 'value': data1[key]}
        else:
            if isinstance(data1[key], dict) and isinstance(data2[key], dict):
                diff[key] = {'type': 'nested', 'children': build_diff(data1[key], data2[key])}
            else:
                diff[key] = {'type': 'changed', 'old': data1[key], 'new': data2[key]}
    return diff