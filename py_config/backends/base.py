#!/usr/bin/env python
# -*- coding: utf-8 -*-

import abc


class BaseProviderBackend(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get(self, key, defaul_value):
        return

    @abc.abstractmethod
    def set(self, key, value):
        return

# vim: filetype=python
