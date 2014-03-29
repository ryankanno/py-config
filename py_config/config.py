#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

logger = logging.getLogger(__name__)


class Config(object):
    def __init__(self, provider):
        self.provider = provider

    def get(self, name, default_value):
        return self.provider.get(name) or default_value

    def set(self, name, value):
        return self.provider.set(name, value)


# vim: filetype=python
