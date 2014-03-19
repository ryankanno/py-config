#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import os

logger = logging.getLogger(__name__)

PY_CONFIG_PATH = "PY_CONFIG_FILE"


class ConfigLocator(object):
    def __init__(self, cwd, config_name):
        self.cwd = cwd
        self.config_name = config_name

    def get_config(self):
        pass

    def get_search_paths(self):
        paths = ["{0}/{1}".format(self._get_home_dir(), self.config_name)]
        return paths

    def _get_curr_dir(self):
        return self.cwd

    def _get_home_dir(self):
        return os.path.expanduser("~")

    def _get_system_dir(self):
        return ""

    def _get_env_dir(self):
        return os.environ.get(PY_CONFIG_PATH, None)

# vim: filetype=python
