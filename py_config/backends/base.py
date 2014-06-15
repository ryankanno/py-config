#!/usr/bin/env python
# -*- coding: utf-8 -*-

import abc


class ConfigException(Exception):
    pass


class BaseProviderBackend(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get(self, key, default_value):
        raise NotImplementedError

    @abc.abstractmethod
    def set(self, key, value):
        raise NotImplementedError

    @abc.abstractmethod
    def delete(self, key):
        raise NotImplementedError


class FileProviderBackend(BaseProviderBackend):
    def __init__(self, file_path):
        self._file_path = file_path

    @property
    def file_path(self):
        return self._file_path


# vim: filetype=python
