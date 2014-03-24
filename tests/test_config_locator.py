#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nose.tools import eq_
from py_config import ConfigLocator
import unittest


class TestConfigLocator(unittest.TestCase):

    def test_config_locator_construction(self):
        config_name = 'foo.bar'
        local_dir = '/foo/bar/tmp'
        env_key = 'CONFIG_KEY'

        locator = ConfigLocator(
            config_name=config_name,
            local_dir=local_dir,
            env_key=env_key)

        eq_(locator.config_name, config_name)
        eq_(locator.local_dir, local_dir)
        eq_(locator.env_key, env_key)

        config_name_2 = 'foo.bar.2'
        local_dir_2 = '/foo/bar/tmp/2'
        env_key_2 = 'CONFIG_KEY_2'
        locator.config_name = config_name_2
        locator.local_dir = local_dir_2
        locator.env_key = env_key_2

        eq_(locator.config_name, config_name_2)
        eq_(locator.local_dir, local_dir_2)
        eq_(locator.env_key, env_key_2)

    def test_config_locator_get_config_search_paths(self):
        pass


# vim: filetype=python
