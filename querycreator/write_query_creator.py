# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 19:06:17 2023

@author: nanik
"""

from __future__ import annotations
from querycreator.query_creator import QueryCreator
from querycreator.table_query_creator import TableQueryCreator


from querycreator.delete_query_creator import DeleteQureryCreator
from querycreator.insert_into_query_creator import InsertIntoQureryCreator

class WriteQureryCreator(QueryCreator, TableQueryCreator):
    __table_name: str
    __query: str
    def __init__(self, table_name, values: dict[str,str]={}, where: dict[str,str]={}):
        self.__table_name = table_name
        self.__values = values
        self.__where = where
        self.__query = self.get_query(values, where)
    
    def __str__(self):
        return self.query
    
    def get_query(self, data: dict[str,str], where: dict[str,str]) -> str:
        query = f"""
{DeleteQureryCreator(self.__table_name).set_where(where)}
{InsertIntoQureryCreator(self.__table_name).set_data(data)}
        """
        return query
        
        
    def set_values(self, values: dict[str,str]={}) -> WriteQureryCreator:
        return WriteQureryCreator(self.__table_name, values, self.__where)
    
    def set_where(self, where: dict[str,str]={}) -> WriteQureryCreator:
        return WriteQureryCreator(self.__table_name, self.__values, where)
    
    @property
    def query(self):
        return self.__query
    
    @property
    def table_name(self):
        return self.__query

