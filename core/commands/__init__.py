"""
Copyright (c) 2017-present, Facebook, Inc.
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree.
"""


from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from .direct import Direct
from .copy import Copy
from .cleanup import Cleanup

commands = [
    Direct,
    Copy,
    Cleanup,
]
