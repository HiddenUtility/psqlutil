# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 22:34:15 2023

@author: iwill
"""
from __future__ import annotations
import psycopg2
import abc
from psqlutil.psql import Psql

class ICreator(Psql):
    @abc.abstractmethod
    def commit(self):
        pass

class Creator(ICreator):

    #@orverride
    def __add__(self,obj: Creator) -> Creator:
        if not isinstance(obj, Creator): raise TypeError()
        self.querys += obj.querys
        return Creator(self.info ,self.querys)

    #@override
    def commit(self) -> None:
        if len(self.querys) == 0: raise Exception("queryがセットされていません。")
        try:
            conn = psycopg2.connect(
                host=self._info.host, 
                port=self._info.port, 
                user=self._info.username, 
                password=self._info.password, 
                database=self._info.database
            )
        except Exception as ex:
            raise ex
        cur = conn.cursor()
        try:
            for query in self.querys: cur.execute(query)
            conn.commit()
            self.querys =[]
        except Exception as ex:
            raise ex
        finally:
            cur.close()
            conn.close()
    
    #@orverride
    def set_free_query(self, *querys: str) -> Creator:
        for query in querys:
            if not isinstance(query, str): raise TypeError()
            if not self._in_query(query, "CREATE"): raise SyntaxError(f"{query}は使用できません。")
        return self._return(*querys)

        