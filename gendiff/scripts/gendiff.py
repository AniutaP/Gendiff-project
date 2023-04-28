#!/usr/bin/env python3
from gendiff.cli import make_parse_args
from gendiff import generate_diff


def main():
    args = make_parse_args()
    first_file = args.first_file
    second_file = args.second_file
    generate_diff(first_file, second_file)


if __name__ == '__main__':
    main()
