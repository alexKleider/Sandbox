#!/usr/bin/env python3

# File: Sandbox/tests/test.py

# Must first add the parent directory of the
# currently running script to the system path:
import os
import sys
sys.path.insert(0, os.path.split(sys.path[0])[0])
# print(sys.path)
# ... or alternatively set PYTHONPATH to project directory:
# export PYTHONPATH=/home/alex/Git/Sandbox

import driver
import code.accessory

print("So far, so good.")
