#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base import ConfigException
from base import FileProviderBackend
import ConfigParser


class IniProviderBackend(FileProviderBackend):
    def __init__(self, file_path):
        super(IniProviderBackend, self).__init__(file_path)
        try:
            self._config = ConfigParser.SafeConfigParser()
            self._config.read(self.file_path)
        except ConfigParser.MissingSectionHeaderError as e:
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
            if len(key_split) == 1:
                section = key_split[0]
                self._config.remove_section(section)
            elif len(key_split) == 2:
                section, option = key_split[0], key_split[1]
                self._config.remove_option(section, option)
        except Exception as e:
            raise ConfigException(e)

    def write(self, file_obj):
        return self._config.write(file_obj)


# vim: filetype=python
