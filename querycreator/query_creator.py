# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 13:25:21 2023

@author: nanik
"""


from abc import ABC, abstractmethod, abstractproperty

class QueryCreator(ABC):
    __query: str

    
    def __str__(self):
        return self.query
    
    @abstractmethod
    def get_query(self, data: dict[str,str]={}) -> str:
        raise NotImplementedError()

    
    @abstractproperty
    def query(self):
        raise NotImplementedError()