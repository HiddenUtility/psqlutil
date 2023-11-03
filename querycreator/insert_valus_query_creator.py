# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 13:43:12 2023

@author: nanik
"""

from querycreator.query_creator import QueryCreator

class InsertValuesQureryCreator(QueryCreator):
    __query: str
    def __init__(self, data: dict[str,str]={}):
        self.__query = self.get_query(data)
    
    def __str__(self):
        return self.query
    
    def get_query(self, data: dict[str,str]={}) -> str:
        if len(data) == 0 : return ""
        cols = []
        words = []
        for k, v in data.items():
            cols.append(k)
            words.append(f"'{v}'")

        return f"({', '.join(cols)}) VALUES ({', '.join(words)});"
    
    @property
    def query(self):
        return self.__query


