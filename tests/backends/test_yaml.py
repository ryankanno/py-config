#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nose.tools import eq_
import os
from py_config.backends.yaml import YamlProviderBackend
import tempfile
import unittest


class TestIniProviderBackend(unittest.TestCase):

    def setUp(self):
        self.cwd = os.path.dirname(os.path.realpath(__file__))
        self.yml_file = os.path.join(self.cwd, '.', 'data', 'foobar.yml')
        self.temp_file = tempfile.TemporaryFile()

    def test_yml(self):
        provider = YamlProviderBackend(self.yml_file)
        eq_(1, provider.get('Foo.Bar', None))
        eq_("Config Data", provider.get('Bar.Foo', None))
        eq_(None, provider.get('Bar2', None))
        provider.delete('Foo.Bar')
        eq_(None, provider.get('Foo.Bar', None))
        provider.set('Foo.Bar', '2')
        eq_('2', provider.get('Foo.Bar', None))

# vim: filetype=python
