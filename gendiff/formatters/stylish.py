def format_stylish(diff):
    """Форматирует diff в stylish-формат"""
    lines = []
    for item in diff:
        status = item[0]
        key = item[1]
        
        if status == 'unchanged':
            lines.append(f"    {key}: {format_value(item[2])}")
        elif status == 'removed':
            lines.append(f"  - {key}: {format_value(item[2])}")
        elif status == 'added':
            lines.append(f"  + {key}: {format_value(item[2])}")
        elif status == 'changed':
            lines.append(f"  - {key}: {format_value(item[2])}")
            lines.append(f"  + {key}: {format_value(item[3])}")
    
    return "{\n" + "\n".join(lines) + "\n}"

def format_value(value):
    """Форматирует значение для вывода"""
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    return str(value)