#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .base import ConfigException
from .base import FileProviderBackend
try:
    import ConfigParser as parser
except ImportError:
    import configparser as parser


class IniProviderBackend(FileProviderBackend):
    def __init__(self, file_path, *args, **kwargs):
        super(IniProviderBackend, self).__init__(file_path, *args, **kwargs)
        try:
            self._config = parser.SafeConfigParser()
            self._config.read(self.file_path)
        except parser.MissingSectionHeaderError as e:
            raise ConfigException(e)

    def get(self, key, default_value=None):
        try:
            section, option = key.split('.')
            return self._config.get(section, option)
        except:
            return default_value

    def set(self, key, value):
        try:
            section, option = key.split('.')
            if not self._config.has_section(section):
                self._config.add_section(section)
            self._config.set(section, option, value)
        except Exception as e:
            raise ConfigException(e)

    def delete(self, key):
        try:
            key_split = key.split('.')
            if len(key_split) == 2:
                section, option = key_split[0], key_split[1]
                self._config.remove_option(section, option)
            else:
                raise Exception("Must include a section header")
        except Exception as e:
            raise ConfigException(e)


# vim: filetype=python
