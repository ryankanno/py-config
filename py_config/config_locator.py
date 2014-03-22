#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import os

logger = logging.getLogger(__name__)

PY_CONFIG_KEY = "PY_CONFIG_FILE"


class ConfigLocator(object):
    def __init__(self, config_name, local_dir='./', env_key=PY_CONFIG_KEY):
        self.config_name = config_name
        self.env_key = env_key
        self.local_dir = local_dir

    def get_config_search_paths(self):
        return [os.path.join(path, self.config_name)
                for path in self._get_search_paths]

    def _get_search_paths(self):
        return [
            self._get_env_dir(),
            self._get_local_dir(),
            self._get_home_dir(),
            self._get_system_dir()
        ]

    def _get_local_dir(self):
        return self.local_dir

    def _get_home_dir(self):
        return os.path.expanduser("~")

    def _get_system_dir(self):
        return ""

    def _get_env_dir(self):
        return os.environ.get(self.env_key, None)

# vim: filetype=python
