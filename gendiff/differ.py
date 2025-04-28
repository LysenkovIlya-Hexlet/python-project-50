def compare_data(data1, data2):
    """Сравнивает два словаря и возвращает список различий"""
    keys = sorted(set(data1.keys()) | set(data2.keys()))
    diff = []
    
    for key in keys:
        if key not in data2:
            diff.append(('removed', key, data1[key]))
        elif key not in data1:
            diff.append(('added', key, data2[key]))
        elif data1[key] == data2[key]:
            diff.append(('unchanged', key, data1[key]))
        else:
            diff.append(('changed', key, data1[key], data2[key]))
    
    return diff