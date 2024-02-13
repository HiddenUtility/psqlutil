# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 13:26:21 2023

@author: nanik
"""

from psqlutil.querycreator.query_creator import QueryCreator

class WhereQureryCreator(QueryCreator):
    __query: str
    def __init__(self, where: dict[str,str]={}):
        self.__query = self.get_query(where)
    
    def __str__(self):
        return self.query
    
    def get_query(self, where: dict[str,str]={}) -> str:
        if len(where) == 0 : return ""
        words = [f"{k} = '{v}'" for k, v in where.items()]
        return "WHERE " + " AND ".join(words)
    
    @property
    def query(self):
        return self.__query


