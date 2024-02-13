# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 13:25:21 2023

@author: nanik
"""


from abc import ABC, abstractproperty

class TableQueryCreator(ABC):
    __table_name: str

    
    @abstractproperty
    def table_name(self):
        raise NotImplementedError()