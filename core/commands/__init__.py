#!/usr/bin/env python3
"""
Copyright (c) 2017-present, Facebook, Inc.
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree.
"""

from .cleanup import Cleanup
from .copy import Copy
from .direct import Direct

commands = [
    Direct,
    Copy,
    Cleanup,
]
