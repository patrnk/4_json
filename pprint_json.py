import json
import argparse
import sys


def load_data(filepath):
    pass


def pretty_print_json(data, outfile):
    pass


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', type=argparse.FileType('r'),
                        help='file contataining json to pretty print')
    parser.add_argument('-o', '--outfile', type=argparse.FileType('w'), 
                        default=sys.stdin,
                        help='file to output pretty json into ')
    return parser


if __name__ == '__main__':
    args = get_parser().parse_args()
    pretty_print_json(load_data(args.infile), args.outfile)

