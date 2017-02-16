import json
import argparse
import sys


def load_data(datafile):
    return json.load(datafile) 


def pretty_print_json(data, outfile):
    json.dump(data, outfile, indent=4, ensure_ascii=False)


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', type=argparse.FileType('r'),
                        help='file contataining json to pretty print')
    parser.add_argument('-o', '--outfile', type=argparse.FileType('w'), 
                        default=sys.stdout,
                        help='file to output pretty json into ')
    return parser


if __name__ == '__main__':
    args = get_parser().parse_args()
    pretty_print_json(load_data(args.infile), args.outfile)

