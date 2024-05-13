#!/usr/bin/python3
"""Module packaging for the test_console.py file"""
import os
from typing import TextIO
from models.engine.file_storage import FileStorage


def clearfilecontents(file_stream: TextIO):
    """Clears the contents of the file stream"""
    if file_stream.seekable():
        file_stream.seek(0)
        file_stream.truncate(0)


def removefile(path: str):
    """Deletes a file if it exists"""
    if os.path.isfile(path):
        os.unlink(path)


def resetstorage(data_store: FileStorage, path='file.json'):
    """Resets items stored in a data store"""
    with open(path, mode='w') as fl:
        fl.write('{}')
        data_store.reload() if data_store else None


def readfilecontents(filename):
    """Reads the contents of the file"""
    file_content = []
    if os.path.isfile(filename):
        with open(filename, mode='r') as fl:
            for file_content in fl.readlines():
                file_content.append(file_content)
    return ''.join(file_content)


def writetofile(filename, content):
    """Writes content to a file"""
    with open(filename, mode='w') as fl:
        fl.write(content)
