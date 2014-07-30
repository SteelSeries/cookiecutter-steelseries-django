#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import random

from binaryornot.check import is_binary


def generate_random_key():
    # Generate a secret key
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*(-_+)'
    sysrandom = random.SystemRandom()
    secret_key = ''.join([sysrandom.choice(alphabet) for i in range(50)])

    # Put it in the env file
    for path, dirs, files in os.walk('.'):
        for filename in files:
            if filename == '.env':
                with open(os.path.join(path, filename), 'r+') as f:
                    without_key = f.read()
                    with_key = without_key.replace('SECRET_KEY=""', 'SECRET_KEY="%s"' % secret_key)
                    f.seek(0)
                    f.write(with_key)


def ensure_newlines():
    root_path = os.getcwd()
    for dirpath, dirnames, filenames in os.walk(root_path):
        for filename in filenames:
            path = os.path.join(dirpath, filename)
            if not is_binary(path):
                fd = open(path, 'a+b')
                try:
                    fd.seek(-1, os.SEEK_END)
                    if not fd.read(1) == '\n':
                        fd.seek(0, os.SEEK_END)
                        fd.write('\n')
                except IOError:
                    # This was an empty file, so do nothing
                    pass


if __name__ == '__main__':
    generate_random_key()
    ensure_newlines()
