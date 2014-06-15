#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nose.tools import eq_
import os
from py_config.backends.ini import IniProviderBackend
import unittest


class TestIniProviderBackend(unittest.TestCase):

    def setUp(self):
        self.cwd = os.path.dirname(os.path.realpath(__file__))
        self.ini_file = os.path.join(self.cwd, '.', 'data', 'foobar.ini')

    def test_ini(self):
        provider = IniProviderBackend(self.ini_file)
        eq_('1', provider.get('Foo.Bar', None))
        eq_("Config Data", provider.get('Bar.Foo', None))
        eq_(None, provider.get('Bar', None))
        provider.delete('Foo.Bar')
        eq_(None, provider.get('Foo.Bar', None))
        provider.set('Foo.Bar', '2')
        eq_('2', provider.get('Foo.Bar', None))

# vim: filetype=python
