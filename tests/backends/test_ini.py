#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nose.tools import eq_
from nose.tools import ok_
from nose.tools import raises
import os
from py_configurator.backends.base import ConfigException
from py_configurator.backends.ini import IniProviderBackend
import unittest


class TestIniProviderBackend(unittest.TestCase):

    def setUp(self):
        self.cwd = os.path.dirname(os.path.realpath(__file__))
        self.ini_file = os.path.join(self.cwd, '.', 'data', 'foobar.ini')
        self.invalid_ini_file = os.path.join(self.cwd, '.', 'data',
                                             'foobar-invalid.ini')
        self.provider = IniProviderBackend(self.ini_file)

    def test_ini_get(self):
        eq_('1', self.provider.get('Foo.Bar', None))
        eq_("Config Data", self.provider.get('Bar.Foo', None))

    def test_ini_get_default(self):
        eq_(None, self.provider.get('Bar', None))
        eq_(10000, self.provider.get('BarBar', 10000))

    def test_ini_set(self):
        self.provider.set('Foo.Bar', '2')
        eq_('2', self.provider.get('Foo.Bar', None))

        # New
        self.provider.set('FoosBallSection.Price', '$.50')
        eq_('$.50', self.provider.get('FoosBallSection.Price', None))

    def test_ini_delete(self):
        eq_('1', self.provider.get('Foo.Bar', None))
        self.provider.delete('Foo.Bar')
        eq_(None, self.provider.get('Foo.Bar', None))

    def test_ini_to_dict(self):
        ini_dict = self.provider.to_dict()
        ok_(ini_dict["Foo"]["bar"] == "1")
        ok_(ini_dict["Bar"]["foo"] == "Config Data")

    @raises(ConfigException)
    def test_ini_set_with_bad_key(self):
        self.provider.set('Foo', 'Bar')

    @raises(ConfigException)
    def test_ini_with_invalid_delete_should_raise_exception(self):
        provider = IniProviderBackend(self.ini_file)
        provider.delete('Foo')

    @raises(ConfigException)
    def test_invalid_ini_should_raise_exception(self):
        IniProviderBackend(self.invalid_ini_file)

    @raises(ConfigException)
    def test_non_existent_ini_should_raise_exception(self):
        IniProviderBackend("skfdjaskldjalksdfjasklfaf")

# vim: filetype=python
