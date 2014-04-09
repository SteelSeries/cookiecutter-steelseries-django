#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import random

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
