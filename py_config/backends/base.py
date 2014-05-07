#!/usr/bin/env python
# -*- coding: utf-8 -*-

import abc


class BaseProviderBackend(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get(self, key, default_value):
        raise NotImplementedError

    @abc.abstractmethod
    def set(self, key, value):
        raise NotImplementedError

# vim: filetype=python
