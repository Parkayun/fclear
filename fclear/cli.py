# -*- coding:utf-8 -*-
from argparse import ArgumentParser, RawTextHelpFormatter
from sys import argv

from .cleaner import Cleaner


def run():
    parser = ArgumentParser(description='Clear compiled files.',
                            formatter_class=RawTextHelpFormatter)
    parser.add_argument('language', type=str, help='\n'.join((
        'python ------ Remove pyc, __pycache__',
        'py ---------- Remove pyc, __pycache__',
        'java -------- Remove class',
        'vim --------- Remove swp',
        'vi ---------- Remove swp',
    )))

    cleaner = Cleaner(parser.parse_args().language)
    cleaner.run()
