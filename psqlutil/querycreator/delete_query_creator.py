# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 14:15:55 2023

@author: nanik
"""
from __future__ import annotations
from psqlutil.querycreator.query_creator import QueryCreator
from psqlutil.querycreator.table_query_creator import TableQueryCreator
from psqlutil.querycreator.where_query_creator import WhereQureryCreator

class DeleteQureryCreator(QueryCreator, TableQueryCreator):
    __table_name: str
    __query: str
    def __init__(self, table_name, where: dict[str,str]={}):
        self.__table_name = table_name
        self.__where = where
        self.__query = self.get_query(where)
    
    def __str__(self):
        return self.query
    
    def get_query(self, where: dict[str,str]={}) -> str:
        return f"DELETE FROM {self.__table_name} {WhereQureryCreator(where)};"
    
    def set_where(self, where: dict[str,str]={}) -> DeleteQureryCreator:
        return DeleteQureryCreator(self.__table_name, where)
    
    @property
    def query(self):
        return self.__query

    @property
    def table_name(self):
        return self.__query
