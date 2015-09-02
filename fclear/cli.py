# -*- coding:utf-8 -*-
from sys import argv

from .cleaner import Cleaner


def run():
    try:
        language = argv[1]
    except IndexError:
        language = ''

    cleaner = Cleaner(language)
    cleaner.run()

run()
