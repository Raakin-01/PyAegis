#
# Copyright 2014 Hewlett-Packard Development Company, L.P.
#
# SPDX-License-Identifier: Apache-2.0
from importlib import metadata

from bandit.core import config  # noqa
from bandit.core import context  # noqa
from bandit.core import manager  # noqa
from bandit.core import meta_ast  # noqa
from bandit.core import node_visitor  # noqa
from bandit.core import test_set  # noqa
from bandit.core import tester  # noqa
from bandit.core import utils  # noqa
from bandit.core.constants import *  # noqa
from bandit.core.issue import *  # noqa
from bandit.core.test_properties import *  # noqa

try:
    __author__ = metadata.metadata("pyaegis")["Author"]
    __version__ = metadata.version("pyaegis")
except metadata.PackageNotFoundError:
    # Backwards compatibility for environments where the distribution is
    # still installed under its historical "bandit" name.
    __author__ = metadata.metadata("bandit")["Author"]
    __version__ = metadata.version("bandit")
