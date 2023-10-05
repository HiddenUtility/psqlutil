# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 05:27:39 2023

@author: nanik
"""

from __future__ import annotations
from psqlutil.psql import Psql
import psycopg2

class Reader(Psql):
    #@orverride
    def __add__(self,obj: Reader) -> Reader:
        if not isinstance(obj, Reader): raise TypeError()
        self.querys += obj.querys
        return Reader(self.info ,self.querys)
    #@orverride
    def set_free_query(self, *querys: str) -> Reader:
        for query in querys:
            if not isinstance(query, str): raise TypeError()
            if not self._in_query(query, "SELECT"): raise SyntaxError(f"{query}は使用できません。")
        return self._return(*querys)
    
    def read(self) -> (list[list[str]],list[str]):
        if len(self.querys) == 0: raise Exception("queryがセットされていません。")
        # connect to PostgreSQL and create table
        conn = psycopg2.connect(
            host=self._info.host, 
            port=self._info.port, 
            user=self._info.username, 
            password=self._info.password, 
            database=self._info.database
        )
        cur = conn.cursor()
        for query in self.querys:
            cur.execute(query)
        rows = cur.fetchall()
        colnames = [col.name for col in cur.description]
        # close connection
        cur.close()
        conn.close()
        self.querys = []
        return rows, colnames