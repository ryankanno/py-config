#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nose.tools import eq_
from nose.tools import ok_
import os
from py_config.backends.ini import IniProviderBackend
import tempfile
import unittest


class TestIniProviderBackend(unittest.TestCase):

    def setUp(self):
        self.cwd = os.path.dirname(os.path.realpath(__file__))
        self.ini_file = os.path.join(self.cwd, '.', 'data', 'foobar.ini')
        self.temp_file = tempfile.TemporaryFile()

    def test_ini(self):
        provider = IniProviderBackend(self.ini_file)
        eq_('1', provider.get('Foo.Bar', None))
        eq_("Config Data", provider.get('Bar.Foo', None))
        eq_(None, provider.get('Bar', None))
        provider.delete('Foo.Bar')
        eq_(None, provider.get('Foo.Bar', None))
        provider.set('Foo.Bar', '2')
        eq_('2', provider.get('Foo.Bar', None))

    def test_ini_save(self):
        provider = IniProviderBackend(self.ini_file)
        provider.delete('Foo.Bar')
        provider.set('Foo.Bar2', '2')
        provider.write(self.temp_file)
        self.temp_file.seek(0)
        contents = self.temp_file.read()
        ok_("bar2 = 2" in contents)


# vim: filetype=python
