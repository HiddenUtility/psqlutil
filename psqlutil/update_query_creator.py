# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 14:16:39 2023

@author: nanik
"""
from __future__ import annotations
from psqlutil.query_creator import QueryCreator
from psqlutil.table_query_creator import TableQueryCreator
from psqlutil.where_query_creator import WhereQureryCreator
from psqlutil.set_valus_query_creator import SetValuesQureryCreator

class UpdateQureryCreator(QueryCreator, TableQueryCreator):
    __table_name: str
    __query: str
    def __init__(self, table_name, values: dict[str,str]={}, where: dict[str,str]={}):
        self.__table_name = table_name
        self.__values = values
        self.__where = where
        self.__query = self.get_query(values, where)
    
    def __str__(self):
        return self.query
    
    def get_query(self, values: dict[str,str]={}, where: dict[str,str]={}) -> str:
        return f"UPDATE {self.__table_name} {SetValuesQureryCreator(values)} {WhereQureryCreator(where)};"
        
    def set_values(self, values: dict[str,str]={}) -> UpdateQureryCreator:
        return UpdateQureryCreator(self.__table_name, values, self.__where)
    
    def set_where(self, where: dict[str,str]={}) -> UpdateQureryCreator:
        return UpdateQureryCreator(self.__table_name, self.__values, where)
    
    @property
    def query(self):
        return self.__query
    
    @property
    def table_name(self):
        return self.__query
