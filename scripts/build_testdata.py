#!/usr/bin/env python3
#
# This python file contains utility scripts to rebuild testdata files
# It trims windows carriage 0xD chars, multiple space chars
# and concatenate files
#
# Execute command
# ./build_testdata.py --help

import os
from argparse import ArgumentParser

def build(options):
    with open(options.output, 'w') as outfile:
        for filename in options.files:
            with open(filename) as infile:
                for line in infile:
                    x, y, z = line.strip().split()
                    if z == "-9999.99": continue
                    outfile.write(' '.join((x, y, z)) + '\n')

if __name__ == "__main__":
    current_dir = os.path.dirname(__file__)
    parser = ArgumentParser(description="Beautify and concatenate testdata")
    parser.add_argument("-o", "--output", default=os.path.join(current_dir, "../testdata/build.xyz"),
                        help="Specify output file")
    parser.add_argument("files", nargs="*", default=[],
                        help="Specify input files")
    options = parser.parse_args()

    build(options)

