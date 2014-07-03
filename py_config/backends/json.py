#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .base import ConfigException
from .base import FileProviderBackend


class JsonProviderBackend(FileProviderBackend):
    def __init__(self, file_path, *args, **kwargs):
        super(JsonProviderBackend, self).__init__(file_path, *args, **kwargs)
        try:
            pass
        except Exception as e:
            raise ConfigException(e)

    def get(self, key, default_value=None):
        try:
            pass
        except:
            return default_value

    def set(self, key, value):
        try:
            pass
        except Exception as e:
            raise ConfigException(e)

    def delete(self, key):
        try:
            pass
        except Exception as e:
            raise ConfigException(e)

# vim: filetype=python
