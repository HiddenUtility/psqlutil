# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 17:49:58 2023

@author: nanik
"""
from __future__ import annotations
from abc import ABCMeta, abstractmethod

class Psql(metaclass=ABCMeta):
    @abstractmethod
    def __add__(self):...
    @abstractmethod
    def to_querys(self):...
    @abstractmethod
    def set_query(self):...
    @abstractmethod
    def commit(self):...
