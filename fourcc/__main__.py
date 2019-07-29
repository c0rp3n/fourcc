#! /usr/bin/env python3

import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description='Four chars to combined hex value.')
    parser.add_argument('chars', metavar='C', help='four chars to be combined')
    parser.add_argument('-l', '--little', action='store_true', help='output little endian fourcc')
    parser.add_argument('-b', '--big', action='store_true', help='output big endian fourcc')
                        
    args = parser.parse_args()

    assert len(args.chars) == 4

    b = bytes(args.chars, 'utf-8')

    assert not (args.little and args.big)
    if args.little:
        byteorder = 'little'
    elif args.big:
        byteorder = 'big'
    else:
        byteorder = sys.byteorder
    
    fourcc = int.from_bytes(b, byteorder)
    print(hex(fourcc))

if __name__ == '__main__':
    main()
