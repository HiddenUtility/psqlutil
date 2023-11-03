# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 13:50:41 2023

@author: nanik
"""

from querycreator.query_creator import QueryCreator

class SetValuesQureryCreator(QueryCreator):
    __query: str
    def __init__(self, data: dict[str,str]={}):
        self.__query = self.get_query(data)
    
    def __str__(self):
        return self.query
    
    def get_query(self, data: dict[str,str]={}) -> str:
        if len(data) == 0 : return ""
        values = [f"{k} = '{v}'" for k, v in data.items()]
        return f"SET {', '.join(values)} "

    @property
    def query(self):
        return self.__query



