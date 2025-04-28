from gendiff import generate_diff
from gendiff.cli import parse_args
import sys

def main():
    try:
        args = parse_args()  # Теперь args содержит распарсенные аргументы
        print(generate_diff(args.first_file, args.second_file))
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()