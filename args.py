import argparse
import sys


def make_arg_parser():
    parser = argparse.ArgumentParser(
        description='Decorates image with white border & shadow')
    parser.add_argument(
        'input',
        nargs='?',
        type=argparse.FileType('r'),
        default=sys.stdin.buffer,
    )
    parser.add_argument(
        'output',
        nargs='?',
        type=argparse.FileType('w'),
        default=sys.stdout.buffer,
    )
    parser.add_argument(
        '--iterations',
        dest='iterations',
        type=int,
        help='Amount of blurring iterations',
        required=True,
    )
    parser.add_argument(
        '--border',
        dest='border',
        type=int,
        help='Border size',
        required=True,
    )
    parser.add_argument(
        '--offset-x',
        dest='offset_x',
        type=int,
        help='Shadow horizontal offset',
        required=True,
    )
    parser.add_argument(
        '--offset-y',
        dest='offset_y',
        type=int,
        help='Shadow vertical offset',
        required=True,
    )
    parser.add_argument(
        '--background',
        dest='background',
        type=str,
        help='Hexadecimal background color',
        required=True,
    )
    parser.add_argument(
        '--shadow',
        dest='shadow',
        type=str,
        help='Hexadecimal shadow color',
        required=True,
    )

    return parser


def parse_args() -> argparse.Namespace:
    parser: argparse.ArgumentParser = make_arg_parser()
    return parser.parse_args()
