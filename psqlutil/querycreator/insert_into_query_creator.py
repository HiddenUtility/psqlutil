# -*- coding: utf-8 -*-
from __future__ import annotations
from psqlutil.querycreator.query_creator import QueryCreator
from psqlutil.querycreator.table_query_creator import TableQueryCreator
from psqlutil.querycreator.insert_valus_query_creator import InsertValuesQureryCreator


class InsertIntoQureryCreator(QueryCreator, TableQueryCreator):
    __table_name: str
    __query: str
    def __init__(self, table_name, data: dict[str,str]={}):
        self.__table_name = table_name
        self.__data = data
        self.__query = self.get_query()
    
    def __str__(self):
        return self.query
    
    def get_query(self) -> str:
        return f"INSERT INTO {self.__table_name} {InsertValuesQureryCreator(self.__data)};"
        
    def set_data(self, data: dict[str,str]) -> InsertIntoQureryCreator:
        return InsertIntoQureryCreator(self.__table_name, data)
    
    @property
    def query(self):
        return self.__query
    
    @property
    def table_name(self):
        return self.__query
