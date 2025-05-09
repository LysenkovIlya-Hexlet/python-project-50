import argparse

def parse_args():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file', help='Path to first file')
    parser.add_argument('second_file', help='Path to second file')
    parser.add_argument('-f', '--format', 
                       help='set format of output',
                       default='stylish')
    return parser.parse_args()  # Возвращаем результат parse_args(), а не parser