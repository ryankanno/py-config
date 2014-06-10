#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base import BaseProviderBackend


class DictionaryProviderBackend(BaseProviderBackend):
    def __init__(self, dict):
        self._dict = dict or {}

    def get(self, key, default_value):
        try:
            return self._dict[key]
        except:
            return default_value

    def set(self, key, value):
        self._dict[key] = value

    def delete(self, key):
        if key in self._dict:
            del self._dict[key]

# vim: filetype=python
