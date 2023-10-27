# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 14:17:14 2023

@author: nanik
"""
from __future__ import annotations
from psqlutil.query_creator import QueryCreator
from psqlutil.table_query_creator import TableQueryCreator
from psqlutil.where_query_creator import WhereQureryCreator
from psqlutil.insert_valus_query_creator import InsertValuesQureryCreator

class InsertIntoQureryCreator(QueryCreator, TableQueryCreator):
    __table_name: str
    __query: str
    def __init__(self, table_name, data: dict[str,str]={}):
        self.__table_name = table_name
        self.__data = data
        self.__query = self.get_query(data)
    
    def __str__(self):
        return self.query
    
    def get_query(self, data:dict[str,str] , where: dict[str,str]={}) -> str:
        return f"INSERT INTO {self.__table_name} {InsertValuesQureryCreator(data)};"
        
    def set_data(self, data: dict[str,str]={}) -> InsertIntoQureryCreator:
        return InsertIntoQureryCreator(self.__table_name, data)
    

    @property
    def query(self):
        return self.__query
    
    @property
    def table_name(self):
        return self.__query
