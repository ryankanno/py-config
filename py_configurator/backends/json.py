#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from .base import FileProviderBackend


class JsonProviderBackend(FileProviderBackend):
    def __init__(self, file_path, *args, **kwargs):
        super(JsonProviderBackend, self).__init__(file_path, *args, **kwargs)

    def get(self, key, default_value=None):
        raise NotImplementedError

    def set(self, key, value):
        raise NotImplementedError

    def delete(self, key):
        raise NotImplementedError

    def to_dict(self):
        raise NotImplementedError

# vim: filetype=python
