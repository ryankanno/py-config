#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nose.tools import eq_
from nose.tools import ok_
from py_configurator.backends.dict import DictionaryProviderBackend
import unittest


class TestDictionaryProviderBackend(unittest.TestCase):

    def setUp(self):
        self.dict = {'foo': 'bar', 'too': 'much'}
        self.provider = DictionaryProviderBackend(self.dict)

    def test_dict_get(self):
        eq_('bar', self.provider.get('foo', None))
        eq_('much', self.provider.get('too', None))

    def test_dict_get_default(self):
        eq_(None, self.provider.get('foo2', None))
        eq_(1, self.provider.get('foo3', 1))

    def test_dict_set(self):
        self.provider.set('python', 'rules')
        eq_('rules', self.provider.get('python', None))

    def test_dict_delete(self):
        self.provider.delete('foo')
        eq_(-1, self.provider.get('foo', -1))

    def test_dict_to_dict(self):
        eq_(self.dict, self.provider.to_dict())
        self.provider.delete('foo')
        ok_(self.dict != self.provider.to_dict())


# vim: filetype=python
