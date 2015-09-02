# -*- coding:utf-8 -*-
from __future__ import print_function
from shutil import rmtree
from os import listdir as _listdir, remove
from os.path import abspath, isdir, join as path_join

from .exception import LanguageNotFound


class Cleaner(object):

    def __init__(self, language):
        self.language = language

    @property
    def extensions_to_delete(self):
        if not hasattr(self, '__extension__'):
            if self.language in ('py', 'python',):
                self.__extension__ = ('pyc', '__pycache__',)
            else:
                raise LanguageNotFound
        return self.__extension__

    def clear(self, path):
        for _file in _listdir(path):
            full_path = path_join(path, _file)
            if isdir(full_path):
                if _file in self.extensions_to_delete:
                    try:
                        rmtree(full_path)
                        print('Removed', ''.join((full_path, '/')))
                    except OSError:
                        print('Permission denied', full_path)
                else:
                    self.clear(full_path)
            else:
                try:
                    if _file.split('.')[1] in self.extensions_to_delete:
                        remove(full_path)
                        print('Removed', full_path)
                except OSError:
                    print('Permission denied', full_path)
                except IndexError:
                    pass

    def run(self):
        try:
            extensions = self.extensions_to_delete
            self.clear(abspath('.'))
        except LanguageNotFound:
            print('Language not found.')
