#!/usr/bin/env python
import argparse

from gendiff import generate_diff


def main(args=None):
    parser = argparse.ArgumentParser(
        prog='gendiff', description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('--f', '--format', dest='FORMAT', help='set format of output')
    parsed_args = parser.parse_args(args)
    print(generate_diff(parsed_args.first_file, parsed_args.second_file))


if __name__ == '__main__':
    main()
