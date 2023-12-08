# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 17:49:58 2023

@author: nanik
"""
from __future__ import annotations
from abc import ABCMeta, abstractmethod
from psqlutil.connection_information import ConnectioinInfromation
from copy import copy
import re

class Psql(metaclass=ABCMeta):
    @abstractmethod
    def set_query():
        pass

class Creator(Psql):
    @abstractmethod
    def set_querys():
        pass
    @abstractmethod
    def commit():
        pass
    
class TableEditor(Psql):
    @abstractmethod
    def set_querys():
        pass
    @abstractmethod
    def commit():
        pass

class Reader(Psql):
    @abstractmethod
    def get_df():
        pass

class Psql():
    #//Field
    _info: ConnectioinInfromation
    querys: list[str] 
    def __init__(self, info: ConnectioinInfromation=None, querys: list[str] = None):
        if info is None:
            info =  ConnectioinInfromation()
        if not isinstance(info, ConnectioinInfromation): raise TypeError("NOT ConnectioinInfromation Object")
        if not info.can_connect():raise ConnectionError("SQLに接続できません。")
        self._info = info
        self.querys = [] if querys is None else querys

    def __add__(self,obj: Psql) -> Psql:
        if not isinstance(obj, Psql): raise TypeError()
        self.querys += obj.querys
        return Psql(self.info ,self.querys)
    
    def __str__(self):
        return "\n".join(self.querys)
    
    def __repr__(self):
        return self.__str__()

    @staticmethod
    def _in_query(query: str, key: str) -> bool:
        # 大文字小文字を区別せずにキーワードを検索
        pattern = re.compile(re.escape(key), re.IGNORECASE)
        match_ = pattern.search(query)
        return match_ is not None
    
    @staticmethod
    def _get_column_query(columns: list[str]) -> str:
        if not isinstance(columns, list): raise TypeError("columns = {columns} is NOT list")
        if len(columns) == 0: return "*"
        return ", ".join(columns)
    @staticmethod
    def _get_where_query(where: dict) -> str:
        if not isinstance(where, dict): raise TypeError("where = {where} is NOT dictionary")
        if len(where) == 0: return ""
        wheres = [f" {k} = '{v}'" for k, v in where.items()]
        return f"WHERE {' AND'.join(wheres)}"
    @staticmethod
    def _get_set_query(values: dict) -> str:
        if not isinstance(values, dict): raise TypeError("values = {values} is NOT dictionary")
        if len(values) == 0: return ""
        values = [f" {k} = '{v}'" for k, v in values.items()]
        return f"SET {', '.join(values)}"
    @staticmethod
    def _get_values_query(values: dict) -> str:
        if not isinstance(values, dict): raise TypeError("values = {values} is NOT dictionary")
        if len(values) == 0: return ""
        columns = []
        vs = []
        for column, v in values.items():
            columns.append(column)
            vs.append(f"'{v}'")
        return f"{', '.join(columns)} VALUES ({', '.join(vs)})"
    
    def _return(self,*querys:str) -> Psql:
        if len(querys)==0:return self
        #元の型を保持する必要がある
        new = copy(self)
        for query in querys:
            if not isinstance(query, str): raise TypeError()
            new.querys.append(query)
        return new

    def set_free_query(self, *querys: str) -> Psql:
        for query in querys:
            if not isinstance(query, str): raise TypeError()
        return self._return(*querys)