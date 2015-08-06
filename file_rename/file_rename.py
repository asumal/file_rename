__author__ = 'Arjun'

from abc import ABCMeta
from os import listdir
from os.path import isfile, join


class GenericParent(object):
    __metaclass__ = ABCMeta

    def __str__(self):
        pass

    def __repr__(self):
        pass


class ListOfFiles(GenericParent):
    def __init__(self, path_to_files):
        self.path_to_files = get_files(path_to_files)


def get_files(path_to_file):
    result =  [f for f in listdir(path_to_file) if isfile(join(path_to_file, f))]
    print result
    return result


