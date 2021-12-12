import os
import sys
import argparse
from pathlib import Path

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('corpus', type=str, help='Corpus path.')
    parser.add_argument('-o', '--order', type=int, help='Order of the model')

    args, _ = parser.parse_known_args(sys.argv[1:])

    corpus = Path(args.corpus)
    file_1 = corpus.parent / f'{args.order}gram.arpa'
    file_2 = corpus.parent / f'{args.order}gram.bin'

    os.system(f'lmplz -o {args.order} -S 80% < {corpus} > {file_1}')
    os.system(f'build_binary {file_1} {file_2}')

