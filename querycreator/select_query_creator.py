# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 13:26:21 2023

@author: nanik
"""
from __future__ import annotations
from querycreator.query_creator import QueryCreator
from querycreator.table_query_creator import TableQueryCreator
from querycreator.where_query_creator import WhereQureryCreator

class SelectQureryCreator(QueryCreator, TableQueryCreator):
    __table_name: str
    __query: str
    def __init__(self, table_name, columns=[], where: dict[str,str]={}):
        self.__table_name = table_name
        self.__columns = columns
        self.__where = where
        self.__query = self.get_query(columns, where)
    
    def __str__(self):
        return self.query
    
    def get_query(self, columns=[], where: dict[str,str]={}) -> str:
        col_query = "*" if not columns else ", ".join([f"{v}" for v in columns])
        return f"SELECT {col_query} from {self.table_name} {WhereQureryCreator(where)};"
    
    def set_columns(self, columns: list[str]) -> SelectQureryCreator:
        return SelectQureryCreator(self.__table_name, columns, self.__where)
        
    def set_where(self, where: dict[str,str]={}) -> SelectQureryCreator:
        return SelectQureryCreator(self.__table_name, self.__columns, where)
        

    @property
    def query(self):
        return self.__query

    @property
    def table_name(self):
        return self.__table_name
