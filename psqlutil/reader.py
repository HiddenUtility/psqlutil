# -*- coding: utf-8 -*-

from __future__ import annotations
from psqlutil.psql import Psql
import psycopg2
from pandas import DataFrame
from psqlutil.connection_information import ConnectioinInfromation

class Reader(Psql):
    __info: ConnectioinInfromation
    __querys: list[str] 
    def __init__(self, info: ConnectioinInfromation=ConnectioinInfromation(), querys: list[str] = []):
        if not isinstance(info , ConnectioinInfromation): TypeError()
        if not isinstance(querys , list): TypeError()
        self.__info = info
        self.__querys = querys

    # @override
    def __add__(self,obj: Reader) -> Reader:
        if not isinstance(obj, Reader): raise TypeError()
        querys = obj.to_querys() + self.__querys
        return Reader(self.__info , querys)
    
    # @override
    def set_querys(self,querys :list[str]) -> Reader:
        querys = querys + self.__querys
        return Reader(self.__info , querys)
    
    # @override
    def to_querys(self):
        return self.__querys

    # @override
    def commit(self) -> None:
        ...
    
    def read(self) -> tuple[list[list[str]], list[str]]:
        if len(self.__querys) == 0: raise Exception("queryがセットされていません。")
        try:
            conn = psycopg2.connect(
                host=self.__info.host, 
                port=self.__info.port, 
                user=self.__info.username, 
                password=self.__info.password, 
                database=self.__info.database
            )
            cur = conn.cursor()
        except Exception as e:
            raise e

        try:
            for query in self.__querys:
                cur.execute(query)
            rows = cur.fetchall()
            colnames = [col.name for col in cur.description]
        except Exception as e:
            raise e
        finally:
            cur.close()
            conn.close()
        return rows, colnames
    
    def get_df(self) -> DataFrame:
        rows, columns = self.read()
        if len(rows) == 0:return DataFrame()
        return DataFrame(rows, columns=columns)
    